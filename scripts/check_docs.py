#!/usr/bin/env python3
"""Vérifie la structure de base des fichiers de projet Markdown, sans dépendances."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0
for path in sorted((ROOT / "projets").rglob("*.md")):
    checked += 1
    text = path.read_text(encoding="utf-8")
    name = path.relative_to(ROOT)
    if not text.lstrip().startswith("# "):
        errors.append(f"{name}: le document doit commencer par un titre '# '.")
    headings = set(text.splitlines())
    if "## Sujets abordés" in headings:
        required = (
            "## Contexte", "## Date", "## Participants", "## Sujets abordés",
            "## Décisions confirmées", "## Actions", "## Questions ouvertes",
        )
    else:
        required = ("## Objectif", "## Étapes")
    for heading in required:
        if heading not in headings:
            errors.append(f"{name}: la section '{heading}' manque.")
    if "\x00" in text:
        errors.append(f"{name}: caractère NUL interdit.")
print(f"{checked} document(s) de projets vérifié(s).")
for error in errors:
    print("ERREUR:", error)
sys.exit(1 if errors else 0)
