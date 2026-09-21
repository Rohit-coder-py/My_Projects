# SlangDecode 🔤

**Instantly decode Gen-Z slang & acronyms.**

A small, reliable Streamlit app that looks up the full meaning of Gen-Z
slang terms and acronyms (e.g. `iykyk`, `fr fr`, `nglqm`) from a curated
dataset of 3,000+ acronym → expansion pairs.

## Overview

This started as a simple script:

```python
df_dict = dict(zip(df['acronym'], df['expansion']))
print(df_dict[input(...)])
```

That core idea — a clean dictionary lookup — is exactly right for this
problem, so it's preserved as-is. What's been added is everything needed
to turn it into a reliable, shareable app: a Streamlit UI, input
validation, error handling, "did you mean...?" suggestions, and a
browsable view of the full dataset.

**This is not a trained machine-learning model.** Mapping a known
acronym to a fixed meaning is a direct lookup problem, and a dictionary
is the transparent, correct tool for it — see "Why not a neural
network?" in the app's "About" section for the reasoning.

## How it works

```
User input (slang term)
        ↓
Normalize (trim, lowercase)
        ↓
Dictionary lookup (data/slang_dataset.csv → dict)
        ↓
   Found?  ── yes → show expansion
      │
      no → suggest closest matches (difflib) or ask user to check spelling
```

## Dataset

- `data/slang_dataset.csv` — two columns: `acronym`, `expansion`
- ~3,350 rows, no missing values, no duplicate acronyms after cleaning
- See `graphs/` for exploratory plots (acronym length distribution,
  expansion length distribution, top-15 longest expansions, dataset size)

## Project structure

```
slangdecode/
├── app.py                  # Streamlit entry point
├── generate_graphs.py      # Regenerates the EDA graphs in graphs/
├── requirements.txt
├── README.md
├── data/
│   └── slang_dataset.csv
├── graphs/                 # Saved dataset-exploration plots
├── assets/
│   ├── logo.png
│   └── make_logo.py        # Regenerates the logo if you want to tweak it
└── utils/
    └── slang_utils.py       # Data loading + lookup logic, with error handling
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints (usually `http://localhost:8501`).

To regenerate the dataset graphs after changing the CSV:

```bash
python generate_graphs.py
```

## Error handling

- **Missing/corrupted dataset file** → friendly error, app stops cleanly
  instead of crashing (`SlangDataError` in `utils/slang_utils.py`)
- **Missing required CSV columns** → clear message naming the missing column(s)
- **Empty input** → warning asking the user to type something
- **Unknown term** → clear "not found" message + nearest-match suggestions
  instead of a raw `KeyError`
- **Duplicate/blank rows in the dataset** → dropped safely at load time,
  logged, and the app continues to run

## Limitations

- Exact-term lookup only (plus simple string-distance suggestions) —
  it does not understand slang used in a full sentence or in context
- Coverage is limited to whatever is in `slang_dataset.csv`
- Not a machine-learning model — by design (see above)

## Author

Rohit Jha — [GitHub](https://github.com/Rohit-coder-py) ·
[LinkedIn](https://linkedin.com/in/rohit-jha-ai)
