# Discussion Record — Loan Document Agent

This file records every Reddit and X contribution made during this project,
and — for each useful human reply — what design change (if any) resulted.

**Status:** In progress. Reddit discussions active; some replies received.
X discussions deferred (see `research-file.md` section 6).

## Legend for "Design change"

Each useful human answer is mapped to one of:
- **A** = new assumption
- **B** = new failure condition
- **C** = new test
- **D** = change to the agent
- **E** = change to the probability model
- **F** = no change, with reason

## Contributions Table

| # | Platform | Community | Link | My first contribution | Human answer | My next answer | Design change |
|---|---|---|---|---|---|---|---|
| 1 | Reddit | r/LoanProcessing | https://www.reddit.com/r/LoanProcessing/comments/1wld0p5/processors_when_a_paystub_and_bank_statement/ | Post: "Processors: when a paystub and bank statement disagree on income, what's your next move?" — asked how processors handle conflicting income evidence and whether they ask, request more, or escalate. | u/gravitola: "Paystub net income vs bank deposit mismatch is usually normal — split deposits or multiple accounts. A real mismatch is a major employer error, not applicant fraud. Would never escalate to UW; would just ask for explanation + supporting docs." | Replied: thanked them for the insight. | **E** — change to probability model: `income_mismatch` is NOT strong evidence of `NOT_ELIGIBLE`. It should mainly push belief toward `UNKNOWN`, not `NOT_ELIGIBLE`. |
| 2 | Reddit | r/LoanProcessing | https://www.reddit.com/r/LoanProcessing/comments/1wld0p5/processors_when_a_paystub_and_bank_statement/ | Same thread — second human replied. | u/Nose-Previous (MOD): "A and B immediately for sure. No reason to get UW involved until you know what's up. May be an easy explanation, may need to just lower income to what you can prove on statements, may be a deal killer. Sometimes a LOE can suffice." | Replied: thanked them; confirmed design insight that mismatch → request, not escalate. | **D + E** (reinforces #1) — REQUEST_EVIDENCE is the correct first response to `income_mismatch`, not SEND_TO_HUMAN. New document type: LOE (Letter of Explanation). |
| 3 | Reddit | r/Mortgages | https://www.reddit.com/r/Mortgages/comments/1wld6rl/beginner_building_a_loan_doc_review_agent_what/ | Post: "Beginner building a loan doc review agent — what does a good underwriting file actually look like?" — asked first check, most-common missing docs, and what makes a clean file. | u/theshadowyartisan: "First check: application matches supporting docs, esp. income + employment. If paystubs don't line up, everything stalls. Most missing: proof of reserves, 2 months of statements (only 30 days often submitted), gift letters. Clean file = numbers reconcile, assets seasoned, no surprise debts on credit report." | Replied: thanked them; noted application-vs-doc check and evidence completeness as signals. | **A + D** — new assumption: application-vs-document mismatch is distinct from document-vs-document mismatch. New evidence types: `application_doc_mismatch`, `insufficient_statement_period`, `missing_proof_of_reserves`. |
| 4 | Reddit | r/loanoriginators | https://www.reddit.com/r/loanoriginators/comments/1wld2xp/how_often_do_apps_stall_from_missing_docs_vs/ | Post: "How often do apps stall from missing docs vs. inconsistent docs vs. suspicious docs?" — asked for a rough distribution of the three failure modes in real files. | Pending | Pending | Pending |
| 5 | Reddit | r/Underwriting | https://www.reddit.com/r/Underwriting/comments/1wld4av/underwriters_have_you_ever_had_a_file_where/ | Post: "Underwriters — have you ever had a file where documents looked fine but something felt off?" — asked what subtle signals make an underwriter slow down. | Pending | Pending | Pending |
| 6 | Reddit | r/asktheunderwriter | https://www.reddit.com/r/asktheunderwriter/comments/1wld5rt/beginner_building_a_loan_doc_review_agent_what/ | Post: "Beginner building a loan doc review agent: what subtle signals make you slow down?" — same question, adapted to the audience of underwriters answering borrower/LO questions. | Pending | Pending | Pending |

## Progress

- **Reddit contributions made:** 9 (5 posts + 3 replies + 1 reply on r/LoanProcessing mod thread)
- **Reddit discussions with 2+ replies:** 1 complete (r/LoanProcessing — 2 human replies + my replies)
- **Reddit discussions in progress:** 1 (r/Mortgages — 1 human reply, my reply posted)
- **X contributions made:** 0 (deferred — documented in `research-file.md`)
- **Design changes from discussions:** 3 (income_mismatch likelihood, action ordering, new evidence types)

## Notes / Open Items

- **2nd contributions:** Still needed in communities where no discussion formed yet (r/loanoriginators, r/Underwriting, r/asktheunderwriter).
- **Karma blockers:** r/fintech, r/MLQuestions, r/MachineLearning, r/learnmachinelearning, r/computervision, r/datascience, r/AI_Agents — cannot post until karma improves.
- **No fabrication rule:** This file will not contain any human reply I did not actually receive.

## How to Update This File

1. When a human replies, paste the reply summary in the **Human answer** column.
2. When I reply back, write a one-line summary in **My next answer**.
3. If the exchange changed my design, note the change in **Design change** using the legend (A–F).
4. Update the **Progress** section counts.