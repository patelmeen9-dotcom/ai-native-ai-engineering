# Loan Document Agent

## Problem Statement

The agent observes a loan application and its supporting documents. It must select Accept, Request Evidence, or Send to Human because the applicant's true eligibility and document authenticity are not known.

## Actions

| Action | Meaning |
|---|---|
| Accept | Documents are complete and consistent; forward to underwriting |
| Request Evidence | Something is missing, unclear, or inconsistent; ask applicant for more |
| Send to Human | High-stakes or ambiguous case; escalate to a loan officer |

## Status

- [x] Problem selected
- [x] Research file created
- [ ] Discussions conducted (in progress)
- [x] Agent designed
- [ ] Agent tested
- [ ] Preprint written
- [ ] Published

## Agent Design

### 1. Input

The agent observes:
- Loan application: amount, purpose, stated income, stated employment duration, stated debts
- Applicant credit score (external)
- Extracted document fields (OCR/parsing):
  - Payslip: income, employer, months covered, extraction confidence
  - Bank statement: monthly deposits, months covered, extraction confidence
  - ID document: name, DOB, extraction confidence
  - Proof of reserves (if provided): balance, statement period
  - Gift letter (if provided): amount, donor relation
- Document metadata: file type, creation date, tamper signals

### 2. Hidden State

Single hidden state for Week 1: **eligibility**.

| State | Meaning |
|---|---|
| ELIGIBLE | Applicant meets income, employment, DTI criteria |
| NOT_ELIGIBLE | Applicant fails at least one criterion |
| UNKNOWN | Evidence is insufficient to determine |

### 3. Belief
P(ELIGIBLE) + P(NOT_ELIGIBLE) + P(UNKNOWN) = 1.00

text

Starting prior:
- P(ELIGIBLE) = 0.70
- P(NOT_ELIGIBLE) = 0.20
- P(UNKNOWN) = 0.10

### 4. Actions

| Action | Meaning |
|---|---|
| ACCEPT | Forward to underwriting; evidence complete, consistent, high-confidence |
| REQUEST_EVIDENCE | Ask applicant for a specific missing/clarifying document (incl. LOE) |
| SEND_TO_HUMAN | Escalate: conflicting evidence, suspicion, or ambiguity |

### 5. Cost

| Error | Cost |
|---|---|
| False Accept | 100 |
| False Request | 5 |
| False Escalate | 3 |

### 6. Policy

1. If `P(NOT_ELIGIBLE) >= 0.60` → SEND_TO_HUMAN
2. If `P(UNKNOWN) >= 0.40` → REQUEST_EVIDENCE
3. If `P(ELIGIBLE) >= 0.90` → ACCEPT
4. Otherwise → REQUEST_EVIDENCE

### 7. Feedback

| Action | Feedback |
|---|---|
| ACCEPT | Human final decision |
| REQUEST_EVIDENCE | New document(s) → belief updates |
| SEND_TO_HUMAN | Human decision |

### 8. Human Reasoning Function

**Change belief after new evidence** (Bayesian update).

### 9. Evidence Types

| Evidence key | Signals | Practitioner source |
|---|---|---|
| `clean_extraction` | All fields extracted with high confidence | Design |
| `income_matches` | Payslip income ≈ bank deposits | Design |
| `income_mismatch` | Payslip ≠ bank deposits | gravitola + Nose-Previous (r/LoanProcessing) |
| `application_doc_mismatch` | Stated app data ≠ document contents | theshadowyartisan (r/Mortgages) |
| `insufficient_statement_period` | < 2 months of statements | theshadowyartisan (r/Mortgages) |
| `missing_proof_of_reserves` | Required reserve doc absent | theshadowyartisan (r/Mortgages) |
| `suspicious_metadata` | Tamper signals in file metadata | Design |

### 10. Likelihood Rationale

Key correction from practitioner feedback:
- `income_mismatch` → primarily pushes toward **UNKNOWN**, not NOT_ELIGIBLE
- Reason (gravitola): most mismatches are split deposits / multiple accounts, not fraud
- Default response to any mismatch: REQUEST_EVIDENCE, not SEND_TO_HUMAN
- Reason (Nose-Previous): "No reason to get UW involved until you know what's up"

## How to Run

(To be filled in later — will contain commands to repeat the test)