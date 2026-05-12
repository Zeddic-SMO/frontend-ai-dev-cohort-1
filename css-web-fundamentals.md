# CSS — Web Fundamentals

CSS (Cascading Style Sheets) controls how HTML looks. This course covers everything from the fundamentals of selectors and the box model to Flexbox, CSS Grid, responsive design, animations, and building a maintainable design system with CSS custom properties. Every module builds directly on the previous one.

## Module 1 — Selectors, Cascade and the Box Model

Master the fundamentals that every other CSS concept builds on.

### Lesson 1.1 — How CSS Works and Selectors

A CSS rule has two parts: a selector and a declaration block.

```css
selector {
  property: value;
}
```

**Selector types:**

```css
/* Type selectors */
h1    { font-size: 2.5rem; }
p     { margin-bottom: 1rem; }

/* Class selectors (most common) */
.card        { border-radius: 8px; background: white; }
.btn-primary { background: #1A56A0; color: white; }

/* ID selectors (unique per page) */
#main-nav { position: sticky; top: 0; }

/* Combinators */
nav a    { text-decoration: none; }   /* descendant */
nav > ul { list-style: none; }        /* direct child */
h2 + p   { margin-top: 0; }          /* adjacent sibling */
h2 ~ p   { color: #555; }            /* general sibling */

/* Attribute selectors */
input[type="email"] { border-color: #1A56A0; }
a[target="_blank"]  { padding-right: 16px; }
a[href^="https"]    { /* starts with */ }
a[href$=".pdf"]     { /* ends with */ }
a[href*="github"]   { /* contains */ }

/* Pseudo-classes */
a:hover            { color: #7C3AED; }
a:focus-visible    { outline: 2px solid #7C3AED; }
input:invalid      { border-color: #DC2626; }
input:disabled     { opacity: 0.5; }
li:first-child     { border-top: none; }
li:last-child      { border-bottom: none; }
li:nth-child(odd)  { background: #F5F7FA; }
li:not(:last-child){ border-bottom: 1px solid #E5E7EB; }

/* Pseudo-elements */
p::first-line   { font-weight: bold; }
.card::before   { content: ""; display: block; height: 4px; background: #1A56A0; }
input::placeholder { color: #9CA3AF; }

/* :is() for grouping */
:is(h1, h2, h3) { font-family: 'Inter', sans-serif; line-height: 1.2; }
```

**Exercises:**

1. Write a single CSS selector for each: every `<a>` inside a `<nav>` that is also `:hover`, every `<input>` that is both `:focus` and `:invalid`, every `<li>` that is not the last child.
2. Add hover, focus, and active states to all links and buttons on your bio page. Each state should be visually distinct. Test with both mouse and keyboard (Tab to focus).

### Lesson 1.2 — The Cascade and Specificity

When two rules target the same element and set the same property, the cascade decides which wins. It checks three things in order:

1. **Origin** — Author CSS beats user CSS beats browser defaults
2. **Specificity** — More specific selector wins
3. **Order** — Later rule wins when specificity is equal

**Specificity scoring:** `(inline, ID, class/attr/pseudo, element)`

```css
/* Selector                  | Score    */
*                           /* 0,0,0,0  */
p                           /* 0,0,0,1  */
.card                       /* 0,0,1,0  */
#hero                       /* 0,1,0,0  */
p.card                      /* 0,0,1,1  */
nav a:hover                 /* 0,0,1,2  */
#hero .card p               /* 0,1,1,1  */
style="..."                 /* 1,0,0,0  */
```

Higher score wins. Equal score → later rule wins.

```css
/* Both target <p class="intro"> */
p.intro { color: blue; }   /* 0,0,1,1 */
body p  { color: red;  }   /* 0,0,0,2 */
/* Result: blue — higher specificity wins even though body p comes after */
```

**Practical rules:**
- Style with classes, not IDs — keeps specificity low and manageable
- Avoid `!important` — it breaks the cascade and is hard to override
- When you need to override a library, increase specificity slightly rather than using `!important`

**CSS Custom Properties (design tokens):**

```css
:root {
  /* Colours */
  --color-primary:  #1A56A0;
  --color-accent:   #7C3AED;
  --color-success:  #16A34A;
  --color-danger:   #DC2626;
  --color-text:     #1C1C1C;
  --color-muted:    #6B7280;
  --color-bg:       #FFFFFF;
  --color-surface:  #F5F7FA;
  --color-border:   #E5E7EB;

  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'Fira Code', monospace;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   1.125rem;
  --text-xl:   1.25rem;
  --text-2xl:  1.5rem;
  --text-4xl:  2.25rem;

  /* Spacing (4px base scale) */
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-6:  24px;
  --space-8:  32px;
  --space-12: 48px;
  --space-16: 64px;

  /* Radii */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
}
```

**Exercises:**

1. Predict the colour for `<p class="intro">` inside `<main id="content">` given: `p { color: red; }`, `.intro { color: blue; }`, `#content p { color: green; }`, `main .intro { color: orange; }`. Test your prediction in the browser and explain the result.
2. Create a `:root` token system for your bio page covering colours, font sizes, spacing, and shadows. Refactor every hardcoded value to use a variable.

### Lesson 1.3 — The Box Model and Sizing

Every element is a rectangular box with four layers:

```
┌─────────────────────────────┐
│           MARGIN            │  ← space outside the element
│  ┌───────────────────────┐  │
│  │        BORDER         │  │  ← visible edge
│  │  ┌─────────────────┐  │  │
│  │  │     PADDING     │  │  │  ← space between border and content
│  │  │  ┌───────────┐  │  │  │
│  │  │  │  CONTENT  │  │  │  │  ← text, images, children
│  │  │  └───────────┘  │  │  │
│  │  └─────────────────┘  │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```

**The box-sizing problem:**

```css
/* Default (content-box): width = content only */
.box { width: 300px; padding: 24px; border: 2px solid; }
/* Actual rendered width: 300 + 48 + 4 = 352px — confusing! */

/* border-box: width = content + padding + border */
.box { box-sizing: border-box; width: 300px; padding: 24px; border: 2px solid; }
/* Actual rendered width: 300px — predictable! */
```

Always add this to every project:

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

**Spacing shorthand:**

```css
.box {
  padding: 24px;                    /* all four sides */
  padding: 16px 24px;               /* top/bottom | left/right */
  padding: 8px 12px 16px 20px;     /* top | right | bottom | left */
  margin: 0 auto;                   /* centred horizontally */
}
```

**Display values:**

```css
div, p, h1  { display: block; }        /* full width, stacks vertically */
span, a     { display: inline; }       /* flows with text */
.badge      { display: inline-block; } /* flows with text, respects width/height */
.hidden     { display: none; }         /* removed from layout entirely */
.invisible  { visibility: hidden; }   /* hidden but still takes up space */
```

**Exercises:**

1. Create a `.card` with `box-sizing: border-box`, `width: 320px`, `padding: 24px`, `border: 1px solid`, `border-radius: 8px`. Inspect it in DevTools → Computed → Box Model. Verify the total width is exactly 320px.
2. Without `box-sizing: border-box`, what is the rendered width of `width: 400px; padding: 32px; border: 3px solid;`? Show your calculation.

### Lesson 1.4 — Typography

```css
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI',
               Roboto, Helvetica, Arial, sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.6;      /* 1.5–1.8 for readability */
  color: var(--color-text);
  -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
  font-weight: 700;
  line-height: 1.2;      /* tighter for headings */
}

/* Fluid sizing with clamp(min, preferred, max) */
h1 { font-size: clamp(2rem,   5vw, 3.5rem); }
h2 { font-size: clamp(1.5rem, 3vw, 2.25rem); }
h3 { font-size: clamp(1.25rem,2.5vw,1.75rem); }

p {
  max-width: 65ch;    /* optimal line length ~65 characters */
  font-size: 1rem;    /* = 16px (relative to root) */
}

code, pre {
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 0.875em; /* relative to parent element's font size */
}
```

**Units reference:**

| Unit | Relative to | Best for |
|------|------------|---------|
| `px` | Screen pixels | Borders, shadows |
| `rem` | Root font size (16px) | Font sizes, spacing |
| `em` | Parent font size | Padding on buttons (scales with font) |
| `%` | Parent dimension | Widths in fluid layouts |
| `vw/vh` | Viewport width/height | Hero heights, fluid spacing |
| `ch` | Width of "0" character | Line length control |
| `clamp()` | min / preferred / max | Fluid typography |

**Exercises:**

1. Set up the complete typography system above on your bio page. Every font size must use a CSS variable. No hardcoded `px` values for text.
2. Use `clamp()` for `h1` through `h3`. Resize your browser from 320px to 1400px — font sizes should scale smoothly without any media queries.

## Module 2 — Layout

Build any layout — from a navigation bar to a full dashboard — using Flexbox and CSS Grid.

### Lesson 2.1 — Flexbox Fundamentals

Flexbox is for **one-dimensional** layouts — items in a row or a column.

```css
/* Container properties */
.container {
  display: flex;

  flex-direction: row;          /* row | row-reverse | column | column-reverse */
  flex-wrap: nowrap;            /* nowrap | wrap */
  flex-flow: row wrap;          /* shorthand for direction + wrap */

  /* Main axis alignment */
  justify-content: flex-start;  /* flex-start | flex-end | center |
                                   space-between | space-around | space-evenly */

  /* Cross axis alignment */
  align-items: stretch;         /* stretch | flex-start | flex-end | center | baseline */

  align-content: flex-start;    /* multi-line cross axis */
  gap: 16px;                    /* gap between items */
  gap: 16px 24px;               /* row-gap column-gap */
}

/* Item properties */
.item {
  flex-grow:   0;       /* 0 = don't grow | 1 = grow to fill */
  flex-shrink: 1;       /* 1 = can shrink | 0 = never shrink */
  flex-basis:  auto;    /* base size before grow/shrink */
  flex: 1;              /* shorthand: 1 1 0% */
  flex: none;           /* shorthand: 0 0 auto */
  align-self: center;   /* override align-items for this item */
  order: -1;            /* change visual order (not DOM order) */
}
```

**Common patterns:**

```css
/* Perfect centering */
.centred { display: flex; align-items: center; justify-content: center; }

/* Nav bar: logo left, links right */
.nav      { display: flex; align-items: center; gap: 8px; }
.nav .logo{ margin-right: auto; }

/* Cards that wrap */
.cards { display: flex; flex-wrap: wrap; gap: 24px; }
.card  { flex: 1 1 280px; max-width: 400px; }

/* Sidebar layout */
.layout  { display: flex; gap: 32px; align-items: flex-start; }
.sidebar { flex: 0 0 280px; }
.content { flex: 1; }

/* Sticky footer */
body { display: flex; flex-direction: column; min-height: 100vh; }
main { flex: 1; }

/* Equal-height cards, footer always at bottom */
.card      { display: flex; flex-direction: column; }
.card-body { flex: 1; }
```

**Exercises:**

1. Build a navigation bar with Flexbox: logo left, links in the centre, "Enrol" button on the right. No absolute positioning.
2. Build a card grid: four cards that wrap naturally. Every card has equal height regardless of content. The footer inside each card sticks to the bottom.
3. Build a sticky footer layout: header at top, main content in the middle, footer always at the bottom even when content is short.

### Lesson 2.2 — Flexbox in Practice

```css
/* Media card — image left, content right */
.media-card {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}
.media-card__image { flex: 0 0 80px; }
.media-card__body  { flex: 1; }

/* Pill / badge */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 9999px;
}

/* Form row */
.input-group {
  display: flex;
  align-items: stretch;
}
.input-group input  { flex: 1; border-radius: 6px 0 0 6px; }
.input-group button { flex: 0 0 auto; border-radius: 0 6px 6px 0; }

/* Responsive reorder — image below text on mobile, left on desktop */
.feature {
  display: flex;
  flex-direction: column;
  gap: 24px;
}
.feature__image { order: 2; }  /* below text by default */
.feature__text  { order: 1; }

@media (min-width: 768px) {
  .feature            { flex-direction: row; }
  .feature__image     { order: 1; }  /* left on desktop */
  .feature__text      { order: 2; }
}
```

**Exercises:**

1. Build a "media card" component (avatar left, name + bio right) using Flexbox. The avatar should never shrink, even when the bio text is very long.
2. Build a search input group: a text input and a "Search" button fused into a single pill shape. The input grows to fill space; the button stays a fixed width.

### Lesson 2.3 — CSS Grid Fundamentals

CSS Grid is for **two-dimensional** layouts — rows AND columns simultaneously.

```css
/* Container properties */
.grid {
  display: grid;

  /* Explicit columns */
  grid-template-columns: 200px 1fr 1fr;
  grid-template-columns: repeat(3, 1fr);
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); /* responsive */
  grid-template-columns: 280px minmax(0, 1fr);

  /* Explicit rows */
  grid-template-rows: auto 1fr auto;

  /* Named areas */
  grid-template-areas:
    "header  header"
    "sidebar content"
    "footer  footer";

  gap: 24px;
  align-items: start;
}

/* Item placement by named area */
header  { grid-area: header; }
.sidebar{ grid-area: sidebar; }
main    { grid-area: content; }
footer  { grid-area: footer; }

/* Item placement by line numbers */
.hero { grid-column: 1 / 3; grid-row: 1; }
.full { grid-column: 1 / -1; }   /* span all columns */
.wide { grid-column: span 2; }   /* span 2 from wherever it lands */
```

**Practical layouts:**

```css
/* Responsive card grid — no media queries needed */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

/* Classic page layout */
.page {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "footer";
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

/* Dashboard — 12 column grid */
.dashboard {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 16px;
}
.stat-card  { grid-column: span 3; }   /* 4 per row */
.chart-main { grid-column: span 8; }
.chart-side { grid-column: span 4; }
.table      { grid-column: 1 / -1; }  /* full width */
```

**Exercises:**

1. Build a full-page layout with `grid-template-areas`: header spanning both columns, sidebar (280px), content (flexible), and footer spanning both. Use `min-height: 100vh`.
2. Build a responsive card grid with `auto-fit` and `minmax(280px, 1fr)`. Cards should fill all available space with no empty gaps. Test by resizing the browser.

### Lesson 2.4 — Grid in Practice

```css
/* Image mosaic */
.mosaic {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
  gap: 8px;
}
.mosaic .featured {
  grid-column: span 2;
  grid-row: span 2;
}
.mosaic img {
  width: 100%; height: 100%;
  object-fit: cover;
}

/* Marketing grid (asymmetric) */
.marketing {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: auto auto;
  gap: 24px;
}
.marketing .hero-text { grid-column: 1 / 3; }
.marketing .hero-img  { grid-row: 1 / 3; grid-column: 3; }
```

**Grid vs Flexbox — the rule of thumb:**
- Use **Grid** when you are designing the page or a complex two-dimensional area
- Use **Flexbox** inside Grid cells for component-level alignment

```css
/* Grid for the page structure */
.page {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 32px;
}

/* Flexbox inside a grid cell */
.card {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
}
```

**Exercises:**

1. Build a dashboard: 4 stat cards (span 3 of 12 columns each), a large chart (span 8) and small chart (span 4), and a full-width table below.
2. Build a 4×4 image mosaic where the first image is double-width and double-height. All images use `object-fit: cover` and fill their cells perfectly.

## Module 3 — Responsive Design and Visual Effects

Make pages work on every screen size and feel polished with motion and transitions.

### Lesson 3.1 — Mobile-First Responsive Design

**Mobile-first means:** write base styles for mobile, then add media queries for larger screens. Smaller is simpler — start there.

```css
/* Base styles — mobile (0px+) */
.card {
  width: 100%;
  padding: var(--space-4);
  font-size: var(--text-base);
}

.cards {
  display: grid;
  grid-template-columns: 1fr;   /* single column */
  gap: var(--space-4);
}

/* Tablet (640px+) */
@media (min-width: 640px) {
  .cards { grid-template-columns: repeat(2, 1fr); }
  .card  { padding: var(--space-6); }
}

/* Laptop (1024px+) */
@media (min-width: 1024px) {
  .cards { grid-template-columns: repeat(3, 1fr); }
}

/* Desktop (1280px+) */
@media (min-width: 1280px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--space-6);
  }
}
```

**Standard breakpoints:**

| Name | Width | Target |
|------|-------|--------|
| sm | 640px | Large phones |
| md | 768px | Tablets |
| lg | 1024px | Laptops |
| xl | 1280px | Desktops |
| 2xl | 1536px | Wide screens |

**Other media query features:**

```css
@media (prefers-color-scheme: dark)     { /* OS dark mode         */ }
@media (prefers-reduced-motion: reduce) { /* Motion sensitivity   */ }
@media (orientation: landscape)        { /* Landscape phone       */ }
@media print                           { /* Print stylesheet      */ }
```

**Exercises:**

1. Rebuild your bio page as mobile-first. Single column on mobile, two columns at 640px, three columns at 1024px. No desktop styles in the base CSS.
2. Add a `prefers-reduced-motion` query that disables all animations and transitions for users who prefer reduced motion.

### Lesson 3.2 — Responsive Navigation

```css
/* Mobile — vertical menu, hidden by default */
.nav-links {
  display: none;
  flex-direction: column;
  position: absolute;
  top: 64px; left: 0;
  width: 100%;
  background: white;
  padding: var(--space-4);
  border-top: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
}

.nav-links.is-open {
  display: flex;
  animation: slideDown 200ms ease-out;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-8px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hamburger { display: flex; }

/* Desktop — horizontal, always visible */
@media (min-width: 768px) {
  .nav-links {
    display: flex;
    flex-direction: row;
    position: static;
    width: auto;
    padding: 0;
    box-shadow: none;
    border-top: none;
    gap: var(--space-2);
  }
  .hamburger { display: none; }
}
```

The JavaScript toggle updates `aria-expanded` and `aria-label` on each click:

```javascript
const hamburger = document.querySelector('.hamburger');
const navLinks  = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('is-open');
  hamburger.setAttribute('aria-expanded', isOpen);
  hamburger.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
});
```

**Exercises:**

1. Build a complete responsive navigation with hamburger toggle. The toggle must update `aria-expanded` and have a visible focus ring. At 768px it becomes a horizontal menu.

### Lesson 3.3 — Transitions and Animations

```css
/* Transitions — animate from one state to another */
.btn {
  background: var(--color-primary);
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
  /* Always transition specific properties — never 'all' */
  transition: background 200ms ease,
              transform  200ms ease,
              box-shadow 200ms ease;
}
.btn:hover  { background: #1246A0; transform: translateY(-2px); box-shadow: var(--shadow-md); }
.btn:active { transform: translateY(0); box-shadow: var(--shadow-sm); }
```

**Timing functions:**

```css
transition-timing-function: ease;                         /* starts fast, slows at end */
transition-timing-function: ease-in-out;                  /* slow start and end */
transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);/* Material Design standard */
```

**Keyframe animations:**

```css
/* Entrance */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Loading spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Pulsing badge */
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.05); }
}

/* Skeleton shimmer */
@keyframes shimmer {
  from { background-position: -200% 0; }
  to   { background-position:  200% 0; }
}

/* Usage */
.hero-title { animation: fadeUp 600ms ease-out both; }

.spinner {
  width: 24px; height: 24px;
  border: 3px solid #E5E7EB;
  border-top-color: var(--color-primary);
  border-radius: 50%;
  animation: spin 700ms linear infinite;
}

.skeleton {
  background: linear-gradient(90deg, #E5E7EB 25%, #F3F4F6 50%, #E5E7EB 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: var(--radius-sm);
}

/* Staggered list entrance */
.item:nth-child(1) { animation: fadeUp 400ms ease-out both; animation-delay:   0ms; }
.item:nth-child(2) { animation: fadeUp 400ms ease-out both; animation-delay: 100ms; }
.item:nth-child(3) { animation: fadeUp 400ms ease-out both; animation-delay: 200ms; }
```

**Performance — only animate:**
- `transform` (translate, rotate, scale)
- `opacity`

Animating `width`, `height`, `margin`, `top`, `left` causes layout recalculation and janky performance.

```css
/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Exercises:**

1. Add hover transitions to all cards and buttons: lift (`translateY(-2px)`), deeper shadow, slight brightness change. All 200ms ease.
2. Add a `fadeUp` animation to each section on your page. Stagger them with `animation-delay` so they appear sequentially.
3. Build a loading spinner and a skeleton card using only CSS animations. Add the `prefers-reduced-motion` override.

### Lesson 3.4 — Theming and Dark Mode

```css
/* Light theme (default) */
:root {
  --bg:         #FFFFFF;
  --bg-subtle:  #F5F7FA;
  --text:       #1C1C1C;
  --text-muted: #6B7280;
  --border:     #E5E7EB;
  --shadow:     rgba(0,0,0,0.08);
}

/* Dark theme */
[data-theme="dark"] {
  --bg:         #0B1628;
  --bg-subtle:  #0F1E35;
  --text:       #F1F5F9;
  --text-muted: #94A3B8;
  --border:     #1E2D45;
  --shadow:     rgba(0,0,0,0.4);
}

/* OS preference — applies when user has not toggled manually */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:         #0B1628;
    --bg-subtle:  #0F1E35;
    --text:       #F1F5F9;
    --text-muted: #94A3B8;
    --border:     #1E2D45;
    --shadow:     rgba(0,0,0,0.4);
  }
}

/* Smooth transition when toggling */
body {
  background: var(--bg);
  color: var(--text);
  transition: background 300ms ease, color 300ms ease;
}
```

The JavaScript toggle persists the user's choice to `localStorage`:

```javascript
const root   = document.documentElement;
const toggle = document.querySelector('#theme-toggle');

const saved = localStorage.getItem('theme');
if (saved) root.setAttribute('data-theme', saved);
updateToggleLabel();

toggle.addEventListener('click', () => {
  const current = root.getAttribute('data-theme');
  const next    = current === 'dark' ? 'light' : 'dark';
  root.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
  updateToggleLabel();
});

function updateToggleLabel() {
  const isDark = root.getAttribute('data-theme') === 'dark';
  toggle.textContent = isDark ? '☀️ Light' : '🌙 Dark';
  toggle.setAttribute('aria-label',
    isDark ? 'Switch to light mode' : 'Switch to dark mode');
}
```

**Exercises:**

1. Add a fully working dark/light toggle to your bio page. The correct theme should load on refresh. The toggle button must have an accessible `aria-label`.
2. Audit your dark theme: check every text/background combination passes WCAG AA (4.5:1 for normal text). Fix any failures.

## Module 4 — CSS Architecture

Write CSS that stays maintainable as the project grows.

### Lesson 4.1 — CSS Reset and Base Styles

**Modern CSS reset:**

```css
/* reset.css */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html {
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
  hanging-punctuation: first last;
}

body {
  font-family: var(--font-sans);
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}

img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

input, button, textarea, select { font: inherit; }

p, h1, h2, h3, h4, h5, h6 { overflow-wrap: break-word; }

a { color: inherit; text-decoration: none; }

ul, ol { list-style: none; }

button { cursor: pointer; background: none; border: none; }

:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```

**Recommended file organisation:**

```
styles/
├── base/
│   ├── reset.css         ← normalize browser defaults
│   ├── tokens.css        ← CSS custom properties
│   └── typography.css    ← base text styles
├── components/
│   ├── button.css
│   ├── card.css
│   ├── nav.css
│   └── form.css
├── layout/
│   ├── header.css
│   ├── footer.css
│   └── grid.css
├── pages/
│   └── home.css
└── main.css              ← @import all the above
```

**Exercises:**

1. Refactor your bio page CSS into the file structure above. Create separate files for tokens, reset, components (card, button, nav), and layout. Import them all in `main.css`.

### Lesson 4.2 — Module Review and Checklist

**Pre-project CSS checklist:**

- `box-sizing: border-box` applied globally
- CSS custom properties for colours, fonts, spacing, and radii
- All selectors use classes — no styling via IDs
- No `!important` used
- Mobile-first: base styles for mobile, media queries for larger screens
- Flexbox used for component-level layouts
- CSS Grid used for page-level layouts
- Transitions on interactive elements (hover, focus) — all 200ms ease
- Animations use only `transform` and `opacity`
- `prefers-reduced-motion` media query disables motion
- Dark/light theme with `data-theme` attribute and localStorage
- CSS files organised by responsibility
- Lighthouse Performance score ≥ 90 (no unused CSS, no render-blocking)

**Exercises:**

1. Apply the full checklist to your bio page. Document each item as Pass / Fail. Fix all failures before moving on.
2. Share your CSS file structure in the community. Get feedback on organisation. Refactor based on one piece of feedback you receive.
