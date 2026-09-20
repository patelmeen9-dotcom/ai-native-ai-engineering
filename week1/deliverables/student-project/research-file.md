# Research File — Loan Document Agent

## 1. My Background

- **Experience level:** Beginner. Little to no prior experience with AI agents, probabilistic modeling, or loan underwriting.
- **Selected problem:** Loan document agent.
- **Project objective:** Design, build, and test an AI agent that decides **Accept**, **Request Evidence**, or **Send to Human** for a loan application, when the applicant's true eligibility and document authenticity are hidden.

## 2. Problem Statement

> The agent observes a loan application and its supporting documents. It must select Accept, Request Evidence, or Send to Human because the applicant's true eligibility and document authenticity are not known.

## 3. Technical Terms

| Term | My definition |
|---|---|
| Loan underwriting | Evaluating whether a loan application meets lending criteria. |
| Document AI | AI that reads and interprets documents (text, layout, tables). |
| Intelligent Document Processing (IDP) | Extracting and validating structured information from documents. |
| Document verification | Checking whether submitted documents are consistent and complete. |
| Uncertainty quantification (UQ) | Measuring how uncertain a system is about its own conclusion. |
| Selective classification | A classifier that can choose "I don't know" instead of forcing a decision. |
| Abstention / model abstention | The model declines to decide when evidence is insufficient. |
| Human-in-the-loop (HITL) | A human handles cases the automated system cannot safely resolve. |
| Evidence aggregation | Combining evidence from multiple documents. |
| Conflicting evidence | Two documents or fields disagree. |
| Missing evidence | A required document or piece of information is absent. |
| Decision policy | The rule that selects Accept / Request Evidence / Send to Human. |
| Calibration | Whether predicted probabilities match observed frequencies. |
| Auditability | Being able to reconstruct why the agent made a decision. |
| Out-of-distribution (OOD) detection | Detecting inputs unlike what the system was designed for. |

## 4. Useful Search Queries

I will use these to find papers and discussions.

1. `selective classification abstention survey`
2. `uncertainty quantification decision making incomplete information`
3. `human-in-the-loop loan underwriting AI`
4. `document AI bank statements payslips fraud detection`
5. `calibration confidence machine learning`
6. `cost-sensitive decision threshold asymmetric costs`
7. `agentic AI loan underwriting`
8. `evidential reasoning lending decisions`

## 5. Verified Reddit Communities

All communities below were checked manually: I opened each one, confirmed it exists, is active, and allows questions. Where I hit a karma restriction, I noted it.

| # | Subreddit | Relevant because | Active? | I can post? | Status |
|---|---|---|---|---|---|
| 1 | r/Underwriting | Underwriters discuss daily practice | ✅ | ✅ | **Posted** |
| 2 | r/LoanProcessing | Loan processors discuss real workflows | ✅ | ✅ | **Posted** |
| 3 | r/loanoriginators | Originators discuss application bottlenecks | ✅ | ✅ | **Posted** |
| 4 | r/asktheunderwriter | Borrowers/LOs ask underwriters questions | ✅ | ✅ | **Posted** |
| 5 | r/Mortgages | Mortgage discussions, document workflows | ✅ | ✅ | **Posted** |
| 6 | r/MachineLearning | ML foundations, uncertainty, evaluation | ✅ | ❌ (karma) | Follow only |
| 7 | r/learnmachinelearning | Beginner-friendly ML | ✅ | ❌ (karma) | Follow only |
| 8 | r/computervision | OCR, document layout analysis | ✅ | ❌ (karma) | Follow only |
| 9 | r/fintech | Lending AI, fraud detection | ✅ | ❌ (karma) | Follow only |
| 10 | r/datascience | Credit risk, production ML | ✅ | ❌ (karma) | Follow only |
| 11 | r/MLQuestions | Uncertainty and ML theory | ✅ | ❌ (karma) | Follow only |
| 12 | r/AI_Agents | Agent architecture, HITL workflows | ✅ | ❌ (karma) | Follow only |

**Dropped:** r/LocalLLaMA (active but not directly about loans — low relevance for this project).

**Karma plan:** Building karma on r/NewToReddit and r/NoStupidQuestions so I can unlock the restricted subs later.

## 6. Relevant X Accounts

**Decision:** X participation is **deferred** and recorded as a limitation in the preprint. The course requires 15–25 accounts and 3–4 comments/day over 7 days. This was not completed in this version. Reddit is the primary human-feedback channel.

ChatGPT suggested only 3 accounts. These are noted here for future use:

| # | Handle | Who they are | Why relevant |
|---|---|---|---|
| 1 | @swatisachan01 | Researcher, AI in financial services | Studies human-AI collaboration in underwriting |
| 2 | @chrmanning | Stanford NLP | Document-language foundations |
| 3 | @seb_ruder | NLP researcher | Modern language-model systems |

I did not independently verify these three, so I am not claiming they are a complete or validated list.

## 7. Useful Papers / Articles / Repos / Datasets

All items below were checked: I opened each link and read at least the abstract.

### Papers

| # | Title | Authors | Year | Venue | Link | Why relevant |
|---|---|---|---|---|---|---|
| 1 | Human-AI collaboration to mitigate decision noise in financial underwriting | Sachan, Almaghrabi, Yang, Xu | 2024 | Int. Review of Financial Analysis | https://www.sciencedirect.com/science/article/abs/pii/S1057521924000814 | Core paper: evidence aggregation, conflicting evidence, human-AI collaboration in lending |
| 2 | Agentic AI and Retrieval-Augmented Models in Straight-Through Underwriting | Richardson, Meyers, Hartman, Sandberg | 2026 | Semantic Scholar | https://www.semanticscholar.org/reader/f5beedb5ce7dd78490737a74ce505d48e9691466 | Compares LLM, RAG, agentic-RAG for underwriting; reports gains on missing-information cases |
| 3 | Selective automation for responsible digital lending using a calibrated and explainable AI triage framework | Nguyen Thanh Quang | 2026 | Discover AI (Springer, open access) | https://link.springer.com/article/10.1007/s44163-026-01793-0 | Directly implements Accept / Reject / Manual Review triage. Uses SBA loan data. |
| 4 | Survey on Leveraging Uncertainty Estimation Towards Trustworthy Deep Neural Networks | Hasan et al. | 2023 | arXiv | https://arxiv.org/abs/2304.04906 | Survey of abstention and selective classification |

### Datasets

| # | Name | Source | What it gives | I downloaded? |
|---|---|---|---|---|
| 1 | SBA 7(a) & 504 Loan Data | https://data.sba.gov/dataset/7-a-504-foia | Real loan records with outcomes | ✅ Yes |
| 2 | IDNet-2025 | https://huggingface.co/datasets/cactuslab/IDNet-2025 | Identity document fraud detection | ⬜ (huge file — deferred) |
| 3 | SIDERE Payslips | Contact authors via HAL | Forged salary slips for forgery detection | ⬜ (deferred) |

## 8. Questions I Want to Answer

**About hidden states:**
- Is the hidden state binary (eligible / not eligible), or should it include an UNKNOWN state?
- Can an applicant be eligible while one document is fraudulent?

**About evidence:**
- When is evidence "sufficient" for an automated decision?
- How should the agent treat a low OCR-confidence extraction vs. a mismatch between documents?

**About actions:**
- When should the agent Request Evidence (and which document)?
- When should it escalate to a human rather than ask the applicant?

**About errors:**
- Which error costs more in practice: false accept, false escalation, or false request?
- How do real underwriters weight these costs?

## 9. AI Prompts Used

### Prompt 1 — Initial research (Section 4 prompt)

**Tool:** ChatGPT
**Prompt sent:**

> I am a beginner. I want to design an AI agent for this problem: 
> "Loan document agent: The agent observes a loan application and its supporting documents. It must select Accept, Request Evidence, or Send to Human because the applicant's true eligibility and document authenticity are not known."
>
> The agent must make decisions when information is not complete.
>
> Help me prepare my research.
>
> 1. Give me the technical terms for this problem.
> 2. Give me useful search queries.
> 3. Find 5 to 10 relevant Reddit communities.
> 4. Tell me why each community is relevant.
> 5. Find relevant researchers and engineers on X.
> 6. Give me questions about hidden states, evidence, actions, and errors.
> 7. Identify each claim that needs a source or a test.
> 8. Tell me which parts of my problem are not clear.
>
> Do not present uncertain information as fact.

**What ChatGPT returned:**
- Technical terms, search queries, and conceptual questions (useful — kept)
- 8 Reddit communities, 3 X accounts, and a few paper references without links
- Some unverifiable claims (e.g., a "GPT-5.6" model, a 2026 paper with no URL)

**What I did with the answer:**
- Kept technical terms, search queries, and questions about hidden states/evidence/actions/errors
- Did NOT trust the Reddit and X recommendations — verified manually
- Did NOT trust the paper references without links — searched for them independently

### Verification — performed with DeepSeek

**Tool:** DeepSeek (chat-based assistant)

The initial ChatGPT answer was **unverified**. To follow the course rule ("Do not use a reference before you read it"), I used DeepSeek to verify it.

**How the DeepSeek conversation actually went:** I described my project, pasted ChatGPT's output, and asked DeepSeek to help me verify it. The topics below summarize the back-and-forth. They are not literal quotes.

**Topics covered with DeepSeek:**
- Verifying whether the Reddit communities ChatGPT suggested actually exist, are active, and allow questions
- Confirming whether the papers ChatGPT mentioned exist and finding working links
- Finding datasets for loan documents and document fraud
- Drafting Reddit posts tailored to each community's norms and rules
- Identifying which Reddit communities had karma restrictions

**What I did with DeepSeek's answers:**
- Opened every Reddit community myself before posting
- Opened every paper link myself and read each abstract before adding it to Section 7
- Downloaded the SBA dataset to confirm it was accessible
- Rewrote the Reddit post drafts in my own words before publishing

### Honest summary of AI use

- **ChatGPT:** produced the initial research draft.
- **DeepSeek:** verified the draft, found real datasets and papers, corrected errors, and helped draft community posts.
- **Me (the student):** opened every link, read every paper abstract, posted in every community, and rewrote every public comment.

## 10. Important AI Errors Found

Errors are attributed to the AI that produced them.

| # | AI tool | What it said | What was actually true | How I found out |
|---|---|---|---|---|
| 1 | ChatGPT | Listed only 3 X accounts | Course requires 15–25 | Re-read Section 6 |
| 2 | ChatGPT | Referenced "GPT-5.6" | This model does not exist | General knowledge |
| 3 | ChatGPT | Listed r/LocalLLaMA as relevant | Active but not about loans | Opened the subreddit |
| 4 | ChatGPT | Named papers without links | Cannot verify without URLs | Searched each title independently |
| 5 | ChatGPT | Recommended no datasets | Several exist (SBA, IDNet, SIDERE) | Searched HuggingFace + arXiv + papers |
| 6 | ChatGPT | Listed Reddit subs with karma filters as if I could post there (r/fintech, r/MLQuestions, r/MachineLearning) | I could not post in these subs | Attempted to post and got blocked |

## 11. Parts of My Problem Still Unclear

- **Loan type:** personal? mortgage? I will use **personal/consumer loan** for simplicity.
- **Jurisdiction:** India vs. US changes compliance. I will model a **generic/neutral** lending policy for this project.
- **What "eligible" means:** I will use three dummy criteria (income ≥ threshold, employment duration ≥ threshold, DTI ≤ threshold) in the simulation.
- **What "authentic" means:** Deferred to Week 2 — the Week 1 agent focuses on **eligibility** only.
- **Who the human is:** Assume a **loan officer / underwriter** for this version.
- **Can the agent ask multiple times?** Yes — it can REQUEST_EVIDENCE, receive new evidence, and re-decide.
- **What happens after human review?** The human's decision is treated as ground truth feedback for evaluation.