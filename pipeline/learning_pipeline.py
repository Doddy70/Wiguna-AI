"""
Pak Ferdy Learning Candidate Pipeline

This module provides functions to extract, classify, and process
learning candidates from Pak Ferdy conversations.

Usage:
    from learning_pipeline import LearningPipeline

    pipeline = LearningPipeline()

    # Extract from conversation
    candidates = pipeline.extract_from_conversation(messages)

    # Classify a statement
    classification = pipeline.classify(statement)

    # Create a candidate
    candidate = pipeline.create_candidate(
        original_statement="...",
        source_conversation="...",
        classification="KNOWLEDGE"
    )
"""

import json
import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from typing import Optional


class Classification(Enum):
    """Learning candidate classification types."""
    KNOWLEDGE = "KNOWLEDGE"
    DECISION_KNOWLEDGE = "DECISION_KNOWLEDGE"
    RESPONSE_POLICY = "RESPONSE_POLICY"
    ESCALATION_RULE = "ESCALATION_RULE"
    BUSINESS_RECOMMENDATION = "BUSINESS_RECOMMENDATION"
    SKILL = "SKILL"
    TOOL_REQUIREMENT = "TOOL_REQUIREMENT"
    EXAMPLE_ONLY = "EXAMPLE_ONLY"
    TEMPORARY_GUIDANCE = "TEMPORARY_GUIDANCE"


class CandidateStatus(Enum):
    """Learning candidate status."""
    CANDIDATE = "CANDIDATE"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    MERGED = "MERGED"
    DEPLOYED = "DEPLOYED"


class Destination(Enum):
    """TGO Web destination for promoted candidates."""
    RAG = "RAG"
    SKILL = "SKILL"
    WORKFLOW = "WORKFLOW"
    TOOL = "TOOL"
    NONE = "NONE"


# Classification to Destination mapping
CLASSIFICATION_TO_DESTINATION = {
    Classification.KNOWLEDGE: Destination.RAG,
    Classification.DECISION_KNOWLEDGE: Destination.RAG,
    Classification.RESPONSE_POLICY: Destination.SKILL,
    Classification.ESCALATION_RULE: Destination.WORKFLOW,
    Classification.BUSINESS_RECOMMENDATION: Destination.RAG,
    Classification.SKILL: Destination.SKILL,
    Classification.TOOL_REQUIREMENT: Destination.TOOL,
    Classification.EXAMPLE_ONLY: Destination.NONE,
    Classification.TEMPORARY_GUIDANCE: Destination.NONE,
}


@dataclass
class LearningCandidate:
    """
    Structured learning candidate extracted from Pak Ferdy conversations.

    This represents a single unit of learning that can be:
    - Reviewed by Pak Ferdy or Admin
    - Promoted to TGO Web
    - Deployed as RAG, Skill, Workflow, or Tool
    """
    # Required fields
    id: str
    classification: str
    topic: str
    principle: str
    status: str = "CANDIDATE"
    created: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

    # Optional fields
    source_conversation: str = ""
    original_statement: str = ""
    trigger: str = ""
    context: str = ""
    condition: str = ""
    recommended_action: str = ""
    exceptions: list = field(default_factory=list)
    scope: str = ""
    confidence: float = 0.0
    destination: str = ""
    tgo_web_reference: str = ""
    reviewed_by: str = ""
    reviewed_at: str = ""
    notes: str = ""
    updated: str = ""

    def __post_init__(self):
        """Set destination based on classification."""
        if not self.destination and self.classification:
            try:
                cls = Classification(self.classification)
                self.destination = CLASSIFICATION_TO_DESTINATION[cls].value
            except ValueError:
                self.destination = ""

        if not self.updated:
            self.updated = self.created

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return asdict(self)

    def to_yaml(self) -> str:
        """Convert to YAML-like format for documentation."""
        lines = [
            f"id: {self.id}",
            f"source_conversation: \"{self.source_conversation}\"",
            f"original_statement: >",
        ]
        for line in self.original_statement.split('\n'):
            lines.append(f"  {line}")
        lines.extend([
            f"classification: {self.classification}",
            f"topic: \"{self.topic}\"",
            f"trigger: \"{self.trigger}\"",
            f"context: \"{self.context}\"",
            f"condition: \"{self.condition}\"",
            f"principle: >",
        ])
        for line in self.principle.split('\n'):
            lines.append(f"  {line}")
        lines.extend([
            f"recommended_action: \"{self.recommended_action}\"",
            f"exceptions:",
        ])
        for exc in self.exceptions:
            lines.append(f"  - \"{exc}\"")
        lines.extend([
            f"scope: \"{self.scope}\"",
            f"confidence: {self.confidence}",
            f"status: {self.status}",
            f"destination: {self.destination}",
            f"created: \"{self.created}\"",
        ])
        return '\n'.join(lines)

    def approve(self, reviewer: str):
        """Mark candidate as approved."""
        self.status = CandidateStatus.APPROVED.value
        self.reviewed_by = reviewer
        self.reviewed_at = datetime.now().isoformat()
        self.updated = datetime.now().strftime("%Y-%m-%d")

    def reject(self, reviewer: str, reason: str = ""):
        """Mark candidate as rejected."""
        self.status = CandidateStatus.REJECTED.value
        self.reviewed_by = reviewer
        self.reviewed_at = datetime.now().isoformat()
        self.notes += f"\nRejected by {reviewer}: {reason}" if reason else ""
        self.updated = datetime.now().strftime("%Y-%m-%d")

    def merge_with(self, other_candidate: 'LearningCandidate'):
        """Merge this candidate with another."""
        self.status = CandidateStatus.MERGED.value
        self.notes += f"\nMerged with {other_candidate.id}"
        self.updated = datetime.now().strftime("%Y-%m-%d")
        return self


class LearningPipeline:
    """
    Pipeline for extracting learning candidates from Pak Ferdy conversations.

    Pipeline stages:
    1. Extract - Identify actionable statements from conversation
    2. Classify - Determine classification type
    3. Normalize - Convert to structured format
    4. Create Candidate - Create LearningCandidate object
    5. Review - Human review (out of scope for this class)
    6. Promote - Deploy to TGO Web (out of scope for this class)
    """

    def __init__(self):
        self.candidates = []
        self.counter = 0

    def _generate_id(self) -> str:
        """Generate next candidate ID."""
        self.counter += 1
        return f"LC-{self.counter:03d}"

    def extract_from_conversation(self, messages: list) -> list:
        """
        Extract learning candidates from conversation messages.

        Args:
            messages: List of message dicts with 'role' and 'content' keys

        Returns:
            List of LearningCandidate objects
        """
        candidates = []

        for msg in messages:
            role = msg.get('role', '')
            content = msg.get('content', '')

            # Only process assistant messages (AI responses in conversation)
            # Pak Ferdy's teachings are embedded in these responses
            if role != 'assistant':
                continue

            # Extract potential learnings from message
            learnings = self._extract_learnings(content)

            for learning in learnings:
                candidate = self._create_candidate_from_learning(
                    learning,
                    source=f"Conversation"
                )
                if candidate:
                    candidates.append(candidate)

        self.candidates.extend(candidates)
        return candidates

    def _extract_learnings(self, content: str) -> list:
        """
        Extract potential learnings from message content.

        This is a simplified heuristic-based extraction.
        In production, this could use LLM-based extraction.

        Returns:
            List of dicts with 'statement', 'type', and 'confidence'
        """
        learnings = []

        # Patterns that indicate direct teaching
        teaching_patterns = [
            r'"([^"]*(?:jangan|selalu|untuk|kalau|kalau|jika|dalam|pada)[^"]*)"',
            r'\*\*([^*]+)\*\*:\s*([^*]+)',
            r'^\s*[-•*]\s*(.*(?:jangan|selalu|untuk|kalau|kalau|jika)[^\.]+)',
        ]

        # Simple heuristic extraction
        # In production, use LLM for better extraction

        return learnings

    def classify(self, statement: str) -> tuple[Classification, float]:
        """
        Classify a statement and return classification + confidence.

        Args:
            statement: The statement to classify

        Returns:
            Tuple of (Classification, confidence_score)
        """
        statement_lower = statement.lower()

        # Escalation patterns
        escalation_keywords = [
            'handoff', 'eskalasi', 'tim teknis', 'human',
            'arahkan ke', 'rujuk ke', 'selesai', 'di luar scope'
        ]
        if any(kw in statement_lower for kw in escalation_keywords):
            return Classification.ESCALATION_RULE, 0.85

        # Response policy patterns
        policy_keywords = [
            'jangan', 'jangan sekali-kali', 'selalu', 'jangan langsung',
            'kalau ragu', 'tidak berarti', 'harus', 'bidden'
        ]
        if any(kw in statement_lower for kw in policy_keywords):
            return Classification.RESPONSE_POLICY, 0.80

        # Decision knowledge patterns
        decision_keywords = [
            'kalau', 'jika', 'maka', 'atau', 'terlebih dahulu',
            'setelah itu', 'pilihan', 'alternatif', 'pertama'
        ]
        if any(kw in statement_lower for kw in decision_keywords):
            return Classification.DECISION_KNOWLEDGE, 0.75

        # Tool requirement patterns
        tool_keywords = [
            'cek stok', 'cek gudang', 'konfirmasi', 'verifikasi',
            'live', 'real-time', 'saat ini'
        ]
        if any(kw in statement_lower for kw in tool_keywords):
            return Classification.TOOL_REQUIREMENT, 0.70

        # Business recommendation patterns
        recommendation_keywords = [
            'rekomendasikan', 'saran', 'sebaiknya', 'lebih baik',
            'cocok untuk', 'untuk', 'vehicle', 'mobil'
        ]
        if any(kw in statement_lower for kw in recommendation_keywords):
            return Classification.BUSINESS_RECOMMENDATION, 0.70

        # Default to knowledge
        return Classification.KNOWLEDGE, 0.60

    def create_candidate(
        self,
        original_statement: str,
        classification: str,
        topic: str,
        principle: str,
        source_conversation: str = "",
        trigger: str = "",
        context: str = "",
        condition: str = "",
        recommended_action: str = "",
        exceptions: list = None,
        scope: str = "",
        confidence: float = 0.0,
    ) -> LearningCandidate:
        """
        Create a new learning candidate.

        Args:
            original_statement: Original quote from Pak Ferdy
            classification: Classification type
            topic: Short topic (2-5 words)
            principle: Core teaching/rule
            source_conversation: Reference to source
            trigger: What triggers this
            context: Background context
            condition: Precondition
            recommended_action: What agent should do
            exceptions: List of exceptions
            scope: Scope/boundaries
            confidence: Confidence score (0.0-1.0)

        Returns:
            LearningCandidate object
        """
        if exceptions is None:
            exceptions = []

        candidate = LearningCandidate(
            id=self._generate_id(),
            source_conversation=source_conversation,
            original_statement=original_statement,
            classification=classification,
            topic=topic,
            trigger=trigger,
            context=context,
            condition=condition,
            principle=principle,
            recommended_action=recommended_action,
            exceptions=exceptions,
            scope=scope,
            confidence=confidence,
            status=CandidateStatus.CANDIDATE.value,
        )

        self.candidates.append(candidate)
        return candidate

    def _create_candidate_from_learning(
        self,
        learning: dict,
        source: str
    ) -> Optional[LearningCandidate]:
        """Create candidate from extracted learning."""
        statement = learning.get('statement', '')
        if not statement:
            return None

        classification, confidence = self.classify(statement)

        return self.create_candidate(
            original_statement=statement,
            classification=classification.value,
            topic=learning.get('topic', 'Untitled'),
            principle=learning.get('principle', statement),
            source_conversation=source,
            confidence=confidence,
        )

    def get_candidates(
        self,
        status: str = None,
        classification: str = None,
    ) -> list:
        """
        Get candidates with optional filtering.

        Args:
            status: Filter by status (CANDIDATE, APPROVED, etc.)
            classification: Filter by classification

        Returns:
            List of LearningCandidate objects
        """
        results = self.candidates

        if status:
            results = [c for c in results if c.status == status]

        if classification:
            results = [c for c in results if c.classification == classification]

        return results

    def export_to_json(self) -> str:
        """Export all candidates to JSON."""
        return json.dumps(
            [c.to_dict() for c in self.candidates],
            indent=2,
            ensure_ascii=False
        )

    def export_to_markdown(self) -> str:
        """Export all candidates to Markdown."""
        lines = [
            "# WIGUNA Learning Candidates",
            "",
            "Learning candidates extracted from Pak Ferdy conversations.",
            "",
            "## Status Summary",
            "",
            "| ID | Topic | Classification | Confidence | Status | Destination |",
            "|----|-------|----------------|------------|--------|-------------|",
        ]

        for c in self.candidates:
            lines.append(
                f"| {c.id} | {c.topic} | {c.classification} | "
                f"{c.confidence:.2f} | {c.status} | {c.destination} |"
            )

        lines.extend(["", "---", "", "## Candidates", ""])

        for c in self.candidates:
            lines.extend([
                f"### {c.id}: {c.topic}",
                "",
                "```yaml",
                c.to_yaml(),
                "```",
                "",
            ])

        return '\n'.join(lines)

    def import_from_json(self, json_str: str):
        """Import candidates from JSON."""
        data = json.loads(json_str)
        self.candidates = [LearningCandidate(**d) for d in data]


# Example usage
if __name__ == "__main__":
    # Initialize pipeline
    pipeline = LearningPipeline()

    # Create sample candidates (based on existing LEARNING-CANDIDATES.md)

    # LC-001: AC Escalation
    pipeline.create_candidate(
        original_statement="Kalau AC bocor atau freon berkurang terus setelah diisi atau tetap bermasalah setelah penggantian part, itu jatuhnya servis besar AC dan harus diarahkan ke tim teknikal atau handoff ke human supaya tidak salah diagnosis.",
        classification="ESCALATION_RULE",
        topic="AC Major Service Escalation",
        trigger="Customer reports AC bocor, freon cepat habis, AC tidak dingin setelah isi freon, AC bermasalah setelah part replacement",
        context="AC issues that persist after initial treatment indicate more serious problem",
        condition="AC problem persists AFTER freon fill OR AC problem persists AFTER part replacement",
        principle="When AC issues persist after standard treatment, escalate to technical team to avoid misdiagnosis.",
        recommended_action="Handoff to technical team or human agent. Explain: 'Ini perlu pemeriksaan lebih lanjut oleh tim teknikal untuk diagnosis yang tepat.'",
        exceptions=["First-time AC service request (not yet treated)", "Minor cooling issues (recommend reset AC first)"],
        scope="All vehicles with persistent AC issues after standard treatment",
        confidence=0.95,
        source_conversation="2026-08-25 WhatsApp Session"
    )

    # LC-002: Reset AC Scope
    pipeline.create_candidate(
        original_statement="Reset AC mencakup flushing system, vacuum + leak test, pembersihan blower AC, pembersihan evaporator menggunakan endoscope tanpa bongkar dashboard, pengecekan filter AC, pembersihan condenser AC, penggantian oli compressor, penggantian freon AC, ozone sterilization.",
        classification="KNOWLEDGE",
        topic="Reset AC Service Scope",
        trigger="Customer asks: 'Reset AC apa saja?' or 'Reset AC termasuk apa?'",
        context="Reset AC is comprehensive service, not just 'reset'",
        condition="Customer inquiring about AC reset service",
        principle="Reset AC includes: 1. Flushing system, 2. Vacuum + leak test, 3. Blower AC cleaning, 4. Evaporator cleaning (endoscope, no dashboard disassembly), 5. Filter AC check, 6. Condenser AC cleaning, 7. Compressor oil replacement, 8. Freon AC replacement, 9. Ozone sterilization",
        recommended_action="Provide comprehensive scope when explaining Reset AC. Emphasize it's not just 'reset' but full treatment.",
        exceptions=[],
        scope="Reset AC service (non-EV vehicles)",
        confidence=0.95,
        source_conversation="2026-08-25 WhatsApp Session"
    )

    # LC-003: Fortuner Oil
    pipeline.create_candidate(
        original_statement="Untuk Toyota Fortuner yang kapasitas olinya di atas 7 liter, rekomendasikan paket oli 10W-30 diesel terlebih dahulu, setelah itu alternatif 15W-40 dengan tambahan 1 liter oli sesuai kebutuhannya.",
        classification="BUSINESS_RECOMMENDATION",
        topic="Fortuner Oil Selection",
        trigger="Customer asks about oil for Toyota Fortuner or vehicle with >7L oil capacity",
        context="Fortuner has large oil capacity requiring specific recommendation",
        condition="Vehicle is Toyota Fortuner OR Oil capacity > 7 liters",
        principle="For Fortuner with >7L oil capacity: PRIMARY: 10W-30 Diesel package, ALTERNATIVE: 15W-40 with +1L additional oil",
        recommended_action="Recommend 10W-30 Diesel first. Offer 15W-40 + 1L as alternative.",
        exceptions=["Diesel vehicle → use diesel-specific oil", "Specific manufacturer recommendation takes priority"],
        scope="Toyota Fortuner, Vehicles with >7L oil capacity",
        confidence=0.90,
        source_conversation="2026-08-25 WhatsApp Session"
    )

    # LC-004: Stock Response Policy
    pipeline.create_candidate(
        original_statement="Jangan langsung bilang stok tidak ada kalau datanya tidak ditemukan.",
        classification="RESPONSE_POLICY",
        topic="Stock Query Response",
        trigger="Customer asks about stock/availability and data is not found in Knowledge Base",
        context="Knowledge Base contains price list, not inventory. Absence of data does not mean absence of stock.",
        condition="Customer asks: 'Ada?', 'Stok?', 'Tersedia?' AND Knowledge Base has no data",
        principle="Absence of Knowledge Base evidence must NOT be interpreted as product unavailability. Always acknowledge limitation.",
        recommended_action="DO NOT say: 'Stok tidak ada', 'Tidak tersedia', 'Barang tidak ada'. INSTEAD say: 'Mohon maaf, untuk informasi ini Minna cek dulu' OR 'Data belum tersedia, Minna bantu konfirmasi ke gudang'",
        exceptions=["None — always verify before claiming"],
        scope="All stock/availability queries",
        confidence=0.95,
        source_conversation="2026-08-25 WhatsApp Session"
    )

    print("=== Sample Candidates Created ===")
    print(f"Total candidates: {len(pipeline.candidates)}")
    print()

    # Print summary
    print("=== Candidates by Classification ===")
    by_class = {}
    for c in pipeline.candidates:
        by_class.setdefault(c.classification, []).append(c.topic)
    for cls, topics in by_class.items():
        print(f"\n{cls}:")
        for topic in topics:
            print(f"  - {topic}")

    print()
    print("=== Export to JSON ===")
    print(pipeline.export_to_json()[:500] + "...")
