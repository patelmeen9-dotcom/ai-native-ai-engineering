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
