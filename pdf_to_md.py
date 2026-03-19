#!/usr/bin/env python3
"""Extract PDF text to markdown with basic cleanup."""
import re
import sys
from pathlib import Path

from pypdf import PdfReader


def clean_line(line: str) -> str:
    """Normalize and clean a single line."""
    line = line.rstrip()
    # Skip page markers like "-- 7 of 791 --"
    if re.match(r'^--\s*\d+\s+of\s+\d+\s+--\s*$', line):
        return ""
    # Skip single-character or two-char lines that look like stamp artifacts
    if len(line.strip()) <= 2 and line.strip().isalpha():
        return ""
    return line


def is_section_header(line: str) -> bool:
    """Heuristic: line looks like a section number header (e.g. 01 12 00, Section 01 12 00)."""
    return bool(
        re.match(r'^(Section\s+)?\d{2}\s+\d{2}\s+(\d{2}\s+)?[\d.]+\s*[GE]?\s*[–\-]', line)
        or re.match(r'^DIVISION\s+\d{2}\s+', line, re.I)
        or re.match(r'^TABLE OF CONTENTS', line, re.I)
        or re.match(r'^CONTRACT CAT-452', line, re.I)
    )


def main() -> None:
    pdf_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf_path.with_suffix(".md")

    reader = PdfReader(str(pdf_path))
    lines_out = []
    lines_out.append(f"# {pdf_path.stem}\n")
    lines_out.append("")  # blank after title

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue
        page_lines = text.splitlines()
        for raw in page_lines:
            line = clean_line(raw)
            if not line:
                continue
            # Optional: add markdown heading for section-like lines
            if is_section_header(line) and not line.startswith("#"):
                # Use ## for Division, ### for Section
                if line.upper().startswith("DIVISION"):
                    lines_out.append(f"\n## {line}\n")
                elif re.match(r'^(Section\s+)?\d{2}\s+\d{2}', line):
                    lines_out.append(f"\n### {line}\n")
                else:
                    lines_out.append(line)
            else:
                # Bullet normalization: use * for bullets (per user rule)
                if line.strip().startswith("•"):
                    line = line.replace("•", "*", 1)
                lines_out.append(line)
        # Optional: add page break comment every N pages for navigation
        if (i + 1) % 100 == 0:
            lines_out.append(f"\n<!-- Page {i + 1} -->\n")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines_out), encoding="utf-8")
    print(f"Wrote {len(lines_out)} lines to {out_path}")


if __name__ == "__main__":
    main()
