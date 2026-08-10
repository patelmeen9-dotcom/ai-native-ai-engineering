# Week 1 AI-Native Project

## Student project instructions

## 1. Project objective

Select one real problem.

Design an AI agent for this problem.

The agent must make decisions when information is not complete.

Use the same problem for all work in this project.

Use the problem for these tasks:

- Reddit discussions
- X discussions
- The agent design
- The probability model
- The experiment
- The IJCAI-style preprint
- The LinkedIn post
- The X preprint post

Do not select a different problem for each platform.

Use this work cycle:

1. Select a problem.
2. Use AI tools to prepare questions.
3. Ask humans the questions.
4. Design and test an agent.
5. Use the test results to change the design.
6. Write a preprint in LaTeX.
7. Publish the preprint.
8. Ask for more comments.

## 2. Correct use of AI tools

Use ChatGPT, Claude, Codex, Gemini, or Gemini Spark.

You can use other AI tools if they are available.

Use AI tools for these tasks:

- Find technical terms.
- Find relevant online communities.
- Find researchers and engineers.
- Prepare search queries.
- Explain difficult posts and papers.
- Prepare questions.
- Find problems in your design.
- Write and repair code.
- Prepare LaTeX source files.
- Review the preprint.

You are responsible for all project content.

Do not use AI tools to make false conversations.

Do not publish an AI answer that you do not understand.

Do not report a test that you did not do.

Do not use a reference before you read it.

Use your own words in public discussions.

It is acceptable to ask a simple question.

Tell other persons when you are not sure.

## 3. Select the problem

Select one problem from Section 12.

You can select a different problem if the instructor approves it.

Make the problem small and testable.

Write one sentence that describes the problem.

Use this form:

> The agent observes [INPUT]. It must select [ACTION] because [HIDDEN STATE] is not known.

Example:

> The agent reads a supplier bank-change request. It must approve, hold, or reject the request because the sender identity is not known.

## 4. Prepare the AI research file

Create a file with the name `research-file.md`.

Give an AI assistant this information:

- Your experience level
- Your selected problem
- Your project objective
- The type of agent that you want to build
- The information that you do not have

Use this prompt:

```text
I am a beginner. I want to design an AI agent for this problem: [PROBLEM].
The agent must make decisions when information is not complete.

Help me prepare my research.

1. Give me the technical terms for this problem.
2. Give me useful search queries.
3. Find 5 to 10 relevant Reddit communities.
4. Tell me why each community is relevant.
5. Find relevant researchers and engineers on X.
6. Give me questions about hidden states, evidence, actions, and errors.
7. Identify each claim that needs a source or a test.
8. Tell me which parts of my problem are not clear.

Do not present uncertain information as fact.
```

Check each AI recommendation.

Remove a Reddit community if it is inactive or not relevant.

Remove an X account if its content is not relevant.

Record this information in `research-file.md`:

- The problem statement
- The project objective
- Technical terms
- Search queries
- Five to ten verified Reddit communities
- Relevant X accounts
- Five useful papers, articles, repositories, or datasets
- Questions that you want to answer
- AI prompts and important AI errors

## 5. Have discussions on Reddit

Participate in at least five relevant Reddit communities.

You can participate in a maximum of ten communities for this project.

Make at least two contributions in each community.

You must start each contribution.

A contribution can be one of these items:

- A new post
- A top-level comment
- A question in an existing discussion

The minimum quantity is ten contributions in five communities.

The target quantity is 20 contributions in ten communities.

Read the community rules before you post.

Do not copy the same text to all communities.

Change the text for the purpose of each community.

Do not publish advertisements in a community that does not permit them.

Continue the discussion when a person answers you.

Complete at least five discussions that have two or more replies.

You can ask these types of questions:

- Which hidden state did I not include?
- Which incorrect decision has the highest cost?
- When must the agent ask a human for help?
- Which part of this test is not realistic?
- Which historical cases are comparable?
- Which evidence will change your decision?
- What failed when you used a similar system?

After a discussion, use an AI assistant for these tasks:

1. Make a short summary of the discussion.
2. Identify each point of disagreement.
3. Identify a new testable assumption.
4. Identify a change for the agent.
5. Identify information that you must verify.

Check the AI summary against the original discussion.

## 6. Have discussions on X

Ask ChatGPT or Gemini to find relevant X accounts.

Give the AI assistant your problem and project objective.

Do not ask only for popular AI accounts.

Select 15 to 25 relevant accounts.

Follow researchers, engineers, users, and critics.

Write three or four useful comments each day.

The target for seven days is 21 to 28 comments.

Start at least three discussions that have two or more replies.

Each comment must be related to your selected problem.

Use these rules for each comment:

- Refer to a specific item in the original post.
- State what you understand.
- State what you do not understand.
- Give one result from your work when it is relevant.
- Ask one clear question.

Do not write comments such as “Great insight.”

Do not use text that has no technical information.

Be honest about your level of knowledge.

## 7. Keep a discussion record

Create a file with the name `discussion-record.md`.

Use this table:

| Platform | Community or account | Link | My first contribution | Human answer | My next answer | Design change |
|---|---|---|---|---|---|---|

Add each Reddit and X contribution to the table.

For each useful answer, record one of these results:

- A new assumption
- A new failure condition
- A new test
- A change to the agent
- A change to the probability model
- No change, with the reason

A link without an explanation does not complete this task.

## 8. Design and build the agent

The agent must do an action.

A chatbot answer is not sufficient.

Define these parts:

1. **Input:** Information that the agent receives.
2. **Hidden state:** Information that can be true but is not visible.
3. **Belief:** The probability of each hidden state.
4. **Action:** What the agent can do.
5. **Cost:** The result of an incorrect action.
6. **Policy:** The rule that selects an action.
7. **Feedback:** New information after the action.

The agent can do one or more of these actions:

- Act
- Wait
- Ask a question
- Get more evidence
- Send the case to a human
- Refuse the action

Add one useful human reasoning function to the agent.

For example, the agent can do one of these functions:

- Remember a prior error.
- Compare the case with similar cases.
- Ask for more information.
- Identify uncertainty.
- Change a belief after new evidence.
- Send a high-cost decision to a human.

Do not try to copy all functions of a human brain.

Build the smallest version that you can test.

You can use one of these implementations:

- An LLM prompt and `if/else` rules
- A notebook simulation
- A spreadsheet model
- A small software agent

## 9. Test the agent

Prepare 30 to 50 labeled or simulated cases.

Hide the correct label when the agent makes a decision.

Test at least two agent policies.

Save all predictions and actions.

Compare the agent with at least one baseline.

Do not report accuracy as the only measurement.

Use applicable measurements from this list:

- Confusion matrix
- Precision
- Recall
- False-positive quantity
- False-negative quantity
- Human-review rate
- Decision cost
- Calibration

Examine at least five incorrect decisions.

Give a name to each failure condition.

Explain which error has the highest cost.

Explain why this error has the highest cost.

Create a README file.

Give complete instructions to repeat the test.

## 10. Make a probability decision record

Select one case for which the correct state is not known.

Create a probability decision record for the case.

Record these items:

| Item | Required information |
|---|---|
| Evidence | Information that the agent observed |
| Hidden states | Possible explanations |
| Beliefs | Probability of each hidden state |
| Event | Hidden states that are important to the user |
| Actions | Available actions |
| Costs | Results of correct and incorrect actions |
| Policy | Decision rule and threshold |
| Decision | Selected action and reason |
| Audit data | Time, data version, model version, and policy version |

The sum of all hidden-state probabilities must be 100 percent.

Then add one new item of evidence.

Complete these steps:

1. State the prior probability.
2. State the new evidence.
3. Estimate the likelihood for each important hidden state.
4. Calculate or simulate the posterior probability.
5. Compare the posterior probability with the decision threshold.
6. Record the new action.

Use recent and comparable historical cases.

Do not use a large data group only because it is easy to find.

Search for evidence for the safe state and the unsafe state.

## 11. Use AI tools to review the work

Use Gemini Spark for repeated reviews.

You can also use ChatGPT, Claude, Codex, or Antern.

Complete at least three different reviews.

### 11.1 Practitioner review

Ask the AI reviewer to find these problems:

- Assumptions that are not realistic
- Missing users or stakeholders
- Deployment risks
- Actions that can cause harm
- Actions that can cause unnecessary work

### 11.2 Probability review

Ask the AI reviewer to check these items:

- Hidden states
- Prior probabilities
- Likelihood estimates
- Decision thresholds
- Error costs
- Calibration
- Evidence for an alternative explanation

### 11.3 Preprint review

Ask the AI reviewer to check these items:

- Clear problem statement
- New information
- Correct methods
- Test design
- Baseline quality
- Repeatable results
- Limitations
- Ethics
- Claims without evidence
- Questions for the next version

Create a file with the name `review-record.md`.

Use this table:

| AI tool | Review comment | Accept or reject | Reason | Change | Evidence |
|---|---|---|---|---|---|

Do not accept each AI review comment automatically.

Record why you accept or reject each important comment.

## 12. Problem ideas

Select one of these problems.

Make the selected problem more specific before you build the agent.

1. **Phishing email agent:** Deliver, hold, or block an email.
2. **Supplier payment agent:** Approve, verify, or stop a bank-change request.
3. **Calendar agent:** Accept, reject, move, or question a meeting request.
4. **Support agent:** Answer, ask for information, or send a ticket to a human.
5. **Code review agent:** Merge, test, request review, or stop a code change.
6. **CI diagnosis agent:** Select the next test for a software failure.
7. **Cloud cost agent:** Ignore, examine, limit, or report unusual cost.
8. **Incident agent:** Observe, collect logs, undo a change, or report an incident.
9. **Dependency agent:** Install, test, delay, or reject a software update.
10. **Secret detection agent:** Ignore, verify, or remove a possible secret.
11. **Data quality agent:** Accept, repair, isolate, or reject a data batch.
12. **Appointment agent:** Select routine, urgent, or emergency routing without a diagnosis.
13. **Medicine reminder agent:** Remind, wait, or notify a person.
14. **Tutor agent:** Answer, ask a question, give a hint, or teach a prior concept.
15. **Assignment review agent:** Clear, question, or report possible copied work.
16. **Job application agent:** Apply, research, request help, or skip a job.
17. **Interview agent:** Select the next practice question from prior answers.
18. **News verification agent:** Publish, wait, check, or add an uncertainty label.
19. **Claim review agent:** Accept, change, add a source, or remove a content claim.
20. **Moderation agent:** Permit, warn, hide, or report community content.
21. **Transaction agent:** Approve, question, stop, or examine a transaction.
22. **Loan document agent:** Accept, request evidence, or send a case to a human.
23. **Food inventory agent:** Order, discount, donate, or wait.
24. **Energy control agent:** Reduce, delay, or continue equipment operation.
25. **Accessibility agent:** Ask, change the interface, or make no change.

For the selected problem, answer these questions:

- What can the agent observe?
- What information is hidden?
- What will a human observe that the agent cannot observe?
- What must the agent remember?
- When must the agent ask a question?
- Which incorrect action can be corrected?
- Who has the cost of an incorrect action?
- Which evidence changes the belief?
- Is the historical evidence comparable?
- How does the agent learn after an action?

## 13. Write the preprint

Write one course preprint in the IJCAI style.

Use LaTeX.

Use the [current official IJCAI author kit](https://www.ijcai.org/authors_kit).

Do not state that IJCAI accepted the preprint.

Do not state that you submitted the preprint to IJCAI if you did not submit it.

The preprint can be shorter than the IJCAI page limit.

Do not add text only to increase the page quantity.

Use these sections:

1. Title
2. Abstract
3. Introduction
4. Related work and user discussions
5. Agent design
6. Probability model and decision rule
7. Test method
8. Results
9. Failure analysis
10. Limitations, ethics, and human control
11. Conclusion and new questions
12. References

The preprint must include these items:

- One specific problem
- Agent input
- Hidden states
- Beliefs
- Actions
- Error costs
- One baseline
- One test or simulation
- One result table or figure
- Failure examples
- Information from human discussions
- Limitations
- A code or project link when it is safe
- An AI-use statement

Check each citation.

Check each equation.

Check each test result.

Compile the LaTeX source to a PDF file.

You can work in a team.

Team members can share access to AI coding tools.

Add a contribution statement for team work.

The statement must identify these contributions:

- Problem selection
- Public discussions
- Agent design
- Software development
- Tests
- Citation checks
- Preprint sections
- PDF checks

## 14. Publish the work

Publish only one LinkedIn post during this week.

Attach the preprint PDF to the LinkedIn post.

The LinkedIn post must include these items:

- The problem in one sentence
- The reason for the agent design
- The reason for the probability model
- One important result or failure
- One design change from a public discussion
- The largest known limitation
- One specific request for comments

Publish the same preprint PDF on X.

Write a short X thread about the preprint.

Include the problem, test, result, and open question.

You can publish the work in a Reddit community if its rules permit this action.

Give useful information in the Reddit post.

Do not require a person to open the PDF to understand the post.

## 15. Required repository structure

```text
week1/
└── deliverables/
    └── student-project/
        ├── README.md
        ├── research-file.md
        ├── discussion-record.md
        ├── review-record.md
        ├── paper/
        │   ├── main.tex
        │   ├── references.bib
        │   ├── figures/
        │   └── preprint.pdf
        ├── src/
        ├── data/
        ├── experiments/
        ├── results/
        ├── decisions/
        │   └── probability-decision-record.md
        └── social/
            ├── linkedin-post.md
            └── x-thread.md
```

## 16. Completion checklist

- [ ] Use one problem for all project work.
- [ ] Create the AI research file.
- [ ] Verify five to ten Reddit communities.
- [ ] Make two contributions in each Reddit community.
- [ ] Complete five Reddit discussions.
- [ ] Follow 15 to 25 relevant X accounts.
- [ ] Write three or four X comments each day.
- [ ] Complete three X discussions.
- [ ] Build a testable agent or simulation.
- [ ] Prepare 30 to 50 test cases.
- [ ] Compare two agent policies.
- [ ] Compare the agent with one baseline.
- [ ] Examine five incorrect decisions.
- [ ] Create one probability decision record.
- [ ] Complete three AI reviews.
- [ ] Record accepted and rejected AI review comments.
- [ ] Write the preprint in LaTeX.
- [ ] Compile the preprint PDF.
- [ ] Publish one LinkedIn post with the PDF.
- [ ] Publish the PDF and a short thread on X.
- [ ] State AI use, human contributions, and limitations.

The final project must give evidence for this result:

> The student used AI tools and human discussions to make, test, improve, and publish new technical information about one problem.
