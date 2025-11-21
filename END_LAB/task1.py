import re
from typing import Callable, Optional

"""
task1.py

A small utility to convert long clinical doctor notes into short structured
summaries using prompt engineering. This file contains a mock AI model call
and tests demonstrating usage.

Note: This mock model is for demonstration and testing only and does not
provide clinical advice.
"""



def build_prompt(note: str) -> str:
    """
    Build a clear, structured prompt to instruct an AI model to convert a
    free-text clinical note into a short, structured summary.

    The prompt asks for a compact output with the following fields:
      - Chief Complaint
      - History of Present Illness (HPI)
      - Assessment / Diagnosis
      - Medications
      - Plan
      - Follow-up / Next Steps

    The model is instructed to be brief (1-3 lines per field) and omit any
    extraneous text.
    """
    instruction = (
        "You are a medical note summarizer. Convert the input doctor note into "
        "a concise structured summary with the exact fields below. Output only "
        "the fields and short contents (1-3 lines each). If a field is not "
        "present, leave it blank.\n\n"
        "FIELDS:\n"
        "Chief Complaint:\n"
        "History of Present Illness (HPI):\n"
        "Assessment / Diagnosis:\n"
        "Medications:\n"
        "Plan:\n"
        "Follow-up / Next Steps:\n\n"
        "Now summarize the following note:\n"
    )
    return instruction + note


def mock_ai_model(prompt: str, max_chars: int = 1000) -> str:
    """
    Mock AI model that heuristically extracts common sections and key
    information from a clinical note text provided in the prompt.

    This function is NOT a real medical summarizer. It uses simple regex and
    heuristics to produce a short structured summary that matches the requested
    field layout.
    """
    # Extract the original note from the prompt by removing the instruction part.
    # We assume the note appears after the last blank line or after the phrase "Now summarize the following note:"
    parts = prompt.split("Now summarize the following note:")
    note = parts[-1].strip() if len(parts) > 1 else prompt

    # Helper: find first match by many possible keys (case-insensitive)
    def find_section(patterns):
        for pat in patterns:
            # Look for lines like "Key: content"
            m = re.search(r"(?mi)^\s*" + re.escape(pat) + r"\s*[:\-]\s*(.+)$", note)
            if m:
                return m.group(1).strip()
        return ""

    # Patterns for common fields
    cc = find_section(["Chief Complaint", "CC", "Complaint"])
    hpi = find_section(["History of Present Illness", "HPI", "History"])
    assessment = find_section(["Assessment", "Diagnosis", "Impression", "Dx"])
    meds = find_section(["Medications", "Meds", "Current Medications", "Rx"])
    plan = find_section(["Plan", "Treatment Plan", "Recommendations"])
    follow = find_section(["Follow-up", "Follow up", "Next Steps"])

    # If explicit sections not found, use heuristics:
    if not cc:
        # Try to use the first sentence as chief complaint
        sentences = re.split(r'(?<=[.!?])\s+', note)
        cc = sentences[0].strip() if sentences and len(sentences[0]) <= 200 else ""

    if not hpi:
        # Look for a few sentences that reference onset, duration, or course
        hpi_candidates = re.findall(r'(?mi)(?:since|for|started|onset|history|progressed|worsen|improve)[^.\n]*[.\n]?', note)
        if hpi_candidates:
            hpi = " ".join([s.strip() for s in hpi_candidates])[:300]

    if not assessment:
        # Look for patterns like "likely X", "consistent with", or words ending in -itis/-osis
        m = re.search(r'(?mi)(diagnosis[:\-]?\s*)([^\n.]+)', note)
        if m:
            assessment = m.group(2).strip()
        else:
            # fallback: pick sentences containing "diagnos", "impress", "consistent with", "likely"
            m2 = re.search(r'(?mi)([^.]*?(diagnos|impress|likely|consistent|rule out)[^.]*\.)', note)
            assessment = (m2.group(1).strip() if m2 else assessment)[:300]

    if not meds:
        # Find common medication words or lines with dosing
        m_med_lines = re.findall(r'(?mi)^[\-\*\s]*([A-Za-z0-9\(\)\/\+\- ]{3,40}\b(?:mg|mcg|units|tablet|tab|capsule|ml)?)', note, re.M)
        if m_med_lines:
            meds = ", ".join(dict.fromkeys([s.strip() for s in m_med_lines]))[:300]

    if not plan:
        # Extract sentences with "plan", "recommend", "advise", "start", "refer"
        m_plan = re.findall(r'(?mi)(?:plan|recommend|advise|start|refer)[^.\n]*[.\n]?', note)
        if m_plan:
            plan = " ".join([s.strip() for s in m_plan])[:300]

    if not follow:
        # Look for "follow up in X weeks/days" patterns
        m_follow = re.search(r'(?mi)(follow[ -]?up(?: in)? [^.\n]+)', note)
        if m_follow:
            follow = m_follow.group(1).strip()
        else:
            # generic fallback
            if "follow-up" in note.lower() or "follow up" in note.lower():
                follow = "See note for follow-up plan."

    # Ensure short outputs (1-3 lines per field)
    def truncate_field(text, limit=300):
        return (text[:limit].rstrip() + ("..." if len(text) > limit else "")).strip()

    summary = (
        f"Chief Complaint: {truncate_field(cc, 200)}\n"
        f"History of Present Illness (HPI): {truncate_field(hpi, 400)}\n"
        f"Assessment / Diagnosis: {truncate_field(assessment, 300)}\n"
        f"Medications: {truncate_field(meds, 300)}\n"
        f"Plan: {truncate_field(plan, 400)}\n"
        f"Follow-up / Next Steps: {truncate_field(follow, 200)}"
    )

    return summary[:max_chars]


def summarize_clinical_note(note: str, model: Optional[Callable[[str], str]] = None) -> str:
    """
    Main function to summarize a clinical note.

    Parameters:
      - note: raw doctor note (string)
      - model: callable that accepts a prompt string and returns the model output.
               If None, the mock_ai_model is used.

    Returns:
      - A short structured summary string produced by the model.
    """
    prompt = build_prompt(note)
    model = model or (lambda p: mock_ai_model(p, max_chars=1500))
    return model(prompt)


# -----------------------
# Simple test cases
# -----------------------
def _run_tests():
    """
    Run three simple test cases demonstrating the summarizer behavior.
    These are basic unit-test style examples; in production, use a test framework.
    """
    notes = [
        # Test 1: Structured note with labels
        (
            "Chief Complaint: Chest pain\n"
            "History of Present Illness: 56-year-old male with 2 hours of substernal chest pain, "
            "radiating to left arm, started while gardening. Hypertension and hyperlipidemia.\n"
            "Assessment: Acute coronary syndrome, rule out myocardial infarction.\n"
            "Medications: Aspirin 325 mg PO, Nitroglycerin 0.4 mg SL PRN.\n"
            "Plan: EKG, troponin x3, cardiology consult, admit to telemetry.\n"
            "Follow-up: Admit and monitor; repeat troponin in 3 hours."
        ),
        # Test 2: Free-text long note
        (
            "Patient is a 30-year-old woman who presents with a 3-week history of worsening "
            "fatigue and intermittent palpitations. She states symptoms began after a viral illness. "
            "No chest pain but reports shortness of breath on exertion. Past medical history includes "
            "iron deficiency anemia diagnosed last year. On exam, pulse irregularly irregular. "
            "Impression: likely atrial fibrillation possibly related to anemia. "
            "Recommend CBC, TSH, start metoprolol 25 mg PO BID for rate control, and refer to cardiology. "
            "Follow up in 1 week or sooner for worsening symptoms."
        ),
        # Test 3: Short note with minimal info
        (
            "Complaint: cough and fever x2 days. Likely viral URI. Recommend rest, fluids, acetaminophen PRN. "
            "Return if symptoms worsen or fever > 103F."
        )
    ]

    for i, note in enumerate(notes, start=1):
        print(f"\n--- Test Case {i} ---")
        summary = summarize_clinical_note(note)
        print(summary)


if __name__ == "__main__":
    _run_tests()