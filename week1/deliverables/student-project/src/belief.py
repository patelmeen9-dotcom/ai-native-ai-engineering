"""
belief.py

Bayesian belief update for the loan document agent.

Hidden states:
  - ELIGIBLE: applicant meets lending criteria
  - NOT_ELIGIBLE: applicant fails at least one criterion
  - UNKNOWN: evidence is insufficient to determine

Each evidence type updates the belief via Bayes' rule:
    P(state | evidence) = P(evidence | state) * P(state) / P(evidence)

Likelihood values encode "how consistent is this evidence with each state?"
They do not need to sum to 1 within a row. Only ratios matter.
"""

from typing import Dict


STATES = ["ELIGIBLE", "NOT_ELIGIBLE", "UNKNOWN"]


def normalize(beliefs: Dict[str, float]) -> Dict[str, float]:
    """Make probabilities sum to 1.0."""
    total = sum(beliefs.values())
    if total == 0:
        return {s: 1 / len(STATES) for s in STATES}
    return {s: v / total for s, v in beliefs.items()}


def prior() -> Dict[str, float]:
    """Starting belief before any evidence is seen."""
    return {
        "ELIGIBLE":     0.70,
        "NOT_ELIGIBLE": 0.20,
        "UNKNOWN":      0.10,
    }


# Likelihood table.
# Rows with high values for UNKNOWN mean "this evidence creates uncertainty".
# Rows with high values for NOT_ELIGIBLE mean "this evidence suggests a problem".
LIKELIHOODS = {
    "clean_extraction": {
        "ELIGIBLE":     0.90,
        "NOT_ELIGIBLE": 0.30,
        "UNKNOWN":      0.20,
    },
    "income_matches": {
        "ELIGIBLE":     0.95,
        "NOT_ELIGIBLE": 0.20,
        "UNKNOWN":      0.30,
    },
    # Practitioner insight (r/LoanProcessing):
    # mismatch is usually split deposits, not fraud -> push to UNKNOWN
    "income_mismatch": {
        "ELIGIBLE":     0.50,
        "NOT_ELIGIBLE": 0.30,
        "UNKNOWN":      0.85,
    },
    # Practitioner insight (r/Mortgages): "the whole thing stalls"
    "application_doc_mismatch": {
        "ELIGIBLE":     0.15,
        "NOT_ELIGIBLE": 0.70,
        "UNKNOWN":      0.50,
    },
    "insufficient_statement_period": {
        "ELIGIBLE":     0.30,
        "NOT_ELIGIBLE": 0.25,
        "UNKNOWN":      0.85,
    },
    "missing_proof_of_reserves": {
        "ELIGIBLE":     0.40,
        "NOT_ELIGIBLE": 0.30,
        "UNKNOWN":      0.80,
    },
    "suspicious_metadata": {
        "ELIGIBLE":     0.05,
        "NOT_ELIGIBLE": 0.70,
        "UNKNOWN":      0.40,
    },
}


def update_belief(
    prior: Dict[str, float],
    likelihoods: Dict[str, float],
) -> Dict[str, float]:
    """Apply Bayes' rule to produce a posterior distribution."""
    posterior = {}
    for s in STATES:
        posterior[s] = likelihoods.get(s, 1.0) * prior[s]
    return normalize(posterior)


if __name__ == "__main__":
    print("Prior:", prior())
    print()
    for key in LIKELIHOODS:
        posterior = update_belief(prior(), LIKELIHOODS[key])
        rounded = {k: round(v, 3) for k, v in posterior.items()}
        print(f"{key:35s} -> {rounded}")