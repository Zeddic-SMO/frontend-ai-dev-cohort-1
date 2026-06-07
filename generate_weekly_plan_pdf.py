#!/usr/bin/env python3
"""
ICTZoid — HTML/CSS/JS 4-Week Plan PDF Generator
Reads html-css-js-4-week-plan.md → styled HTML → PDF via Chrome headless
"""
import subprocess, sys, re
from pathlib import Path
import markdown

ROOT    = Path(__file__).parent
SRC_MD  = ROOT / "html-css-js-4-week-plan.md"
HTML_OUT = ROOT / "html-css-js-4-week-plan.html"
PDF_OUT  = ROOT / "html-css-js-4-week-plan.pdf"

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ── Accent palette ─────────────────────────────────────────────────────────────
WEEK_COLORS = {
    "Week 1": "#0EA5E9",   # sky blue
    "Week 2": "#F59E0B",   # amber
    "Week 3": "#8B5CF6",   # violet
    "Week 4": "#22C55E",   # green
}
PRIMARY = "#1A56A0"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500&display=swap');

/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:        #FFFFFF;
  --surface:   #F8FAFC;
  --surface2:  #F1F5F9;
  --border:    #E2E8F0;
  --text:      #0F172A;
  --muted:     #64748B;
  --primary:   #1A56A0;
  --code-bg:   #0F172A;
  --code-text: #E2E8F0;
  --font-sans: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
  --font-mono: 'Fira Code', 'Cascadia Code', 'Consolas', monospace;
}

html { font-size: 16px; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

body {
  font-family: var(--font-sans);
  font-size: 1rem;
  line-height: 1.75;
  color: var(--text);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
}

/* ── Page wrap ── */
.page-wrap { max-width: 900px; margin: 0 auto; padding: 0 3rem 5rem; }

/* ── Cover ── */
.cover {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  text-align: center;
  padding: 5rem 3rem;
  background: #08081A;
  color: #F8FAFC;
  page-break-after: always;
}
.cover-bar {
  width: 5px; height: 72px;
  background: #0EA5E9;
  border-radius: 3px;
  margin: 0 auto 2rem;
}
.cover-eyebrow {
  font-size: 0.7rem; font-weight: 700;
  letter-spacing: 0.25em; text-transform: uppercase;
  color: #64748B; margin-bottom: 1rem;
}
.cover-title {
  font-size: clamp(2.2rem, 6vw, 3.75rem);
  font-weight: 900; line-height: 1.1;
  color: #FFFFFF; margin-bottom: 1rem;
}
.cover-subtitle {
  font-size: 1.05rem; color: #94A3B8;
  max-width: 520px; margin: 0 auto 2.5rem;
}
.cover-pills {
  display: flex; flex-wrap: wrap; justify-content: center;
  gap: 0.5rem; margin-bottom: 3rem;
}
.pill {
  font-size: 0.75rem; font-weight: 600;
  padding: 0.3rem 0.8rem; border-radius: 100px;
  border: 1px solid rgba(14,165,233,0.4);
  color: #0EA5E9; background: rgba(14,165,233,0.07);
}
.cover-meta {
  font-size: 0.8rem; color: #475569; margin-top: 1rem;
}
.cover-author {
  font-size: 1.15rem; font-weight: 700;
  color: #F1F5F9; margin-top: 0.25rem;
}

/* ── Overview table ── */
.overview-section {
  padding: 4rem 0 2rem;
  page-break-after: always;
}

/* ── Week sections ── */
.week-section {
  padding: 4rem 0 2rem;
  page-break-before: always;
}
.week-number {
  font-size: 0.7rem; font-weight: 700;
  letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--muted); margin-bottom: 0.4rem;
}
.week-badge {
  display: inline-block;
  font-size: 2.75rem; font-weight: 900;
  line-height: 1; margin-bottom: 0.25rem;
}
.week-title {
  font-size: 1.9rem; font-weight: 800;
  color: var(--text); margin-bottom: 0.5rem;
}
.week-theme {
  font-size: 1rem; color: var(--muted);
  font-style: italic; margin-bottom: 2rem;
}
.week-divider {
  border: none; border-top: 2px solid var(--border);
  margin: 0 0 2rem;
}

/* ── Subject blocks ── */
.subject-block {
  margin-bottom: 2rem;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid var(--border);
}
.subject-header {
  display: flex; align-items: center; gap: 0.6rem;
  padding: 0.7rem 1.1rem;
  font-size: 0.75rem; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: white;
}
.subject-dot {
  width: 8px; height: 8px;
  border-radius: 50%; background: rgba(255,255,255,0.6);
}
.subject-body { padding: 1rem 1.25rem; background: var(--bg); }

/* ── General content typography ── */
h1 {
  font-size: 2.25rem; font-weight: 900;
  color: var(--text); margin-bottom: 1rem;
}
h2 {
  font-size: 1.5rem; font-weight: 800;
  color: var(--text); margin: 2.5rem 0 0.75rem;
  padding-top: 0.5rem; border-top: 2px solid var(--border);
}
h3 {
  font-size: 1.1rem; font-weight: 700;
  color: var(--text); margin: 1.5rem 0 0.5rem;
}
h4 {
  font-size: 0.875rem; font-weight: 700;
  color: var(--muted); text-transform: uppercase;
  letter-spacing: 0.06em; margin: 1.25rem 0 0.4rem;
}
p { margin-bottom: 0.875rem; max-width: 72ch; }
ul, ol { margin: 0.5rem 0 0.875rem 1.75rem; }
li { margin-bottom: 0.25rem; }
li > ul, li > ol { margin-top: 0.25rem; }
strong { font-weight: 700; }
em { font-style: italic; }
a { color: var(--primary); text-decoration: underline; text-underline-offset: 2px; }
blockquote {
  border-left: 4px solid #0EA5E9;
  background: #EFF6FF;
  padding: 0.875rem 1.1rem;
  margin: 1.25rem 0;
  border-radius: 0 6px 6px 0;
  color: #1E40AF; font-style: italic;
}
blockquote > p { margin-bottom: 0; max-width: 100%; color: inherit; }
hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }

/* ── Tables ── */
table {
  width: 100%; border-collapse: collapse;
  font-size: 0.875rem; margin: 1.25rem 0;
  overflow-x: auto; display: block;
}
th {
  background: var(--surface2); font-weight: 700;
  text-align: left; padding: 0.55rem 0.8rem;
  border: 1px solid var(--border);
}
td { padding: 0.45rem 0.8rem; border: 1px solid var(--border); vertical-align: top; }
tr:nth-child(even) td { background: var(--surface); }

/* ── Code ── */
code {
  font-family: var(--font-mono);
  font-size: 0.84em;
  background: var(--surface2);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  border: 1px solid var(--border);
}
pre {
  background: var(--code-bg); color: var(--code-text);
  font-family: var(--font-mono); font-size: 0.83rem;
  line-height: 1.6; padding: 1.25rem 1.5rem;
  border-radius: 8px; overflow-x: auto;
  margin: 1rem 0 1.5rem;
  border: 1px solid #1E293B;
}
pre code { background: none; color: inherit; padding: 0; border: none; font-size: inherit; }

/* ── Checklist wrapper ── */
.checklist-section { page-break-before: always; padding: 4rem 0 2rem; }
.checklist-group { margin-bottom: 2rem; }
.checklist-group-title {
  font-size: 1rem; font-weight: 700; color: var(--text);
  padding: 0.5rem 0.875rem;
  border-left: 4px solid var(--primary);
  background: var(--surface); margin-bottom: 0.75rem;
}
.check-item {
  display: flex; align-items: flex-start; gap: 0.6rem;
  padding: 0.3rem 0.875rem; font-size: 0.9rem;
  border-bottom: 1px solid var(--border);
}
.check-item:last-child { border-bottom: none; }
.check-box {
  width: 16px; height: 16px; min-width: 16px;
  border: 2px solid #CBD5E1; border-radius: 4px;
  margin-top: 0.2rem;
}

/* ── Print ── */
@media print {
  body { font-size: 10.5pt; }
  .week-section { page-break-before: always; }
  pre { white-space: pre-wrap; word-break: break-all; }
  a { color: inherit; text-decoration: none; }
}
"""

def md_to_html(text: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )
    return md.convert(text)

def build_cover() -> str:
    pills = ["HTML", "CSS", "JavaScript", "4 Weeks", "Pre-React", "Hands-on Builds"]
    pill_html = "".join(f'<span class="pill">{p}</span>' for p in pills)
    return f"""
<div class="cover">
  <div class="cover-bar"></div>
  <p class="cover-eyebrow">ICTZoid Web Development Program</p>
  <h1 class="cover-title">HTML, CSS & JavaScript<br>4-Week Plan</h1>
  <p class="cover-subtitle">
    A simultaneous learning curriculum covering all three web fundamentals
    before the React sessions begin — built around weekly integration projects.
  </p>
  <div class="cover-pills">{pill_html}</div>
  <p class="cover-meta">Written by</p>
  <p class="cover-author">Samuel M. Ortil</p>
  <p class="cover-meta" style="margin-top:2rem">ICTZoid &nbsp;·&nbsp; 2026</p>
</div>
"""

# Colour map: subject label → bg colour
SUBJECT_COLORS = {
    "html":       "#E85D3A",  # orange-red
    "css":        "#1A56A0",  # blue
    "javascript": "#D97706",  # amber
    "js":         "#D97706",
    "weekly build": "#16A34A",  # green
}

def subject_color(label: str) -> str:
    key = label.lower().strip()
    for k, v in SUBJECT_COLORS.items():
        if k in key:
            return v
    return "#6B7280"

def build_week_section(week_num: int, week_md: str, accent: str) -> str:
    """Render one week's markdown into a styled section."""
    # Extract the week title line (## Week N — Theme)
    lines = week_md.strip().splitlines()
    title_line = lines[0].lstrip("#").strip()  # e.g. "Week 1 — Foundations"
    theme_match = re.search(r"\*\*Theme:\*\*\s*(.+)", week_md)
    theme = theme_match.group(1).strip() if theme_match else ""

    # Remove the first heading and theme line for body processing
    body_md = "\n".join(lines[1:])
    body_md = re.sub(r"\*\*Theme:\*\*.*\n?", "", body_md)

    # Split by ### Subject headers into blocks
    subject_pattern = re.compile(r"^### (.+)$", re.MULTILINE)
    parts = subject_pattern.split(body_md)

    # parts alternates: [preamble, subject1, content1, subject2, content2, ...]
    subject_blocks_html = ""
    preamble = parts[0].strip()
    if preamble:
        subject_blocks_html += md_to_html(preamble)

    for i in range(1, len(parts), 2):
        subj_label = parts[i].strip()
        subj_content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        color = subject_color(subj_label)
        content_html = md_to_html(subj_content)
        subject_blocks_html += f"""
<div class="subject-block">
  <div class="subject-header" style="background:{color}">
    <div class="subject-dot"></div>
    {subj_label}
  </div>
  <div class="subject-body">{content_html}</div>
</div>
"""

    return f"""
<section class="week-section page-wrap">
  <p class="week-number">Week {week_num}</p>
  <p class="week-badge" style="color:{accent}">{week_num:02d}</p>
  <h2 class="week-title" style="border:none;margin-top:0;padding-top:0">{title_line}</h2>
  <p class="week-theme">{theme}</p>
  <hr class="week-divider">
  {subject_blocks_html}
</section>
"""

def build_checklist_section(md_text: str) -> str:
    """Extract and render the Pre-React Readiness Checklist."""
    # Find the checklist section
    match = re.search(r"## Pre-React Readiness Checklist(.+?)(?=\n---|\Z)", md_text, re.DOTALL)
    if not match:
        return ""

    checklist_md = match.group(1).strip()
    lines = checklist_md.splitlines()

    groups_html = ""
    current_group = ""
    current_items: list[str] = []

    def flush_group():
        nonlocal current_group, current_items
        if not current_items:
            return ""
        items_html = "".join(
            f'<div class="check-item"><div class="check-box"></div><span>{item}</span></div>'
            for item in current_items
        )
        result = f"""
<div class="checklist-group">
  <div class="checklist-group-title">{current_group}</div>
  {items_html}
</div>
"""
        current_group = ""
        current_items = []
        return result

    for line in lines:
        # Bold heading like **HTML**
        heading_match = re.match(r"^\*\*(.+?)\*\*\s*$", line.strip())
        if heading_match:
            groups_html += flush_group()
            current_group = heading_match.group(1)
        # Checklist item: - [ ] ...
        elif re.match(r"^- \[.?\]", line.strip()):
            item_text = re.sub(r"^- \[.?\]\s*", "", line.strip())
            current_items.append(item_text)

    groups_html += flush_group()

    return f"""
<section class="checklist-section page-wrap">
  <h2>Pre-React Readiness Checklist</h2>
  <p style="color:var(--muted);margin-bottom:2rem">
    Confirm every box before Week 5's React sessions begin.
  </p>
  {groups_html}
</section>
"""

def build_overview_section(md_text: str) -> str:
    """Extract the intro block (before Week 1) and render as an overview page."""
    # Everything before the first ## Week heading
    match = re.search(r"^## Week 1", md_text, re.MULTILINE)
    if not match:
        return ""
    overview_md = md_text[:match.start()].strip()
    # Strip the top-level h1 (already in cover)
    overview_md = re.sub(r"^#\s+.+\n", "", overview_md, count=1).strip()
    return f"""
<section class="overview-section page-wrap">
  {md_to_html(overview_md)}
</section>
"""

def build_weekly_rhythm_section(md_text: str) -> str:
    """Extract the Weekly Rhythm section."""
    match = re.search(r"## Weekly Rhythm(.+?)(?=\n## |\Z)", md_text, re.DOTALL)
    if not match:
        return ""
    rhythm_md = match.group(0).strip()
    return f'<section class="page-wrap" style="padding-top:3rem">{md_to_html(rhythm_md)}</section>'

def build_html_doc(md_text: str) -> str:
    cover   = build_cover()
    overview = build_overview_section(md_text)

    # Extract each week block
    week_sections_html = ""
    week_pattern = re.compile(
        r"^## (Week \d+.*?)$(.+?)(?=^## Week \d+|^## Weekly Rhythm|^## Pre-React|\Z)",
        re.MULTILINE | re.DOTALL
    )
    for i, m in enumerate(week_pattern.finditer(md_text), start=1):
        week_heading = m.group(1).strip()
        week_body = m.group(2).strip()
        full_md = f"## {week_heading}\n{week_body}"
        accent = list(WEEK_COLORS.values())[i - 1] if i <= 4 else "#6B7280"
        week_sections_html += build_week_section(i, full_md, accent)

    rhythm = build_weekly_rhythm_section(md_text)
    checklist = build_checklist_section(md_text)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>HTML, CSS & JS — 4-Week Plan — ICTZoid</title>
  <style>{CSS}</style>
</head>
<body>

{cover}
{overview}
{week_sections_html}
{rhythm}
{checklist}

<div style="height:5rem"></div>
</body>
</html>
"""

def generate_pdf(html_path: Path, pdf_path: Path) -> None:
    print(f"Rendering PDF via Chrome headless…")
    result = subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            f"--print-to-pdf={pdf_path.resolve()}",
            "--print-to-pdf-no-header",
            "--no-pdf-header-footer",
            "--virtual-time-budget=5000",
            html_path.resolve().as_uri(),
        ],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode != 0 and not pdf_path.exists():
        print("Chrome stderr:", result.stderr[:800])
        sys.exit(1)

if __name__ == "__main__":
    if not SRC_MD.exists():
        print(f"Source not found: {SRC_MD}")
        sys.exit(1)

    print(f"Reading {SRC_MD.name}…")
    md_text = SRC_MD.read_text(encoding="utf-8")

    print("Building HTML…")
    html = build_html_doc(md_text)
    HTML_OUT.write_text(html, encoding="utf-8")
    print(f"HTML → {HTML_OUT}  ({HTML_OUT.stat().st_size // 1024} KB)")

    generate_pdf(HTML_OUT, PDF_OUT)

    if PDF_OUT.exists():
        size_kb = PDF_OUT.stat().st_size // 1024
        print(f"PDF  → {PDF_OUT}  ({size_kb} KB)")
    else:
        print("PDF generation may have failed — check the HTML output manually.")
