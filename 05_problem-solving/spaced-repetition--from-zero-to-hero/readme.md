# Spaced Repetition: from Zero to Expert in Python

## 1. What & Why: Sthe Science
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