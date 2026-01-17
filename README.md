# Mini Machine (Person of Interest-inspired)

A small Python project inspired by The Machine from Person of Interest.
It reads a JSON “profile” and scans for keyword-based signals,
and prints a terminal style report with a risk level, counts, and flags.

> Fictional demo project — any personal data used should be fake/test-only.

---

## How It Works
- Profile activity and notes are combined into a single text source.
- Keywords are matched using a whole-word and phrase-based checks
- Matches are made by category.
- A risk level is assigned using a simple rule-based threshold.
- Results are displayed using a typewriter-style terminal output.

---

## Features
- Reads a single profile from JSON
- Keyword-based detection across:
  - suspicious terms
  - emotional terms
  - positive terms
- Outputs a “Machine-like” report:
  - identity fields (name, age, height, weight, etc.)
  - risk level
  - flag list
- Terminal “typewriter” output effect for vibe 

---



## Quick Start

### 1. Install (optional)
This project uses only Python standard library.

### 2. Run
`python3 main.py`

## Things learned 
- I learned how to make the output appear as it is being typed by making a `type_out` function.
- I built a small system by separating logic (`analysis.py`) from the execution (`main.py`).

This started as one of my first solo Python projects and evolved as I learned better structure, organization, and readability.
