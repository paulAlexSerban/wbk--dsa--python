# Spaced Repetition: from Zero to Expert in Python

## What & Why: Sthe Science
Spaced repetition is a learning techinqique that schedules reviews of material at increasing intervals, exploiting two cognitive phenomena:

- phenomenon: forgetting curve
  - what it means: memory decays exponentially over time
  - implication: review before you forget, not after
- phenomenon: spacing effect
  - what it means: studying speaf across timea beats cramming
  - implication: longer gaps = stringer long-term memory
- phenomenon: testing effect
  - what it means: recalling > re-reading
  - implication: active retrival strngthens the trace

### Why does it matter for software?
A naive scheduler (review everthing dauly) wastes time on things you know well.
SRS directs your effort only where needed - typically cutting study time by 5-10x versus random review.

Use cases:
- language learning - Anki, Duolingo
- medical licensing exams - anki decks for USMLE
- programming knwoledge retention
- customer onboarding / employee trainging tools
- vocabulary in LLM fine-tuning pipelines
- personal knowledge manageemnt (Obsidian + plugins)
- code review flashcards (API signatures, regex pattern, SQL idioms)

## SM-2: The Original Algorithm
SM2- was designed by piots Wozniak in 1987 - it remains the foundation of most SRS tools

Core concepts

| variable | name              | meaning                              |
| -------- | ----------------- | ------------------------------------ |
| `n`      | repetition number | how many times reviewed successfully |
| `EF`     | easiness factor   | how easy the card is (starts at 2.5) |
| `I`      | interval          | days until next review               |
| `q`      | quality           | user's self-rating: 0-5              |

The SM-2 Formulas:

```
# interval formulas
if n == 0: I = 1
if n == 1: I = 6
if n >= 2: I = round(I_prev * EF)

# easiness factor update (after each review):
EF_new = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
EF_new = max(EF_new, 1.3) # floor: 1.3

# if q < 3 (failed recall): reset n to 0, keep EF, restart intervals
```