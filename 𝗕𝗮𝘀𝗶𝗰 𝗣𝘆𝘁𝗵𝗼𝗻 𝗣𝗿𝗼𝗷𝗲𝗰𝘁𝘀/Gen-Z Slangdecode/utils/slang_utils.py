"""
Core logic for SlangDecode.

Keeps the original project's idea intact: a CSV of Gen-Z acronyms ->
full-form expansions, loaded into a dictionary, looked up by user input.

This module only adds: safe file loading, input normalization, and
graceful handling of missing/invalid data -- no new "smart" logic is
introduced beyond a simple, transparent nearest-match suggestion
(plain string comparison, not any kind of model).
"""

from __future__ import annotations

import difflib
import logging
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

logger = logging.getLogger("slangdecode")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "slang_dataset.csv"

REQUIRED_COLUMNS = {"acronym", "expansion"}


class SlangDataError(Exception):
    """Raised when the slang dataset can't be loaded or is invalid."""


@dataclass
class SlangResult:
    query: str
    found: bool
    expansion: str | None = None
    suggestions: list[str] | None = None


def load_slang_dict(csv_path: Path = DATA_PATH) -> dict[str, str]:
    """
    Load the acronym -> expansion dataset into a dictionary.

    Raises SlangDataError with a clear, user-safe message on any
    problem. Full technical detail is logged, not shown to the user.
    """
    if not csv_path.exists():
        logger.error("Dataset file not found at %s", csv_path)
        raise SlangDataError(
            "The slang dataset file is missing. Please make sure "
            f"'{csv_path.name}' exists inside the 'data' folder."
        )

    try:
        df = pd.read_csv(csv_path)
    except pd.errors.EmptyDataError as exc:
        logger.error("Dataset file is empty: %s", exc)
        raise SlangDataError("The slang dataset file is empty.") from exc
    except pd.errors.ParserError as exc:
        logger.error("Dataset file could not be parsed: %s", exc)
        raise SlangDataError(
            "The slang dataset file appears to be corrupted or "
            "incorrectly formatted."
        ) from exc
    except (OSError, UnicodeDecodeError) as exc:
        logger.error("Dataset file could not be read: %s", exc)
        raise SlangDataError("The slang dataset file could not be read.") from exc

    if not REQUIRED_COLUMNS.issubset(df.columns):
        missing = REQUIRED_COLUMNS - set(df.columns)
        logger.error("Dataset missing required columns: %s", missing)
        raise SlangDataError(
            f"The dataset is missing required column(s): {', '.join(missing)}."
        )

    # Drop rows with missing acronym/expansion rather than crashing later.
    before = len(df)
    df = df.dropna(subset=["acronym", "expansion"])
    dropped = before - len(df)
    if dropped:
        logger.warning("Dropped %d row(s) with missing values", dropped)

    if df.empty:
        raise SlangDataError("The dataset contains no usable entries.")

    # Normalize keys (lowercase, stripped) so lookups are forgiving.
    df["acronym"] = df["acronym"].astype(str).str.strip().str.lower()
    df["expansion"] = df["expansion"].astype(str).str.strip()
    df = df.drop_duplicates(subset="acronym", keep="first")

    return dict(zip(df["acronym"], df["expansion"]))


def lookup_slang(
    term: str,
    slang_dict: dict[str, str],
    max_suggestions: int = 3,
) -> SlangResult:
    """
    Safely look up a term in the slang dictionary.

    Never raises KeyError. If the term isn't found, returns close
    string-match suggestions (difflib) so the UI can say
    "did you mean...".
    """
    normalized = (term or "").strip().lower()

    if not normalized:
        return SlangResult(query=term, found=False, suggestions=None)

    expansion = slang_dict.get(normalized)
    if expansion is not None:
        return SlangResult(query=normalized, found=True, expansion=expansion)

    close_matches = difflib.get_close_matches(
        normalized, slang_dict.keys(), n=max_suggestions, cutoff=0.6
    )
    return SlangResult(query=normalized, found=False, suggestions=close_matches or None)
