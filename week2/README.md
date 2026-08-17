# Week 2

## Objective

Extend your Week 1 agent so it reasons about what might be true, chooses which information is worth obtaining, accounts for what that information costs, and decides when it is rational to act.

Same problem as Week 1. Same agent. New question.

## Deliverable

Read **[A Probabilistic and Information-Theoretic View of AI Agents](week2-probabilistic-view-of-ai-agents.pdf)** — the full project brief.

LaTeX source is in [`paper/main.tex`](paper/main.tex). Build with `tectonic main.tex` or `pdflatex main.tex` (run twice).

## There is no deadline

"Week 2" is the name of the deliverable, not a due date. If you are full-time, you may finish in a week. At two hours a day, two to three weeks is normal. Submitting this in Week 5 or Week 6 is completely acceptable.

We do not enforce deadlines. Students who give a deliverable the right amount of time consistently produce better work than students who rush to match a calendar.

## Concepts are prompts, not formulas

The brief does not hand you equations for entropy, information gain, mutual information, cross-entropy, KL divergence, Jensen–Shannon divergence, calibration, or value of information. It gives you the plain-English meaning, a concrete example, and **a prompt to paste into ChatGPT, Claude, or Gemini** to learn each one properly.

That is deliberate. Nine of the thirteen concepts you need were never taught in the sessions. Going and learning them yourself is the assignment.

## Two skills

Both are optional. Both exist because one document cannot give the right next step to a room full of people at different starting points.

| Skill | What it does |
|---|---|
| [`skill/readiness/`](skill/readiness/SKILL.md) | **Run this first.** Interviews you about your problem, what you already have, which concepts you can actually explain, your time, and where you're stuck — then writes a roadmap for your situation. "I don't know" is a useful answer. |
| [`skill/coach/`](skill/coach/SKILL.md) | **Run this while you build.** Walks you through the deliverable stage by stage with a gate check at each one. Explains any concept as many times as you need. |

Install:

```bash
mkdir -p ~/.claude/skills/week2-readiness ~/.claude/skills/week2-coach
cp week2/skill/readiness/SKILL.md ~/.claude/skills/week2-readiness/SKILL.md
cp week2/skill/coach/SKILL.md     ~/.claude/skills/week2-coach/SKILL.md
```

Then run `/week2-readiness`, and later `/week2-coach`.

Not using Claude Code? The skill files are plain text — paste one in as your first message to ChatGPT or Gemini and it works the same way.

Neither will write your project for you. That is deliberate: the course evaluates whether you can reason under uncertainty, and a paper you did not think through is a paper you cannot defend.
