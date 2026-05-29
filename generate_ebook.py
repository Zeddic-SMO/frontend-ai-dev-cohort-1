#!/usr/bin/env python3
"""
ICTZoid Web Development Program — Ebook Generator
Produces: ebook.html
Author credit: Samuel M. Ortil
"""
import re, textwrap
from pathlib import Path
import markdown
from markdown.extensions import tables, fenced_code, attr_list, toc

ROOT = Path("/Users/samuel/Documents/Projects/lms/course-format")
OUT  = ROOT / "ebook.html"

# ── Chapter manifest (order = reading order) ─────────────────────────────────
CHAPTERS = [
    # (file, part_label, chapter_num, display_title, accent)
    ("how-the-internet-works.md",       "Part I — Foundations",      1,
     "How the Internet Works",           "#00D4FF"),
    ("software-development-lifecycle.md","Part I — Foundations",      2,
     "Software Development Lifecycle",   "#00D4FF"),
    (None,                               "Part II — Web Fundamentals", 3,
     "HTML",                             "#F59E0B"),
    ("css-web-fundamentals.md",          "Part II — Web Fundamentals", 4,
     "CSS",                              "#F59E0B"),
    ("javascript-web-fundamentals.md",   "Part II — Web Fundamentals", 5,
     "JavaScript",                       "#F59E0B"),
    ("git-github-web-fundamentals.md",   "Part II — Web Fundamentals", 6,
     "Git & GitHub",                     "#F59E0B"),
    ("react.md",                         "Part III — Modern Frontend", 7,
     "React",                            "#8B5CF6"),
    ("frontend-ai-development.md",       "Part IV — AI Development",   8,
     "Frontend AI Development",          "#22C55E"),
]

# HTML course overview extracted from courses.md (no standalone file exists)
HTML_CHAPTER_CONTENT = """
## Course Overview

HTML (HyperText Markup Language) gives every web page its structure and meaning.
Before any styling or interactivity exists, HTML describes *what the content is* — a heading,
a paragraph, a navigation link, a form. This course takes you from writing your first valid
document all the way to building fully accessible, validated HTML that meets professional standards.

---

## Learning Objectives

By the end of this course you will be able to:

- Write a valid HTML5 document from memory
- Use semantic elements to describe page structure with precision
- Build accessible forms that work with keyboard and screen readers
- Mark up lists, tables, figures, and media correctly
- Apply ARIA attributes where HTML semantics are not enough
- Validate your HTML and systematically fix errors

---

## Module Overview

| # | Module | Focus |
|---|--------|-------|
| 1 | Document Structure | DOCTYPE, head, body, meta tags |
| 2 | Semantic HTML | nav, main, article, section, aside, header, footer |
| 3 | Forms and Inputs | input types, labels, fieldsets, validation attributes |
| 4 | Accessibility | ARIA roles, landmarks, alt text, keyboard navigation |

---

## Module 1 — Document Structure

### Lesson 1.1 — Your First HTML Document

Every HTML document follows the same skeleton:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>My First Page</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <h1>Hello, world!</h1>
  <p>This is my first HTML page.</p>
</body>
</html>
```

**Why each line matters:**

| Line | Purpose |
|------|---------|
| `<!DOCTYPE html>` | Tells the browser this is an HTML5 document |
| `<html lang="en">` | Root element; `lang` helps screen readers and search engines |
| `<meta charset="UTF-8">` | Character encoding — supports every language and emoji |
| `<meta name="viewport">` | Prevents mobile browsers from zooming out by default |
| `<title>` | Shown in the browser tab and search results |

---

### Lesson 1.2 — Headings, Text, and Lists

```html
<!-- Headings — h1 is the page title; only one per page -->
<h1>ICTZoid Web Development Program</h1>
<h2>Course Catalogue</h2>
<h3>Module 1 — Foundations</h3>

<!-- Paragraphs and inline text -->
<p>HTML is the <strong>structure</strong> of the web.
   CSS is the <em>style</em>. JavaScript is the behaviour.</p>

<!-- Unordered list -->
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

<!-- Ordered list -->
<ol>
  <li>Plan</li>
  <li>Design</li>
  <li>Develop</li>
  <li>Test</li>
  <li>Deploy</li>
</ol>

<!-- Description list — great for glossaries -->
<dl>
  <dt>DOM</dt>
  <dd>Document Object Model — a tree representation of an HTML document</dd>
  <dt>API</dt>
  <dd>Application Programming Interface — a contract between software components</dd>
</dl>
```

---

## Module 2 — Semantic HTML

### Lesson 2.1 — Landmark Elements

Semantic elements carry meaning beyond just visual presentation. Screen readers and search
engines use them to understand your page's structure.

```html
<body>
  <header>
    <nav aria-label="Main navigation">
      <a href="/">Home</a>
      <a href="/courses">Courses</a>
      <a href="/about">About</a>
    </nav>
  </header>

  <main>
    <article>
      <h1>Course 1 — HTML</h1>
      <section>
        <h2>Module 1 — Document Structure</h2>
        <p>...</p>
      </section>
      <aside>
        <h2>Quick Tip</h2>
        <p>Validate your HTML at validator.w3.org</p>
      </aside>
    </article>
  </main>

  <footer>
    <p>&copy; 2026 ICTZoid. All rights reserved.</p>
  </footer>
</body>
```

**Why semantics matter:**

- Screen readers announce landmarks — users can jump directly to `<main>` or `<nav>`
- Search engines give more weight to content inside `<article>` and `<main>`
- Other developers understand the page structure without reading all the CSS

---

## Module 3 — Forms and Inputs

### Lesson 3.1 — Building Accessible Forms

```html
<form action="/register" method="POST" novalidate>

  <!-- Always associate labels with inputs -->
  <div class="field">
    <label for="name">Full name</label>
    <input id="name" name="name" type="text"
           autocomplete="name" required
           aria-describedby="name-hint name-error" />
    <p id="name-hint" class="hint">As it appears on your ID</p>
    <p id="name-error" class="error" hidden aria-live="polite"></p>
  </div>

  <div class="field">
    <label for="email">Email address</label>
    <input id="email" name="email" type="email"
           autocomplete="email" required />
  </div>

  <div class="field">
    <label for="password">Password</label>
    <input id="password" name="password" type="password"
           autocomplete="new-password"
           minlength="8" required
           aria-describedby="pwd-rules" />
    <p id="pwd-rules" class="hint">Minimum 8 characters, include a number</p>
  </div>

  <!-- Group related checkboxes with fieldset + legend -->
  <fieldset>
    <legend>Courses of interest</legend>
    <label><input type="checkbox" name="interests" value="html" /> HTML</label>
    <label><input type="checkbox" name="interests" value="css"  /> CSS</label>
    <label><input type="checkbox" name="interests" value="js"   /> JavaScript</label>
  </fieldset>

  <button type="submit">Create account</button>

</form>
```

---

## Module 4 — Accessibility

### Lesson 4.1 — ARIA Essentials

ARIA (Accessible Rich Internet Applications) fills gaps where HTML semantics are not enough.

**Rule 1:** Never use ARIA when native HTML can do the job.

```html
<!-- ❌ Unnecessary ARIA -->
<button role="button">Submit</button>

<!-- ✅ Native HTML already has the role -->
<button>Submit</button>

<!-- ✅ ARIA is needed here (custom component) -->
<div role="tablist" aria-label="Course sections">
  <div role="tab" aria-selected="true"  aria-controls="panel-1" id="tab-1" tabindex="0">HTML</div>
  <div role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2" tabindex="-1">CSS</div>
</div>

<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">HTML content...</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>CSS content...</div>
```

**Live regions — announce dynamic content to screen readers:**

```html
<!-- Announce status messages without moving focus -->
<div aria-live="polite" id="status"></div>

<script>
  document.getElementById("status").textContent = "Form saved successfully.";
</script>
```
"""

# ── Markdown → HTML conversion ────────────────────────────────────────────────
MD = markdown.Markdown(
    extensions=["tables", "fenced_code", "attr_list", "nl2br", "sane_lists"],
    extension_configs={},
)

def md_to_html(text: str) -> str:
    MD.reset()
    # Normalize the image paths to be relative to the ebook location
    text = text.replace("![", "![").replace("](images/", "](images/")
    return MD.convert(text)

def strip_h1(text: str) -> str:
    """Remove the first # heading — we render our own chapter header."""
    return re.sub(r"^#\s+.+\n", "", text, count=1)

def load_chapter(filename: str | None, fallback: str = "") -> str:
    if filename is None:
        return md_to_html(fallback)
    path = ROOT / filename
    if not path.exists():
        return f"<p><em>Content file not found: {filename}</em></p>"
    raw  = path.read_text(encoding="utf-8")
    raw  = strip_h1(raw)
    return md_to_html(raw)

# ── TOC generation ────────────────────────────────────────────────────────────
def build_toc() -> str:
    items = []
    cur_part = None
    for fname, part, num, title, accent in CHAPTERS:
        if part != cur_part:
            cur_part = part
            items.append(f'<li class="toc-part">{part}</li>')
        items.append(
            f'<li class="toc-chapter">'
            f'<a href="#ch{num}">'
            f'<span class="toc-num" style="color:{accent}">Chapter {num}</span> '
            f'<span class="toc-title">{title}</span>'
            f'</a></li>'
        )
    return "\n".join(items)

# ── Per-chapter SVG images ────────────────────────────────────────────────────
CHAPTER_IMAGES = {
    1: "images/course-internet.svg",
    2: "images/course-sdlc.svg",
    3: "images/course-html.svg",
    4: "images/course-css.svg",
    5: "images/course-javascript.svg",
    6: "images/course-git.svg",
    7: "images/course-react.svg",
    8: "images/course-ai.svg",
}

def chapter_img_tag(num: int) -> str:
    src = CHAPTER_IMAGES.get(num)
    if src and (ROOT / src).exists():
        return f'<img class="ch-hero" src="{src}" alt="Chapter {num} illustration" />'
    return ""

# ── HTML template ─────────────────────────────────────────────────────────────
CSS = """
/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:          #FFFFFF;
  --surface:     #F8FAFC;
  --surface2:    #F1F5F9;
  --border:      #E2E8F0;
  --text:        #0F172A;
  --muted:       #64748B;
  --accent:      #0EA5E9;
  --code-bg:     #0F172A;
  --code-text:   #E2E8F0;
  --code-border: #1E293B;
  --font-sans:   'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
  --font-serif:  'Georgia', 'Palatino Linotype', 'Book Antiqua', serif;
  --font-mono:   'Fira Code', 'Cascadia Code', 'Consolas', monospace;
  --max-width:   900px;
}

html { scroll-behavior: smooth; font-size: 16px; }

body {
  font-family: var(--font-serif);
  font-size: 1.0625rem;
  line-height: 1.8;
  color: var(--text);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
}

/* ── Layout ── */
.page-wrap { max-width: var(--max-width); margin: 0 auto; padding: 0 2rem 4rem; }

/* ── Cover ── */
.cover {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  text-align: center;
  padding: 4rem 2rem;
  background: #08081A;
  color: #F8FAFC;
  page-break-after: always;
}
.cover-accent-bar {
  width: 6px; height: 80px;
  background: #00D4FF;
  margin: 0 auto 2.5rem;
  border-radius: 3px;
}
.cover-label {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #94A3B8;
  margin-bottom: 1rem;
}
.cover-title {
  font-family: var(--font-sans);
  font-size: clamp(2.4rem, 6vw, 4rem);
  font-weight: 900;
  color: #FFFFFF;
  line-height: 1.1;
  margin-bottom: 1rem;
}
.cover-subtitle {
  font-family: var(--font-sans);
  font-size: 1.15rem;
  color: #94A3B8;
  margin-bottom: 3rem;
  max-width: 560px;
}
.cover-pills {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 3.5rem;
}
.cover-pill {
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.35rem 0.85rem;
  border-radius: 100px;
  border: 1px solid rgba(0,212,255,0.35);
  color: #00D4FF;
  background: rgba(0,212,255,0.07);
}
.cover-author-block { margin-top: 1rem; }
.cover-author-label {
  font-family: var(--font-sans);
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #64748B;
  margin-bottom: 0.25rem;
}
.cover-author {
  font-family: var(--font-sans);
  font-size: 1.25rem;
  font-weight: 700;
  color: #F1F5F9;
}
.cover-year {
  font-family: var(--font-sans);
  font-size: 0.875rem;
  color: #475569;
  margin-top: 2.5rem;
}
.cover-flyer {
  width: min(420px, 80vw);
  margin: 0 auto 2rem;
  opacity: 0.9;
}

/* ── Copyright page ── */
.copyright-page {
  padding: 6rem 2rem;
  max-width: 600px;
  margin: 0 auto;
  font-family: var(--font-sans);
  font-size: 0.875rem;
  color: var(--muted);
  line-height: 1.7;
  page-break-after: always;
}
.copyright-page h2 {
  font-size: 1.25rem;
  color: var(--text);
  margin-bottom: 1.5rem;
  font-weight: 700;
}
.copyright-page p { margin-bottom: 0.75rem; }

/* ── TOC ── */
.toc-page {
  padding: 4rem 2rem 6rem;
  max-width: var(--max-width);
  margin: 0 auto;
  page-break-after: always;
}
.toc-page h2 {
  font-family: var(--font-sans);
  font-size: 2rem;
  font-weight: 900;
  margin-bottom: 2.5rem;
  color: var(--text);
}
.toc-list {
  list-style: none;
  padding: 0;
}
.toc-part {
  font-family: var(--font-sans);
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 2rem 0 0.5rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid var(--border);
}
.toc-chapter a {
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
  padding: 0.55rem 0;
  text-decoration: none;
  color: var(--text);
  border-bottom: 1px solid var(--border);
  transition: color 150ms;
}
.toc-chapter a:hover { color: var(--accent); }
.toc-num {
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-weight: 700;
  min-width: 6rem;
}
.toc-title {
  font-family: var(--font-sans);
  font-size: 0.95rem;
  font-weight: 500;
}

/* ── Part dividers ── */
.part-divider {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  padding: 4rem 2rem;
  background: var(--surface);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  page-break-before: always;
  page-break-after: always;
}
.part-label {
  font-family: var(--font-sans);
  font-size: 0.7rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 0.75rem;
}
.part-title {
  font-family: var(--font-sans);
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 900;
  color: var(--text);
}
.part-accent {
  width: 60px; height: 5px;
  border-radius: 3px;
  margin: 1.25rem auto 0;
}

/* ── Chapter ── */
.chapter {
  padding: 5rem 0 4rem;
  page-break-before: always;
}
.ch-meta {
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 0.75rem;
}
.ch-number {
  font-family: var(--font-sans);
  font-size: clamp(3rem, 8vw, 5rem);
  font-weight: 900;
  line-height: 1;
  margin-bottom: 0.25rem;
}
.ch-title {
  font-family: var(--font-sans);
  font-size: clamp(1.75rem, 4vw, 2.75rem);
  font-weight: 800;
  color: var(--text);
  margin-bottom: 2rem;
  line-height: 1.15;
}
.ch-hero {
  width: 100%;
  max-width: 440px;
  height: auto;
  margin: 0 auto 3rem;
  display: block;
  border-radius: 12px;
}
.ch-divider {
  border: none;
  border-top: 2px solid var(--border);
  margin: 3rem 0;
}

/* ── Content typography ── */
.ch-content { max-width: var(--max-width); }

.ch-content h2 {
  font-family: var(--font-sans);
  font-size: 1.55rem;
  font-weight: 800;
  color: var(--text);
  margin: 3rem 0 1rem;
  padding-top: 0.5rem;
  border-top: 2px solid var(--border);
}
.ch-content h3 {
  font-family: var(--font-sans);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text);
  margin: 2rem 0 0.75rem;
}
.ch-content h4 {
  font-family: var(--font-sans);
  font-size: 1rem;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin: 1.5rem 0 0.5rem;
}
.ch-content p {
  margin-bottom: 1rem;
  max-width: 72ch;
}
.ch-content ul, .ch-content ol {
  margin: 0.75rem 0 1rem 1.75rem;
}
.ch-content li { margin-bottom: 0.3rem; }
.ch-content li > ul, .ch-content li > ol { margin-top: 0.3rem; }

.ch-content strong { font-weight: 700; color: var(--text); }
.ch-content em     { font-style: italic; }

.ch-content a {
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 2px;
}

/* ── Tables ── */
.ch-content table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-sans);
  font-size: 0.875rem;
  margin: 1.5rem 0;
  overflow-x: auto;
  display: block;
}
.ch-content th {
  background: var(--surface2);
  font-weight: 700;
  text-align: left;
  padding: 0.6rem 0.85rem;
  border: 1px solid var(--border);
  color: var(--text);
}
.ch-content td {
  padding: 0.5rem 0.85rem;
  border: 1px solid var(--border);
  vertical-align: top;
}
.ch-content tr:nth-child(even) td { background: var(--surface); }

/* ── Code ── */
.ch-content code {
  font-family: var(--font-mono);
  font-size: 0.85em;
  background: var(--surface2);
  color: #1E293B;
  padding: 0.15em 0.4em;
  border-radius: 4px;
  border: 1px solid var(--border);
}
.ch-content pre {
  background: var(--code-bg);
  color: var(--code-text);
  font-family: var(--font-mono);
  font-size: 0.84rem;
  line-height: 1.65;
  padding: 1.5rem 1.75rem;
  border-radius: 10px;
  overflow-x: auto;
  margin: 1.25rem 0 1.75rem;
  border: 1px solid var(--code-border);
  tab-size: 2;
}
.ch-content pre code {
  background: none;
  color: inherit;
  padding: 0;
  border: none;
  font-size: inherit;
  border-radius: 0;
}

/* Code language labels */
.ch-content pre::before {
  display: block;
  font-family: var(--font-sans);
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #64748B;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #1E293B;
}

/* ── Block quotes / callouts ── */
.ch-content blockquote {
  border-left: 4px solid var(--accent);
  background: #EFF6FF;
  padding: 1rem 1.25rem;
  margin: 1.5rem 0;
  border-radius: 0 6px 6px 0;
  font-style: italic;
  color: #1E40AF;
}
.ch-content blockquote p { margin-bottom: 0; max-width: 100%; color: inherit; }

/* ── HR ── */
.ch-content hr {
  border: none;
  border-top: 1px solid var(--border);
  margin: 2.5rem 0;
}

/* ── Inline images ── */
.ch-content img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 1rem 0;
}

/* ── Print ── */
@media print {
  body { font-size: 11pt; }
  .cover, .part-divider { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .chapter { page-break-before: always; }
  a { color: inherit; text-decoration: none; }
  .ch-content pre { white-space: pre-wrap; word-break: break-all; }
}
"""

# ── Assemble ──────────────────────────────────────────────────────────────────

def build_cover() -> str:
    flyer_src = "images/flyer.svg"
    flyer_tag = ""
    if (ROOT / flyer_src).exists():
        flyer_tag = f'<img class="cover-flyer" src="{flyer_src}" alt="ICTZoid Program" />'
    pills = ["HTML", "CSS", "JavaScript", "Git", "React", "Frontend AI"]
    pill_html = "".join(f'<span class="cover-pill">{p}</span>' for p in pills)
    return f"""
<div class="cover">
  <div class="cover-accent-bar"></div>
  <p class="cover-label">ICTZoid Web Development Program</p>
  <h1 class="cover-title">From Zero<br>to AI-Powered<br>Developer</h1>
  <p class="cover-subtitle">
    A complete curriculum covering how the web works, professional development practices,
    and the AI-powered tools shaping the next generation of frontend engineers.
  </p>
  <div class="cover-pills">{pill_html}</div>
  {flyer_tag}
  <div class="cover-author-block">
    <p class="cover-author-label">Written by</p>
    <p class="cover-author">Samuel M. Ortil</p>
  </div>
  <p class="cover-year">ICTZoid &nbsp;·&nbsp; 2026</p>
</div>
"""

def build_copyright() -> str:
    return """
<div class="copyright-page">
  <h2>Copyright</h2>
  <p>From Zero to AI-Powered Developer<br>
  ICTZoid Web Development Program</p>
  <p>&copy; 2026 Samuel M. Ortil &amp; ICTZoid. All rights reserved.</p>
  <p>
    No part of this publication may be reproduced, distributed, or transmitted in any form
    or by any means, including photocopying, recording, or other electronic or mechanical
    methods, without the prior written permission of the author.
  </p>
  <p>
    For permissions and enquiries, contact the ICTZoid team through the program platform.
  </p>
  <p style="margin-top:2rem;font-style:italic;color:#94A3B8">
    First edition &mdash; May 2026
  </p>
</div>
"""

def build_toc_page() -> str:
    return f"""
<div class="toc-page">
  <h2>Table of Contents</h2>
  <ul class="toc-list">
    {build_toc()}
  </ul>
</div>
"""

def build_part_dividers(chapters: list) -> dict:
    """Return a dict: part_label → divider HTML.  Only built once per part."""
    seen = {}
    for _, part, _, _, accent in chapters:
        if part not in seen:
            # Extract the label after "—"
            title = part.split("—", 1)[1].strip() if "—" in part else part
            prefix = part.split("—", 1)[0].strip() if "—" in part else ""
            seen[part] = f"""
<div class="part-divider">
  <p class="part-label">{prefix}</p>
  <h2 class="part-title">{title}</h2>
  <div class="part-accent" style="background:{accent}"></div>
</div>
"""
    return seen

def build_chapters(chapters: list) -> str:
    part_dividers = build_part_dividers(chapters)
    parts_emitted: set[str] = set()
    html_parts: list[str] = []

    for fname, part, num, title, accent in chapters:
        # Emit part divider once
        if part not in parts_emitted:
            html_parts.append(part_dividers[part])
            parts_emitted.add(part)

        # Load content
        if fname is None:
            content_html = load_chapter(None, HTML_CHAPTER_CONTENT)
        else:
            content_html = load_chapter(fname)

        img_tag = chapter_img_tag(num)

        html_parts.append(f"""
<section class="chapter page-wrap" id="ch{num}">
  <p class="ch-meta">Chapter {num}</p>
  <p class="ch-number" style="color:{accent}">{num:02d}</p>
  <h2 class="ch-title">{title}</h2>
  {img_tag}
  <hr class="ch-divider">
  <div class="ch-content">
    {content_html}
  </div>
</section>
""")

    return "\n".join(html_parts)

def build_html() -> str:
    cover      = build_cover()
    copyright_ = build_copyright()
    toc        = build_toc_page()
    chapters   = build_chapters(CHAPTERS)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>From Zero to AI-Powered Developer — ICTZoid</title>
  <style>
{CSS}
  </style>
</head>
<body>

{cover}
{copyright_}
{toc}
{chapters}

<div style="height:6rem"></div>

</body>
</html>
"""

if __name__ == "__main__":
    print("Building ebook…")
    html = build_html()
    OUT.write_text(html, encoding="utf-8")
    size_kb = OUT.stat().st_size // 1024
    print(f"Done → {OUT}  ({size_kb} KB)")
