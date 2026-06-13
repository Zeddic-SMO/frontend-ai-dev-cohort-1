# CSS — Web Fundamentals

## Welcome! What is CSS?

Imagine you built a house out of LEGO bricks. The bricks are the **HTML** — the structure and the content.

**CSS is the paint, wallpaper, and furniture.** It controls what colour things are, how big they are, where they sit on the page, and how they move.

Without CSS, every website would look like a plain text document — just black words on a white background. CSS is what makes websites look cool.

**Here's how CSS connects to HTML:**

```html
<!-- This is your HTML file -->
<head>
  <link rel="stylesheet" href="style.css">  <!-- connects your CSS file -->
</head>
<body>
  <h1>Hello World!</h1>
</body>
```

```css
/* This is your style.css file */
h1 {
  color: hotpink;
  font-size: 48px;
}
```

That's it — your heading is now big and pink!

---

## Module 1 — Painting and Decorating

### Lesson 1.1 — How CSS Rules Work

A CSS "rule" is like an instruction you give to the browser. It has two parts:

1. **The selector** — *who* you're talking to ("hey, all headings!")
2. **The declarations** — *what* to change ("make them blue and big")

```css
/* ↓ selector: targets all <h1> elements */
h1 {
  color: blue;       /* ← declaration: change the colour */
  font-size: 32px;   /* ← declaration: change the size */
}
/* ↑ everything between { } is the declaration block */
```

Every declaration is written as `property: value;` — always with a colon in the middle and a semicolon at the end.

---

**Three ways to point at elements**

**1. By tag name** — targets every element of that type

```css
/* makes ALL paragraphs dark grey */
p {
  color: #333333;
}

/* makes ALL headings bold */
h1 {
  font-weight: bold;
}
```

**2. By class** — targets elements you've labelled (most common!)

```html
<!-- you add the class in HTML -->
<div class="card">I am a card!</div>
<div class="card">Me too!</div>
```

```css
/* targets only elements with class="card" */
.card {
  background: white;
  border-radius: 8px;  /* rounds the corners */
}
```

Think of a class like a colour of sticky note. Any element with that sticky note gets those styles.

**3. By ID** — targets one specific element (use sparingly)

```html
<nav id="main-nav">...</nav>
```

```css
/* targets only the element with id="main-nav" */
#main-nav {
  background: navy;
}
```

> **Golden rule:** Use classes (`.name`) most of the time. IDs (`#name`) are for one-of-a-kind elements only.

---

**Styling based on what's happening — pseudo-classes**

You can style an element differently depending on what the user is doing:

```css
/* when the mouse hovers over a link */
a:hover {
  color: purple;
}

/* when a button is clicked */
button:active {
  background: darkblue;
}

/* the very first item in a list */
li:first-child {
  font-weight: bold;
}

/* the very last item in a list */
li:last-child {
  border-bottom: none;
}
```

---

**Try it yourself!**

Create an `index.html` and a `style.css`. In your HTML, add:
- A heading `<h1>` with your name
- A paragraph `<p>` with a fun fact about yourself
- A `<div class="card">` around a short description of your favourite hobby

In your CSS:
- Change the `<h1>` to your favourite colour
- Make `.card` have a background colour and rounded corners
- Add a hover colour change to any link

---

### Lesson 1.2 — Colours and Text

**Colours in CSS**

There are several ways to write a colour:

```css
.box {
  /* by name — easy to read, limited options */
  color: red;
  color: hotpink;
  color: cornflowerblue;

  /* hex code — a specific colour (the most common way) */
  color: #FF0000;   /* red */
  color: #1A56A0;   /* a nice blue */
  color: #FFFFFF;   /* white */
  color: #000000;   /* black */

  /* rgb — Red, Green, Blue, each from 0–255 */
  color: rgb(255, 0, 0);       /* red */
  color: rgb(26, 86, 160);     /* that same nice blue */

  /* rgba — same as rgb, but with transparency (0 = invisible, 1 = solid) */
  background: rgba(0, 0, 0, 0.5); /* semi-transparent black */
}
```

> **Tip:** In VS Code, click on any colour value and a colour picker will appear. You can drag to choose any colour you like!

---

**Text styling**

```css
p {
  font-size: 18px;       /* how big the text is */
  font-weight: bold;     /* bold, or use a number like 400 (normal) or 700 (bold) */
  font-style: italic;    /* slanted text */
  text-align: center;    /* left | center | right */
  text-decoration: underline; /* underline, line-through, or none */
  line-height: 1.6;      /* space between lines — 1.5 to 1.8 is comfortable to read */
  letter-spacing: 2px;   /* space between letters */
  color: #333333;        /* the text colour */
}
```

**Choosing fonts**

Browsers come with only a few built-in fonts. You can load extra ones from Google Fonts for free:

```html
<!-- Add this inside your <head> in HTML -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
```

```css
/* Now use it in CSS */
body {
  font-family: 'Poppins', sans-serif;
}
```

---

**Try it yourself!**

Add these to your bio page:
1. Give the `<body>` a background colour you like
2. Make your `<h1>` a different font and a large size
3. Make your paragraph text comfortable to read with `line-height: 1.7`
4. Pick a Google Font and load it into your project

---

### Lesson 1.3 — The Box Model (Everything is a Box!)

Here's a secret: **every single thing on a web page is a rectangle**. Even circles are just rectangles with very round corners.

Every rectangle has four layers, like layers of a sandwich:

```
┌─────────────────────────────┐
│           MARGIN            │  ← empty space OUTSIDE the element
│  ┌───────────────────────┐  │
│  │        BORDER         │  │  ← the visible edge (like a picture frame)
│  │  ┌─────────────────┐  │  │
│  │  │     PADDING     │  │  │  ← breathing room INSIDE the border
│  │  │  ┌───────────┐  │  │  │
│  │  │  │  CONTENT  │  │  │  │  ← your actual text or image
│  │  │  └───────────┘  │  │  │
│  │  └─────────────────┘  │  │
│  └───────────────────────┘  │
└─────────────────────────────┘
```

Think of it like a framed photo:
- The **photo** is the content
- The white space inside the frame is the **padding**
- The **frame** itself is the border
- The wall space around the frame is the **margin**

---

**Setting each layer:**

```css
.card {
  /* CONTENT size */
  width: 300px;
  height: 200px;

  /* PADDING — space inside, between content and border */
  padding: 20px;           /* all four sides */
  padding: 10px 20px;      /* top+bottom | left+right */

  /* BORDER — the visible edge */
  border: 2px solid black; /* thickness | style | colour */
  border-radius: 12px;     /* rounds the corners */

  /* MARGIN — space outside, between this and other elements */
  margin: 16px;            /* all four sides */
  margin: 0 auto;          /* 0 top/bottom, auto left/right = horizontally centred */
}
```

---

**The box-sizing fix (very important!)**

By default, `width` only counts the content — padding and border are *added on top*. This is confusing. Here's the problem:

```css
.box {
  width: 300px;
  padding: 20px;    /* adds 20px on left AND right = 40px extra */
  border: 2px solid;/* adds 2px on left AND right = 4px extra */
}
/* Actual width on screen: 300 + 40 + 4 = 344px — NOT what you said! */
```

The fix — paste this at the very top of every CSS file you ever write:

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

Now `width: 300px` means the *total* width is 300px, including padding and border. Much more predictable!

---

**Try it yourself!**

1. Create a `.card` div with some text inside. Give it:
   - A background colour
   - `padding: 24px`
   - `border: 2px solid` in a colour of your choice
   - `border-radius: 12px`
   - `margin: 20px auto` to centre it on the page

2. Open your browser's DevTools (right-click → Inspect) and click on your card. You'll see the box model diagram showing exactly how much space each layer takes up.

---

### Lesson 1.4 — CSS Variables (Your Colour Palette!)

Imagine having to change your website's main colour from blue to green. If you typed `#1A56A0` in 50 different places, you'd have to change it 50 times.

**CSS variables** let you define a value once and use it everywhere:

```css
/* Define your variables at the top of your CSS — inside :root */
:root {
  --my-blue: #1A56A0;
  --my-pink: #FF6B9D;
  --text-colour: #333333;
  --spacing-small: 8px;
  --spacing-medium: 16px;
  --spacing-large: 32px;
}
```

```css
/* Use them anywhere with var(--name) */
h1 {
  color: var(--my-blue);
  margin-bottom: var(--spacing-medium);
}

.card {
  border: 2px solid var(--my-blue);
  padding: var(--spacing-medium);
  color: var(--text-colour);
}

.highlight {
  background: var(--my-pink);
}
```

Now to change your blue to green — change it in ONE place and everything updates instantly.

---

**Try it yourself!**

Add a `:root` block with:
- Your favourite main colour as `--color-main`
- A background colour as `--color-bg`
- A text colour as `--color-text`
- Three spacing sizes: `--space-small`, `--space-medium`, `--space-large`

Then update your page to use `var()` everywhere instead of typing the values directly.

---

## Module 2 — Arranging Things on the Page

Up until now, elements just stack on top of each other — one after another, top to bottom. This module is about *controlling where things go*.

### Lesson 2.1 — Flexbox: Arranging Things in a Row or Column

**What is Flexbox?**

Imagine you have a shelf. You can put items on it and decide:
- Should they line up left-to-right, or top-to-bottom?
- Should they be squished together or spread out?
- Should they be at the top, middle, or bottom of the shelf?

That's Flexbox! You apply it to the **container** (the shelf), and it controls how the **children** (the items) are arranged.

```css
.shelf {
  display: flex; /* turns on Flexbox — all direct children become flex items */
}
```

---

**Direction: row or column?**

```css
.container {
  display: flex;
  flex-direction: row;    /* → items go left to right (the default) */
  /* flex-direction: column; ↓ items go top to bottom */
}
```

---

**Spacing items along the main direction**

```css
.container {
  display: flex;
  justify-content: flex-start;    /* pack everything to the left */
  justify-content: center;        /* everything in the middle */
  justify-content: flex-end;      /* pack everything to the right */
  justify-content: space-between; /* first item left, last item right, rest spread out */
  justify-content: space-evenly;  /* equal space between AND around all items */
}
```

**Aligning items in the other direction**

```css
.container {
  display: flex;
  align-items: flex-start; /* items line up at the top */
  align-items: center;     /* items line up in the middle (vertically) */
  align-items: flex-end;   /* items line up at the bottom */
  align-items: stretch;    /* items stretch to fill the full height (default) */
}
```

---

**Gap — space between items**

```css
.container {
  display: flex;
  gap: 16px; /* adds 16px of space between each item */
}
```

---

**The most useful Flexbox trick: perfect centering**

Centering something used to be hard. With Flexbox it's three lines:

```css
.centred-box {
  display: flex;
  justify-content: center; /* centre horizontally */
  align-items: center;     /* centre vertically */
  height: 300px;           /* needs a height to centre in */
}
```

---

**Common patterns you'll use constantly**

```css
/* Navigation bar — logo on the left, links on the right */
.nav {
  display: flex;
  align-items: center;
}
.nav .logo {
  margin-right: auto; /* pushes everything after it to the far right */
}

/* Cards that wrap to a new row when there's no room */
.card-grid {
  display: flex;
  flex-wrap: wrap; /* allow wrapping */
  gap: 24px;
}
.card {
  flex: 1 1 250px; /* each card is at least 250px wide, then grows to fill space */
}

/* Make the footer always sit at the bottom of the page */
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* at least as tall as the screen */
}
main {
  flex: 1; /* main content grows to fill all leftover space */
}
```

---

**Try it yourself!**

1. **Centering challenge:** Create a `<div class="hero">` that is 400px tall. Put an `<h1>` inside it. Use Flexbox to perfectly centre the heading both horizontally and vertically.

2. **Navigation challenge:** Build a nav bar with a logo on the left and three links on the right. Use Flexbox with `margin-right: auto` on the logo — no floating, no absolute positioning.

3. **Card grid challenge:** Create four `<div class="card">` elements inside a container. Use Flexbox with `flex-wrap: wrap` so they arrange themselves automatically. Make each card at least 200px wide.

---

### Lesson 2.2 — CSS Grid: Drawing a Layout on Graph Paper

**What is CSS Grid?**

Flexbox is great for one direction at a time (a row *or* a column). But what if you need to control rows *and* columns at the same time — like a newspaper layout or a photo gallery?

That's what **CSS Grid** is for. Think of it like drawing a grid on graph paper, then deciding which squares each piece of content occupies.

---

**Setting up a grid**

```css
.container {
  display: grid;

  /* Define 3 equal columns */
  grid-template-columns: 1fr 1fr 1fr;

  /* Same thing, shorter */
  grid-template-columns: repeat(3, 1fr);

  /* Space between all cells */
  gap: 24px;
}
```

`1fr` means "1 fraction of the available space". Three `1fr` columns means three equal-width columns.

---

**A magic responsive trick**

This one line creates as many columns as will fit, with no media queries:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}
```

Translation: "Make columns that are at least 250px wide. Fit as many as you can. Stretch them equally to fill any leftover space."

Resize your browser — the number of columns adjusts automatically!

---

**Naming areas (the easy way to build page layouts)**

Instead of counting rows and columns, you can give areas names:

```css
.page {
  display: grid;
  grid-template-areas:
    "header  header"    /* row 1: header takes up both columns */
    "sidebar content"   /* row 2: sidebar on left, content on right */
    "footer  footer";   /* row 3: footer takes up both columns */
  grid-template-columns: 250px 1fr; /* sidebar is 250px, content fills the rest */
  grid-template-rows: auto 1fr auto; /* header and footer shrink to content, main grows */
  min-height: 100vh;
}

/* Each element claims its named area */
header  { grid-area: header; }
.sidebar{ grid-area: sidebar; }
main    { grid-area: content; }
footer  { grid-area: footer; }
```

---

**Making items span multiple columns or rows**

```css
/* This item takes up 2 columns */
.wide-card {
  grid-column: span 2;
}

/* This item takes up the full width (from first to last column) */
.full-width {
  grid-column: 1 / -1;
}
```

---

**Grid vs Flexbox — which one do I use?**

| Situation | Use |
|---|---|
| Items in a single row (navigation, button group) | Flexbox |
| Items in a single column (stacked content) | Flexbox |
| Full-page layout (header, sidebar, footer) | Grid |
| Photo gallery or card gallery | Grid |
| Both — align items *inside* a grid cell | Flexbox inside Grid |

They work great together. Use Grid for the big picture, Flexbox inside each piece.

---

**Try it yourself!**

1. **Page layout challenge:** Create a full page layout with `grid-template-areas` — a header, a 250px sidebar, a main content area, and a footer. Give each area a different background colour so you can see the layout clearly.

2. **Photo gallery challenge:** Create 6 `<div>` boxes inside a grid container. Use `auto-fit` and `minmax(200px, 1fr)` so they arrange into as many columns as fit. Resize the browser to see them reflow.

---

## Module 3 — Making It Look Great on Every Screen

### Lesson 3.1 — Responsive Design: Phones, Tablets, Desktops

**The problem**

Your page might look perfect on your laptop. But someone opening it on their phone sees a completely different screen — much narrower. Without responsive design, your layout might break completely.

**The solution: media queries**

A media query lets you say "apply these styles ONLY when the screen is a certain width":

```css
/* These styles apply to EVERYONE, all screen sizes */
.card {
  width: 100%;    /* full width on small screens */
  padding: 16px;
}

/* These styles ONLY apply when the screen is 768px or wider */
@media (min-width: 768px) {
  .card {
    width: 48%;   /* two cards side by side on tablets */
    padding: 24px;
  }
}

/* These styles ONLY apply when the screen is 1024px or wider */
@media (min-width: 1024px) {
  .card {
    width: 30%;   /* three cards per row on laptops */
  }
}
```

---

**Start from mobile — always**

This is called **"mobile-first"** design. Write your default styles for small screens, then *add* complexity for larger screens. It's easier than the other way around.

```css
/* WRONG way — start desktop, try to undo for mobile */
.menu { display: flex; } /* desktop style first */
@media (max-width: 768px) {
  .menu { display: none; } /* messy override */
}

/* RIGHT way — start mobile, add for larger screens */
.menu { display: none; }  /* hidden on mobile */
@media (min-width: 768px) {
  .menu { display: flex; } /* shown on desktop */
}
```

---

**Common screen size breakpoints**

| Name | Width | What it targets |
|---|---|---|
| Small | 640px | Large phones |
| Medium | 768px | Tablets |
| Large | 1024px | Laptops |
| Extra large | 1280px | Desktop monitors |

---

**A special media query for people who prefer less movement**

Some people get dizzy from lots of animation. You can turn off your animations for them:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
```

---

**Try it yourself!**

1. Take your card grid and make it truly responsive:
   - 1 card per row on mobile (default)
   - 2 cards per row at 640px
   - 3 cards per row at 1024px

2. Use your browser's DevTools to simulate a phone. In Chrome: right-click → Inspect → click the phone icon in the top-left of DevTools. Test your page at iPhone and iPad sizes.

---

### Lesson 3.2 — Transitions and Animations

**Transitions — smooth changes**

Without transitions, changes are instant and jarring. With them, changes animate smoothly.

```css
.button {
  background: blue;
  /* list the properties you want to animate smoothly */
  transition: background 200ms ease;
}

.button:hover {
  background: darkblue; /* this change now animates over 200 milliseconds */
}
```

The transition property takes: `property duration timing-function`
- `property` — what to animate (`background`, `color`, `transform`, etc.)
- `duration` — how long (`200ms` = 0.2 seconds)
- `timing-function` — the speed curve (`ease` = starts fast, slows down)

---

**Transform — move, scale, and rotate without breaking layout**

```css
.card {
  transition: transform 200ms ease, box-shadow 200ms ease;
}

.card:hover {
  transform: translateY(-4px); /* lifts the card up 4px */
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); /* bigger shadow */
}
```

`transform` is special — it doesn't affect other elements' positions, so it's smooth and fast.

Common transforms:
```css
transform: translateY(-4px);  /* move up 4px */
transform: translateX(10px);  /* move right 10px */
transform: scale(1.05);       /* make 5% bigger */
transform: rotate(45deg);     /* rotate 45 degrees */
```

---

**Keyframe animations — play automatically**

For animations that play without user interaction (like a spinner):

```css
/* Step 1: define the animation */
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

/* Step 2: apply it */
.loader {
  width: 32px;
  height: 32px;
  border: 4px solid lightgrey;
  border-top-color: blue;
  border-radius: 50%; /* makes it a circle */
  animation: spin 1s linear infinite; /* name | duration | timing | repeat */
}
```

---

```css
/* Fade in and float up — great for page sections */
@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.section {
  animation: fadeUp 500ms ease-out;
}
```

---

**Try it yourself!**

1. Add a hover effect to your cards:
   - Lift up with `translateY(-4px)`
   - Add a bigger shadow
   - Change the transition duration and see how it feels

2. Build a loading spinner using `@keyframes spin` and `border-radius: 50%`. Make it spin infinitely.

3. Make your page sections fade up when they appear using `@keyframes fadeUp`.

---

### Lesson 3.3 — Dark Mode

Dark mode is when the website switches to a dark background with light text. Many people prefer it at night. Here's how to build it.

**The idea**

Instead of writing colours directly in your CSS, you use variables. Then you just swap the variable values when dark mode is on.

```css
/* Light mode colours (default) */
:root {
  --bg:   #FFFFFF;   /* white background */
  --text: #1C1C1C;   /* almost-black text */
  --card: #F5F7FA;   /* light grey card */
}

/* Dark mode colours — only when data-theme="dark" is set on <html> */
[data-theme="dark"] {
  --bg:   #0D1117;   /* very dark background */
  --text: #E6EDF3;   /* light text */
  --card: #161B22;   /* dark card */
}

/* Use the variables everywhere */
body {
  background: var(--bg);
  color: var(--text);
  transition: background 300ms, color 300ms; /* smooth switch */
}

.card {
  background: var(--card);
}
```

**The JavaScript toggle:**

```javascript
const toggleBtn = document.querySelector('#theme-toggle');
const html = document.documentElement; // this is the <html> element

toggleBtn.addEventListener('click', () => {
  // If dark mode is on, switch to light — and vice versa
  if (html.getAttribute('data-theme') === 'dark') {
    html.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light'); // remember the choice
  } else {
    html.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
  }
});

// When the page loads, use the saved choice
const saved = localStorage.getItem('theme');
if (saved) {
  html.setAttribute('data-theme', saved);
}
```

---

**Try it yourself!**

1. Add CSS variables for light and dark colours to your bio page
2. Add a toggle button in your navigation
3. Wire up the JavaScript to switch themes on click
4. Refresh the page — the chosen theme should still be active

---

## Module 4 — Keeping Your CSS Tidy

### Lesson 4.1 — The CSS Reset

Different browsers have different default styles. Chrome might add different margins to headings than Firefox. A **CSS reset** removes all of these differences so you start from the same place everywhere.

Paste this at the very top of your CSS file (before any of your own styles):

```css
/* === RESET — paste this in every project === */

/* 1. Fix the box model for all elements */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* 2. Sensible base for the whole page */
body {
  min-height: 100vh;       /* at least as tall as the screen */
  line-height: 1.6;        /* comfortable reading */
  -webkit-font-smoothing: antialiased; /* smoother text on Mac */
}

/* 3. Images should never overflow their container */
img, video {
  display: block;
  max-width: 100%;
}

/* 4. Form elements should use the same font as the page */
input, button, textarea, select {
  font: inherit;
}

/* 5. Show a visible focus ring when navigating with a keyboard */
:focus-visible {
  outline: 2px solid blue;
  outline-offset: 2px;
}
```

---

### Lesson 4.2 — Organising Your Files

When your project gets bigger, one huge CSS file becomes hard to manage. Split it into smaller files by topic:

```
styles/
├── reset.css         ← the reset above
├── variables.css     ← all your :root CSS variables
├── typography.css    ← fonts and text styles
├── buttons.css       ← button styles
├── cards.css         ← card styles
├── nav.css           ← navigation styles
├── layout.css        ← page layout (header, footer, grid)
└── main.css          ← imports all the above files
```

In `main.css`, import them all in order:

```css
/* main.css */
@import './reset.css';
@import './variables.css';
@import './typography.css';
@import './buttons.css';
@import './cards.css';
@import './nav.css';
@import './layout.css';
```

Then in your HTML, you only need to link one file:

```html
<link rel="stylesheet" href="styles/main.css">
```

> **Why organise this way?** When something looks wrong with a button, you know exactly which file to open. It saves time and makes it easier for others to help you.

---

### Lesson 4.3 — Course Checklist

Before you move on, make sure your bio page does all of these things:

**Basics**
- [ ] `box-sizing: border-box` is at the top of your CSS
- [ ] All colours and sizes are stored as CSS variables in `:root`
- [ ] No messy hardcoded colours typed directly in rules (use `var()`)

**Layout**
- [ ] The page works and looks good on a phone (test in DevTools)
- [ ] Flexbox is used for at least one component (navigation, card row, etc.)
- [ ] CSS Grid is used for at least one layout (card gallery or page structure)

**Visual polish**
- [ ] Buttons and cards have a smooth hover effect with `transition`
- [ ] At least one `@keyframes` animation is used
- [ ] `prefers-reduced-motion` turns off animations for users who need it

**Dark mode**
- [ ] There is a working dark/light toggle button
- [ ] The chosen theme is saved and restored on page refresh

**Files**
- [ ] CSS is split into at least 3 separate files (variables, reset, and components)
- [ ] All files are imported in `main.css`

---

**Final project**

Build a personal bio page from scratch that passes the checklist above. It should include:
1. A navigation bar with your name/logo on the left and links on the right
2. A hero section with your name and a short description, centred on the page
3. A "Skills" or "Hobbies" card grid that reflows on different screen sizes
4. A dark/light mode toggle
5. Hover animations on all cards and buttons

Share your finished page with someone and ask them to resize the browser window. If everything reflows nicely, you've done it!
