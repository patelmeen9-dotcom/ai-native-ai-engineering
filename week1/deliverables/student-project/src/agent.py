"""
agent.py

The loan document decision agent.

Flow:
  1. Start with a prior belief over hidden states.
  2. Update the belief with each piece of evidence via Bayes' rule.
  3. Apply the decision policy to choose one action.

Actions:
  ACCEPT            -- evidence is strong; forward to underwriting
  REQUEST_EVIDENCE  -- evidence is incomplete; ask for more
  SEND_TO_HUMAN     -- high-stakes or ambiguous; escalate
"""

from typing import Dict, List, Tuple

from .belief import (
    STATES,
    LIKELIHOODS,
    prior,
    update_belief,
)


# --- Action names ----------------------------------------------------------

ACCEPT = "ACCEPT"
REQUEST_EVIDENCE = "REQUEST_EVIDENCE"
SEND_TO_HUMAN = "SEND_TO_HUMAN"

ACTIONS = [ACCEPT, REQUEST_EVIDENCE, SEND_TO_HUMAN]


# --- Policy thresholds -----------------------------------------------------
# Hypotheses, not facts. We will tune these during the experiment step.

ACCEPT_THRESHOLD = 0.90          # P(ELIGIBLE) must be at least this to accept
SUSPICION_THRESHOLD = 0.60       # P(NOT_ELIGIBLE) above this -> escalate
UNKNOWN_THRESHOLD = 0.40         # P(UNKNOWN) above this -> request evidence


# --- Decision rule ---------------------------------------------------------

def decide(beliefs: Dict[str, float]) -> Tuple[str, str]:
    """
    Apply the policy to a belief distribution.

    Returns (action, reason).
    """
    p_eligible = beliefs["ELIGIBLE"]
    p_not_eligible = beliefs["NOT_ELIGIBLE"]
    p_unknown = beliefs["UNKNOWN"]

    # Rule 1: strong suspicion -> escalate
    if p_not_eligible >= SUSPICION_THRESHOLD:
        return (
            SEND_TO_HUMAN,
            f"P(NOT_ELIGIBLE)={p_not_eligible:.2f} >= {SUSPICION_THRESHOLD}",
        )

    # Rule 2: too much unknown -> request evidence
    if p_unknown >= UNKNOWN_THRESHOLD:
        return (
            REQUEST_EVIDENCE,
            f"P(UNKNOWN)={p_unknown:.2f} >= {UNKNOWN_THRESHOLD}",
        )

    # Rule 3: strong evidence of eligibility -> accept
    if p_eligible >= ACCEPT_THRESHOLD:
        return (
            ACCEPT,
            f"P(ELIGIBLE)={p_eligible:.2f} >= {ACCEPT_THRESHOLD}",
        )

    # Rule 4: default -> request evidence
    return (
        REQUEST_EVIDENCE,
        f"P(ELIGIBLE)={p_eligible:.2f} below {ACCEPT_THRESHOLD}, "
        f"P(UNKNOWN)={p_unknown:.2f} below {UNKNOWN_THRESHOLD}",
    )


# --- Full pipeline ---------------------------------------------------------

def run_agent(evidence_keys: List[str], verbose: bool = False) -> Dict:
    """
    Run the full pipeline: prior -> sequential Bayes updates -> decision.

    Returns a dict with the trace, final beliefs, action, and reason.
    """
    beliefs = prior()
    trace = [{"step": 0, "evidence": None, "beliefs": dict(beliefs)}]

    for i, key in enumerate(evidence_keys, start=1):
        if key not in LIKELIHOODS:
            raise ValueError(f"Unknown evidence key: {key}")
        beliefs = update_belief(beliefs, LIKELIHOODS[key])
        trace.append({"step": i, "evidence": key, "beliefs": dict(beliefs)})

    action, reason = decide(beliefs)

    if verbose:
        print(f"Evidence: {evidence_keys}")
        for entry in trace:
            rounded = {k: round(v, 3) for k, v in entry["beliefs"].items()}
            label = entry["evidence"] or "prior"
            print(f"  step {entry['step']}: {label:30s} -> {rounded}")
        print(f"Action: {action}")
        print(f"Reason: {reason}")
        print()

    return {
        "evidence": evidence_keys,
        "final_beliefs": beliefs,
        "action": action,
        "reason": reason,
        "trace": trace,
    }


# --- Demo ------------------------------------------------------------------

if __name__ == "__main__":
    demo_cases = [
        ["clean_extraction", "income_matches"],
        ["income_mismatch"],
        ["application_doc_mismatch"],
        ["suspicious_metadata"],
        ["clean_extraction", "missing_proof_of_reserves"],
    ]
    for case in demo_cases:
        run_agent(case, verbose=True)
        print("-" * 70)