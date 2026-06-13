# HTML — Web Fundamentals

## Welcome! What is HTML?

Have you ever seen a house being built? Before the walls go up, before it gets painted, before the furniture goes in — there's a **skeleton** of beams and bricks holding everything in place.

**HTML is the skeleton of every website.** It tells the browser "here is a heading", "here is a paragraph", "here is an image", "here is a button". Without HTML, there is no website.

HTML stands for **HyperText Markup Language**. Don't worry about the fancy name. In simple terms:
- **HyperText** means text that can link to other pages (that's what links are!)
- **Markup** means you "mark up" your content with labels describing what each piece is
- **Language** means it follows rules the browser understands

**The three layers of every website:**

```
HTML  →  The skeleton    (what is on the page?)
CSS   →  The skin/paint  (what does it look like?)
JS    →  The muscles     (what does it do when you interact?)
```

This course is all about HTML — the foundation. You can't do CSS or JavaScript without it.

---

## Module 1 — Your First Web Page

### Lesson 1.1 — Writing Your First HTML File

Let's write a real webpage right now. Open any text editor (VS Code is great), create a file called `index.html`, and type this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <p>I just made a website. This is amazing.</p>
  </body>
</html>
```

Save the file. Now open it in your browser (drag the file into Chrome or double-click it). You should see your heading and paragraph!

**What just happened?** You wrote HTML and the browser read it and turned it into a visible page. That's it. That's web development.

---

**What are those angle brackets?**

Every piece of HTML uses **tags**. A tag is a word wrapped in angle brackets: `< >`.

Most tags come in pairs — an **opening tag** and a **closing tag** (with a `/`):

```html
<h1>This is a heading</h1>
<!--  ↑ opening        ↑ closing (has a forward slash) -->
```

The content goes *between* the two tags. Whatever is between them gets that tag's meaning.

Think of tags like **sandwich bread** — the content is the filling, and the tags are the bread slices on either side.

Some tags don't need a closing tag because they don't wrap around content — they're self-closing:

```html
<img src="photo.jpg" alt="A photo" />
<br />  <!-- a line break -->
<hr />  <!-- a horizontal line -->
```

---

**What goes in `<head>` vs `<body>`?**

Think of your webpage like an iceberg:

- `<head>` is the **part underwater** — information about the page that the browser needs, but the user doesn't see (like the page title, language, links to CSS files)
- `<body>` is the **part above water** — everything the user actually sees on the page

```html
<head>
  <title>My Page</title>  <!-- shows up in the browser tab -->
  <link rel="stylesheet" href="style.css" /> <!-- connects your CSS -->
</head>

<body>
  <h1>This shows on screen!</h1>  <!-- the user sees this -->
</body>
```

---

**HTML comments — notes for yourself**

You can write notes in your HTML that the browser ignores. These are called **comments**:

```html
<!-- This is a comment. The browser skips it. -->

<!-- 
  You can also write
  multi-line comments
  like this
-->

<h1>The browser renders this normally</h1>
```

Use comments to explain what a section does, or to temporarily "hide" some code while testing.

---

**Try it yourself!**

1. Create `index.html` and type the boilerplate from this lesson from memory (don't copy-paste). Open it in your browser and confirm it works.
2. Add a comment above your `<h1>` explaining what the page is about.
3. Change the `<title>` tag to have your name in it. Look at the browser tab — it should show your name!

---

### Lesson 1.2 — The Full HTML Boilerplate

Now let's add all the lines that professional developers include at the start of every HTML file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Page Title — Site Name</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>

    <!-- all your visible content goes here -->

    <script src="script.js"></script>
  </body>
</html>
```

**What does each line do?**

| Line | What it does in plain English |
|---|---|
| `<!DOCTYPE html>` | Tells the browser "this is a modern HTML5 file". Always the very first line. |
| `<html lang="en">` | The root of your entire page. `lang="en"` tells screen readers to speak in English. |
| `<meta charset="UTF-8">` | Lets you use any character — emojis, Arabic, Chinese, accented letters — without them breaking. |
| `<meta name="viewport">` | Without this, phones zoom out to show the desktop version of your site. This keeps it looking right on mobiles. |
| `<title>` | The text that appears in the browser tab and in Google search results. Every page needs a unique title. |
| `<link rel="stylesheet">` | Connects your CSS file so your page gets styled. |
| `<script>` at the bottom | JavaScript goes here — at the bottom, so your HTML loads first before the JS tries to find it. |

> **Why is `<script>` at the bottom?** Imagine building a bookshelf while blindfolded, and someone hands you a book before the shelf exists. That's what happens if JavaScript runs before the HTML is ready. Putting it at the bottom means the HTML is fully built first.

---

**Try it yourself!**

1. Update your `index.html` to include every line from the full boilerplate above.
2. In a browser, right-click on any website and choose "View Page Source". Try to find the `<!DOCTYPE html>`, `<title>`, and the `<meta viewport>` tag. Does the site have them?
3. Change `lang="en"` to `lang="fr"`. What do you think that would do? (It tells the browser and screen readers the page is in French.)

---

### Lesson 1.3 — Headings and Paragraphs

**Headings** are like the titles and subtitles in a book. There are six levels:

```html
<h1>This is the main title (biggest)</h1>
<h2>This is a section title</h2>
<h3>This is a sub-section title</h3>
<h4>This is a smaller sub-section</h4>
<h5>Even smaller</h5>
<h6>The smallest heading</h6>
```

> **Important rule:** Use headings for *structure*, not for making text bigger. If you want big text, use CSS. If something is a major section heading, use `<h2>`. The browser makes headings big by default, but you can change that with CSS.

**The heading hierarchy:**
- One page = **one `<h1>`** (the main title of the whole page)
- Use `<h2>` for major sections
- Use `<h3>` for sub-sections inside those
- Never skip levels! Don't jump from `<h2>` to `<h4>`.

Think of it like a book:
- `<h1>` = the book title
- `<h2>` = chapter name
- `<h3>` = section within a chapter
- `<h4>` = sub-section within a section

---

**Paragraphs** hold your regular text:

```html
<p>This is a paragraph. It can be as long as you want.
   Line breaks in the HTML code don't matter — the browser
   wraps the text based on the screen width.</p>

<p>This is a second paragraph. Notice there's a gap between
   the two paragraphs. That's the browser's default styling.</p>
```

**Other basic text elements:**

```html
<p>This word is <strong>very important</strong> — it's bold.</p>
<p>This word is <em>emphasised</em> — it's italic.</p>
<p>This is <br /> text on a new line. (Use sparingly!)</p>
<hr /> <!-- a horizontal dividing line -->
```

> **`<strong>` vs `<b>`, and `<em>` vs `<i>`:** Both pairs look the same visually, but `<strong>` means "this is important" and `<em>` means "emphasis". Screen readers say these words with different intonation. Use `<strong>` and `<em>` — they carry meaning, not just style.

---

**Try it yourself!**

Build a simple "About Me" page with:
1. An `<h1>` with your name
2. An `<h2>` called "About Me" with a paragraph about yourself
3. An `<h2>` called "My Hobbies" with a few words using `<strong>` and `<em>`
4. An `<h2>` called "My Favourite Quote" with a quote inside a `<p>`

---

## Module 2 — Structuring Your Page Like a Pro

### Lesson 2.1 — Semantic HTML: Giving Your Content Meaning

Look at these two pieces of code:

```html
<!-- Version 1 — no meaning -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main-content">
  <div class="big-title">Welcome</div>
  <div class="paragraph">Some text here.</div>
</div>
<div class="footer">...</div>
```

```html
<!-- Version 2 — with meaning -->
<header>
  <nav>...</nav>
</header>
<main>
  <h1>Welcome</h1>
  <p>Some text here.</p>
</main>
<footer>...</footer>
```

Both versions look identical in the browser. But Version 2 is far better. Here's why:

1. **Screen readers** (used by people who are blind) can jump directly to `<main>` — they don't have to listen to every bit of navigation first
2. **Google** understands that `<nav>` contains navigation links and ranks the page better
3. **You** can read the code months later and immediately understand what each section is

Using the right element for the right job is called **semantic HTML**. "Semantic" just means "meaningful".

---

**The main page-level building blocks:**

| Element | What it's for |
|---|---|
| `<header>` | The top of the page — your logo, site name, and main navigation |
| `<nav>` | A group of navigation links |
| `<main>` | The main content of this specific page (only ONE per page!) |
| `<section>` | A themed chunk of content — should always have a heading |
| `<article>` | Content that makes sense on its own — like a blog post or a card |
| `<aside>` | Side content — like a tip box, a related links panel, or a sidebar |
| `<footer>` | The bottom of the page — copyright, contact info, secondary links |

---

**A real page structure:**

```html
<body>

  <header>
    <a href="/" class="logo">My Website</a>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>

    <section id="hero">
      <h1>Welcome to My Website!</h1>
      <p>I'm learning web development and this is my first site.</p>
    </section>

    <section id="about">
      <h2>About Me</h2>
      <p>I'm 10 years old and I love coding and football.</p>
    </section>

    <section id="hobbies">
      <h2>My Hobbies</h2>

      <article>
        <h3>Football</h3>
        <p>I play for my school team every Saturday.</p>
      </article>

      <article>
        <h3>Coding</h3>
        <p>I've been learning HTML for two weeks!</p>
      </article>
    </section>

  </main>

  <aside>
    <h2>Did You Know?</h2>
    <p>The first website ever made is still online today!</p>
  </aside>

  <footer>
    <p>Made by me in 2025</p>
  </footer>

</body>
```

---

**`<div>` and `<span>` — when there's no semantic option**

Sometimes you need a container just for styling purposes, with no particular meaning. That's what `<div>` (block-level) and `<span>` (inline) are for:

```html
<!-- <div> is a block container with no special meaning -->
<div class="card">
  <h3>Card Title</h3>
  <p>Card content</p>
</div>

<!-- <span> is for styling a bit of text inline -->
<p>My favourite colour is <span class="highlight">blue</span>.</p>
```

> **The rule:** If there's a semantic element that fits (`<section>`, `<article>`, `<header>`, etc.) — use it. Only reach for `<div>` or `<span>` when nothing semantic fits.

---

**Try it yourself!**

1. Rebuild your "About Me" page from Lesson 1.3 using proper semantic elements. Wrap everything in `<header>`, `<main>`, `<section>`, and `<footer>`. Do NOT use a single `<div>` — see if you can avoid it entirely!

2. Visit your favourite website. Right-click → "View Page Source". Look for `<header>`, `<main>`, `<nav>`, `<footer>`, `<article>`. Does it use semantic HTML? Or is it full of `<div>` tags?

---

### Lesson 2.2 — Navigation Menus

Every website needs a navigation menu so visitors can move between pages. Here's how to build one properly:

```html
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/projects">Projects</a></li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

**Why use `<ul>` (a list) for navigation?**

A navigation menu is literally a *list of links*. Screen readers announce it as a list, so people know there are multiple options. Never just stack links without a list:

```html
<!-- WRONG — not a list, confusing for screen readers -->
<nav>
  <a href="/">Home</a>
  <a href="/about">About</a>
</nav>

<!-- RIGHT — it IS a list of links -->
<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

**Showing which page you're on:**

Add `aria-current="page"` to the link for the current page. Screen readers will say "current page" when they reach it:

```html
<ul>
  <li><a href="/" aria-current="page">Home</a></li>  <!-- we're on this page -->
  <li><a href="/about">About</a></li>
</ul>
```

**A dropdown submenu:**

```html
<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li>
      <a href="/courses">Courses</a>
      <ul>  <!-- nested list = dropdown submenu -->
        <li><a href="/courses/html">HTML</a></li>
        <li><a href="/courses/css">CSS</a></li>
        <li><a href="/courses/js">JavaScript</a></li>
      </ul>
    </li>
    <li><a href="/contact">Contact</a></li>
  </ul>
</nav>
```

---

**Try it yourself!**

1. Add a `<nav>` to your bio page with at least 4 links. Use `aria-current="page"` on the Home link.
2. Add a dropdown with 3 sub-links inside one of your nav items. Just the HTML — we'll style it with CSS later.

---

## Module 3 — Working with Content

### Lesson 3.1 — Links: Connecting the Web

Links are what make the web a *web*. Without links, every page would be a dead end.

**Basic link:**

```html
<a href="https://www.google.com">Go to Google</a>
<!--  ↑ href = where to go       ↑ link text the user sees -->
```

`href` stands for **Hypertext Reference** — basically, the address to go to.

**Types of links:**

```html
<!-- 1. External — goes to another website -->
<!-- Always add target and rel for security (explained below) -->
<a href="https://developer.mozilla.org" target="_blank" rel="noopener noreferrer">
  MDN Web Docs
</a>

<!-- 2. Internal — goes to another page on YOUR site -->
<a href="/about">About Me</a>
<a href="/projects/game.html">My Game Project</a>

<!-- 3. Anchor — jumps to a section on the SAME page -->
<a href="#contact">Jump to Contact Section</a>
<!-- ... further down the page ... -->
<section id="contact">
  <h2>Contact Me</h2>
</section>

<!-- 4. Email — opens the user's email app -->
<a href="mailto:me@example.com">Send me an email</a>

<!-- 5. Phone — on mobile, offers to call the number -->
<a href="tel:+2348001234567">Call us</a>

<!-- 6. Download — saves a file instead of opening it -->
<a href="/files/resume.pdf" download="My-Resume.pdf">Download my CV</a>
```

---

**Why `target="_blank"` needs `rel="noopener noreferrer"`**

When you add `target="_blank"`, the link opens in a new tab. But there's a sneaky security problem — the new tab can secretly access your page and redirect it somewhere else.

Adding `rel="noopener noreferrer"` blocks this completely. Always add it on external links:

```html
<!-- WRONG — security risk -->
<a href="https://example.com" target="_blank">Visit site</a>

<!-- RIGHT — safe -->
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Visit site</a>
```

---

**Back to top link:**

```html
<!-- At the bottom of your page -->
<a href="#top">Back to top</a>

<!-- At the very top of <body> -->
<body id="top">
```

---

**Try it yourself!**

Add a navigation bar to your bio page with:
1. A home link (`href="/"`)
2. An internal link to a "Projects" section on your page using an anchor (`href="#projects"`)
3. An external link to your favourite website (with `target="_blank"` and `rel="noopener noreferrer"`)
4. A "Back to top" link at the bottom

---

### Lesson 3.2 — Images: Adding Pictures

Images make pages come alive. Here's how to use them properly:

```html
<!-- Basic image -->
<img src="my-photo.jpg" alt="Me smiling at the camera" />
```

`<img>` is self-closing (no `</img>` needed). It has two important attributes:
- `src` — the **source** (where the image file is)
- `alt` — the **alternative text** (a description of the image)

---

**Alt text — why it matters**

The `alt` attribute describes the image to:
- People who are blind (their screen reader reads the alt text out loud)
- People on slow internet (image hasn't loaded yet)
- Search engines (they can't "see" images)

**How to write good alt text:**

```html
<!-- Describe WHAT IS HAPPENING, not just what you see -->
<img src="dog.jpg" alt="A golden retriever jumping to catch a frisbee in a park" />

<!-- For logos, describe the company name -->
<img src="logo.png" alt="Nike logo" />

<!-- For chart/diagram, describe the key insight -->
<img src="chart.png" alt="Bar chart showing HTML is used by 95% of all websites" />

<!-- For a purely decorative image (background pattern, divider) — empty alt -->
<!-- Screen readers will skip it entirely -->
<img src="pattern.svg" alt="" />

<!-- WRONG — never leave alt out entirely -->
<img src="photo.jpg" />
```

---

**Controlling image size:**

```html
<!-- Always set width and height — prevents "layout shift" (page jumping around as images load) -->
<img src="photo.jpg" alt="A photo" width="400" height="300" />
```

> **What is layout shift?** When you open a page on slow internet, you start reading. Then an image loads, pushes everything down, and you lose your place. Setting `width` and `height` reserves the space in advance so nothing jumps around.

---

**Images with captions:**

```html
<!-- <figure> groups an image with its caption -->
<figure>
  <img src="eiffel-tower.jpg" alt="The Eiffel Tower lit up at night in Paris" width="600" height="400" />
  <figcaption>The Eiffel Tower in Paris, France — built in 1889</figcaption>
</figure>
```

**Clickable image (image inside a link):**

```html
<!-- When inside a link, the alt text describes where the link goes -->
<a href="/">
  <img src="logo.png" alt="Go to the homepage" />
</a>
```

---

**Try it yourself!**

1. Add 3 images to your bio page. Write meaningful alt text for each.
2. Put one image inside a `<figure>` with a `<figcaption>`.
3. Make your logo a clickable link back to the homepage.
4. Cover your screen, have someone else read your alt text — can they picture what the images show?

---

### Lesson 3.3 — Lists: Organising Information

There are three types of lists in HTML. Choosing the right one matters.

**1. Unordered list `<ul>` — when order doesn't matter**

```html
<!-- A shopping list — you don't care what order you buy things in -->
<ul>
  <li>Apples</li>
  <li>Bread</li>
  <li>Orange juice</li>
  <li>Cheese</li>
</ul>
```

Use `<ul>` for: ingredients, feature lists, navigation menus, tag clouds.

---

**2. Ordered list `<ol>` — when the order matters**

```html
<!-- A recipe — you MUST do these in order -->
<ol>
  <li>Boil water in a pot.</li>
  <li>Add pasta and cook for 10 minutes.</li>
  <li>Drain the water.</li>
  <li>Add sauce and stir.</li>
  <li>Serve and enjoy!</li>
</ol>
```

Use `<ol>` for: step-by-step instructions, rankings, numbered steps, table of contents.

---

**3. Description list `<dl>` — for terms and definitions**

```html
<!-- A glossary of HTML terms -->
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language — the skeleton of web pages.</dd>

  <dt>CSS</dt>
  <dd>Cascading Style Sheets — controls how web pages look.</dd>

  <dt>JavaScript</dt>
  <dd>The programming language that makes web pages interactive.</dd>
</dl>
```

Use `<dl>` for: glossaries, FAQs, dictionaries, metadata.

---

**Nested lists — a list inside a list:**

```html
<ul>
  <li>Web Fundamentals
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>React</li>
  <li>Backend Development</li>
</ul>
```

---

**Quick guide — which list type to use?**

| Situation | List type |
|---|---|
| Navigation links | `<ul>` |
| Ingredients | `<ul>` |
| Step-by-step instructions | `<ol>` |
| How-to guide | `<ol>` |
| Glossary or FAQ answers | `<dl>` |
| Search results | `<ol>` |

---

**Try it yourself!**

1. Add an "About Me" section with a `<ul>` of 5 facts about yourself.
2. Add a "How To Make My Favourite Food" section with an `<ol>` of recipe steps.
3. Add a "Glossary" section with a `<dl>` defining 3 web development terms.

---

### Lesson 3.4 — Tables: Showing Data in Rows and Columns

Tables are for **data that naturally belongs in a grid** — like a school timetable, a comparison chart, or sports statistics.

> **Important:** Tables are NOT for page layout! In the early internet, developers used tables to arrange the whole page. Don't do this — use CSS for layout instead.

**A basic table:**

```html
<table>
  <caption>My Weekly Timetable</caption>  <!-- a title for the table -->

  <thead>  <!-- the header row -->
    <tr>
      <th scope="col">Time</th>
      <th scope="col">Monday</th>
      <th scope="col">Tuesday</th>
      <th scope="col">Wednesday</th>
    </tr>
  </thead>

  <tbody>  <!-- the data rows -->
    <tr>
      <th scope="row">9:00 AM</th>
      <td>Maths</td>
      <td>English</td>
      <td>Science</td>
    </tr>
    <tr>
      <th scope="row">10:00 AM</th>
      <td>Science</td>
      <td>Art</td>
      <td>Maths</td>
    </tr>
    <tr>
      <th scope="row">11:00 AM</th>
      <td>English</td>
      <td>PE</td>
      <td>History</td>
    </tr>
  </tbody>

  <tfoot>  <!-- optional summary row at the bottom -->
    <tr>
      <td colspan="4">3 lessons per day</td>
    </tr>
  </tfoot>
</table>
```

**Breaking down the new tags:**

| Tag | What it does |
|---|---|
| `<table>` | Wraps the whole table |
| `<caption>` | A title/description for the table (like `alt` for images) |
| `<thead>` | Groups the header row(s) |
| `<tbody>` | Groups the data rows |
| `<tfoot>` | Groups the footer row(s) — totals, summaries |
| `<tr>` | A table **row** |
| `<th>` | A table **header** cell — bold and centred by default |
| `<td>` | A regular table **data** cell |
| `scope="col"` | Tells screen readers this `<th>` is a header for a column |
| `scope="row"` | Tells screen readers this `<th>` is a header for a row |

**Merging cells:**

```html
<!-- colspan: cell takes up 2 columns -->
<td colspan="2">This spans two columns</td>

<!-- rowspan: cell takes up 3 rows -->
<td rowspan="3">This spans three rows</td>
```

---

**Try it yourself!**

1. Build your school timetable as an HTML table. Use `<thead>`, `<tbody>`, `<tfoot>`, and a `<caption>`.
2. Add `scope="col"` to the day-of-week headers and `scope="row"` to the time headers.
3. If your school has a free period that spans two subjects, use `colspan` to merge those cells.

---

### Lesson 3.5 — Inline Elements: Styling Text With Meaning

These elements go *inside* paragraphs to add meaning to specific words:

```html
<!-- Strong importance — makes text bold -->
<p>You <strong>must</strong> submit before midnight.</p>

<!-- Emphasis — makes text italic -->
<p>The exam is <em>tomorrow</em>, not next week!</p>

<!-- Inline code — for code snippets inside text -->
<p>To save in VS Code, press <code>Ctrl + S</code>.</p>

<!-- Keyboard key — wraps keyboard shortcut keys -->
<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.</p>

<!-- Abbreviation — expands on hover -->
<p><abbr title="HyperText Markup Language">HTML</abbr> is the skeleton of the web.</p>

<!-- Deleted and inserted text — show changes -->
<p>The price is <del>$50</del> <ins>$30</ins> today only!</p>

<!-- Superscript and subscript -->
<p>E = mc<sup>2</sup></p>       <!-- superscript: above the line -->
<p>Water is H<sub>2</sub>O</p>  <!-- subscript: below the line -->

<!-- Time — machine-readable date/time -->
<p>The event starts on <time datetime="2025-12-25">Christmas Day</time>.</p>

<!-- Mark — highlighted text, like a yellow marker -->
<p>The most important part is <mark>this highlighted bit</mark>.</p>
```

> **`<strong>` is not the same as `<b>`.** Both look bold, but `<strong>` means "this is important" — screen readers will change their voice. `<b>` just makes text bold with no extra meaning. Use `<strong>`. Same idea for `<em>` vs `<i>`.

---

**Blockquotes:**

```html
<!-- A long quote from someone else -->
<blockquote>
  <p>"The best way to learn to code is to build things you actually want to use."</p>
  <footer>— Unknown</footer>
</blockquote>
```

---

**Try it yourself!**

Write a paragraph about your favourite book or movie. Include at least 5 different inline elements used *naturally* — not forced. For example, use `<strong>` on the character's name because they're truly the most important part of the story, not just to make it bold.

---

## Module 4 — Forms: Collecting Information

### Lesson 4.1 — What is a Form?

A form is how websites collect information from you. When you sign up for an account, search on Google, buy something online, or log in — you're using a form.

Think of an HTML form like a paper form at the doctor's office. It has blank boxes you fill in, questions you answer, and a submit button at the end.

```html
<form action="/submit" method="POST">

  <!-- form fields go here -->

  <button type="submit">Submit</button>
</form>
```

The two important attributes:
- `action` — where to *send* the form data when submitted (a URL on your server)
- `method` — how to send it:
  - `POST` — for creating or changing data (signing up, logging in, sending a message)
  - `GET` — for searching (the data goes in the URL: `google.com/search?q=html`)

---

**The most important rule about forms: always use labels!**

Every input field needs a label. Without a label:
- Clicking the label text won't focus the input
- Screen readers won't know what the field is for
- The form is much harder to use on mobile

```html
<!-- WRONG — no label -->
<input type="text" placeholder="Enter your name" />

<!-- RIGHT — label is connected to the input via matching for and id -->
<label for="name">Your name</label>
<input type="text" id="name" name="name" />
```

When `for` matches `id`, clicking the label text focuses the input. On a checkbox, this doubles the click area — much easier to tap on a phone!

---

**Grouping related fields with `<fieldset>` and `<legend>`:**

```html
<form>
  <fieldset>
    <legend>Your Personal Details</legend>

    <div>
      <label for="first-name">First name</label>
      <input type="text" id="first-name" name="firstName" required />
    </div>

    <div>
      <label for="last-name">Last name</label>
      <input type="text" id="last-name" name="lastName" required />
    </div>
  </fieldset>

  <fieldset>
    <legend>Choose Your Plan</legend>

    <label>
      <input type="radio" name="plan" value="free" checked />
      Free — basic access
    </label>

    <label>
      <input type="radio" name="plan" value="pro" />
      Pro — $10/month
    </label>
  </fieldset>

  <button type="submit">Sign Up</button>
</form>
```

`<fieldset>` draws a border around a group of related fields. `<legend>` gives it a title — like a heading for that group.

---

**Try it yourself!**

1. Build a "Contact Me" form with: name, email, and a message. Every field must have a proper `<label>`. Add a Submit button.
2. Notice that clicking the label text on your fields now focuses the input. Try it!

---

### Lesson 4.2 — All the Different Input Types

The `type` attribute on an `<input>` completely changes what it looks like and what it does:

**Text inputs:**

```html
<!-- Regular text: anything goes -->
<input type="text" name="username" placeholder="Enter a username" />

<!-- Email: browser validates it looks like an email -->
<input type="email" name="email" placeholder="you@example.com" />

<!-- Password: text is hidden with dots/stars -->
<input type="password" name="password" placeholder="Min. 8 characters" />

<!-- Phone number: on mobile, shows the numeric keypad -->
<input type="tel" name="phone" placeholder="+234 800 123 4567" />

<!-- Website URL -->
<input type="url" name="website" placeholder="https://mysite.com" />

<!-- Search field (adds a clear/× button in some browsers) -->
<input type="search" name="q" placeholder="Search..." />
```

**Number inputs:**

```html
<!-- A number spinner — only allows numbers -->
<input type="number" name="age" min="5" max="120" step="1" />

<!-- A slider from 0 to 100 -->
<input type="range" name="volume" min="0" max="100" value="50" />
```

**Date and time:**

```html
<!-- A calendar date picker -->
<input type="date" name="birthday" />

<!-- A time picker -->
<input type="time" name="appointment" />

<!-- Date AND time -->
<input type="datetime-local" name="event-start" />
```

**Choices:**

```html
<!-- Checkbox — tick one or more -->
<label>
  <input type="checkbox" name="newsletter" value="yes" />
  Sign me up for the newsletter
</label>

<!-- Radio buttons — pick exactly one from a group -->
<!-- All options in a group share the same "name" -->
<label>
  <input type="radio" name="colour" value="red" />
  Red
</label>
<label>
  <input type="radio" name="colour" value="blue" />
  Blue
</label>
<label>
  <input type="radio" name="colour" value="green" />
  Green
</label>
```

**File uploads:**

```html
<!-- Upload a single image -->
<input type="file" name="photo" accept="image/*" />

<!-- Upload multiple PDF files -->
<input type="file" name="documents" accept=".pdf" multiple />
```

**Multi-line text (not an `<input>`):**

```html
<!-- A large text box — for messages, bios, descriptions -->
<textarea name="message" rows="5" placeholder="Write your message here..."></textarea>
```

**Dropdown menu (not an `<input>`):**

```html
<select name="country">
  <option value="">Choose your country</option>

  <!-- optgroup groups related options with a header -->
  <optgroup label="West Africa">
    <option value="NG">Nigeria</option>
    <option value="GH">Ghana</option>
    <option value="SL">Sierra Leone</option>
  </optgroup>

  <optgroup label="East Africa">
    <option value="KE">Kenya</option>
    <option value="ET">Ethiopia</option>
  </optgroup>
</select>
```

---

**Validation attributes — making fields required:**

```html
<!-- required: field must be filled in before submitting -->
<input type="text" name="name" required />

<!-- minlength / maxlength: text length limits -->
<input type="text" name="username" required minlength="3" maxlength="20" />

<!-- min / max for numbers and dates -->
<input type="number" name="score" min="0" max="100" />
<input type="date" name="birthday" max="2015-01-01" />

<!-- pattern: must match a specific format (advanced) -->
<input type="text" name="postcode"
       pattern="[A-Z]{2}[0-9]{1,2} [0-9][A-Z]{2}"
       title="UK postcode format, e.g. SW1A 1AA" />
```

---

**Try it yourself!**

Build a "Book a Slot" form with:
1. Name (`type="text"`, required)
2. Email (`type="email"`, required)
3. Phone (`type="tel"`, optional)
4. Preferred date (`type="date"`, only future dates — set `min` to today)
5. Time slot (a `<select>` with Morning, Afternoon, Evening options)
6. Extra notes (`<textarea>`, optional)
7. A "Terms and Conditions" checkbox (required)
8. A Submit button

---

### Lesson 4.3 — A Complete Registration Form

Let's put everything together in a full, real-world form:

```html
<form id="signup-form" novalidate>

  <fieldset>
    <legend>Create Your Account</legend>

    <div class="field">
      <label for="full-name">Full name</label>
      <input
        type="text"
        id="full-name"
        name="fullName"
        required
        minlength="2"
        autocomplete="name"
        aria-describedby="name-error"
      />
      <p id="name-error" class="error" role="alert" hidden>
        Please enter your full name.
      </p>
    </div>

    <div class="field">
      <label for="email">Email address</label>
      <input
        type="email"
        id="email"
        name="email"
        required
        autocomplete="email"
        aria-describedby="email-error"
      />
      <p id="email-error" class="error" role="alert" hidden>
        Please enter a valid email address.
      </p>
    </div>

    <div class="field">
      <label for="password">Password</label>
      <input
        type="password"
        id="password"
        name="password"
        required
        minlength="8"
        autocomplete="new-password"
        aria-describedby="password-hint password-error"
      />
      <p id="password-hint" class="hint">Must be at least 8 characters.</p>
      <p id="password-error" class="error" role="alert" hidden>
        Password must be at least 8 characters.
      </p>
    </div>
  </fieldset>

  <fieldset>
    <legend>Choose Your Plan</legend>

    <label class="radio-option">
      <input type="radio" name="plan" value="free" checked />
      Free — read-only access
    </label>

    <label class="radio-option">
      <input type="radio" name="plan" value="basic" />
      Basic — $5/month
    </label>

    <label class="radio-option">
      <input type="radio" name="plan" value="pro" />
      Pro — $15/month
    </label>
  </fieldset>

  <div class="field">
    <label for="bio">Short bio <span class="optional">(optional, max 200 characters)</span></label>
    <textarea
      id="bio"
      name="bio"
      rows="4"
      maxlength="200"
      aria-describedby="bio-count"
      placeholder="Tell us a little about yourself..."
    ></textarea>
    <p id="bio-count" class="hint"><span id="chars-left">200</span> characters left</p>
  </div>

  <div class="field">
    <label class="checkbox-label">
      <input type="checkbox" name="terms" id="terms" required />
      I agree to the <a href="/terms">Terms and Conditions</a>
    </label>
  </div>

  <button type="submit">Create Account</button>
</form>
```

**New things here:**
- `novalidate` on the form — turns off the browser's built-in validation so we can control it ourselves with JavaScript
- `autocomplete` — helps browsers pre-fill fields the user has typed before
- `aria-describedby` — links an input to its error message or hint text (so screen readers read both)
- `role="alert"` — tells screen readers to announce the error immediately when it appears
- `hidden` — hides the error message until validation fails

---

**Try it yourself!**

1. Build the complete form above. Style it with CSS to make it look clean (labels above inputs, inputs with a border, submit button with a background colour).
2. Navigate through the form using only your keyboard (Tab to move forward, Shift+Tab to move back, Space to toggle checkboxes, arrow keys for radio buttons).

---

## Module 5 — Media: Audio, Video and Embedding

### Lesson 5.1 — Adding Video to Your Page

HTML5 has built-in support for video — no plugins or Flash required!

```html
<video controls width="640" height="360">
  <!-- Multiple formats for browser compatibility -->
  <source src="my-video.mp4"  type="video/mp4" />
  <source src="my-video.webm" type="video/webm" />
  <!-- Fallback for browsers that don't support video -->
  <p>Your browser doesn't support video. <a href="my-video.mp4">Download it here</a>.</p>
</video>
```

**The `controls` attribute** adds the play/pause button, volume slider, and timeline. Without it, the video has no controls.

**Other video attributes:**

```html
<video
  controls
  width="640"
  height="360"
  autoplay      <!-- plays automatically (use sparingly — can be annoying!) -->
  muted         <!-- starts muted (required for autoplay in most browsers) -->
  loop          <!-- plays again when it finishes -->
  poster="thumbnail.jpg"  <!-- shows this image before the video plays -->
>
  <source src="intro.mp4" type="video/mp4" />
</video>
```

> **Accessibility tip:** If your video has speech or important sounds, add subtitles. The `<track>` element adds captions:

```html
<video controls width="640" height="360">
  <source src="lesson.mp4" type="video/mp4" />
  <track kind="subtitles" src="subtitles-en.vtt" srclang="en" label="English" default />
</video>
```

---

### Lesson 5.2 — Adding Audio to Your Page

```html
<audio controls>
  <source src="song.mp3"  type="audio/mpeg" />
  <source src="song.ogg"  type="audio/ogg" />
  <p>Your browser doesn't support audio. <a href="song.mp3">Download it</a>.</p>
</audio>
```

Audio attributes work the same as video:

```html
<audio controls loop autoplay muted>
  <source src="background-music.mp3" type="audio/mpeg" />
</audio>
```

---

### Lesson 5.3 — Embedding Content with `<iframe>`

`<iframe>` (inline frame) lets you embed another webpage or tool inside yours. This is how you embed YouTube videos, Google Maps, and other third-party content:

**Embedding a YouTube video:**

```html
<!-- Go to YouTube → Share → Embed → copy the src URL -->
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/dQw4w9WgXcQ"
  title="YouTube video player"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope"
  allowfullscreen
></iframe>
```

**Embedding a Google Map:**

```html
<!-- Go to Google Maps → Share → Embed a map → copy the src URL -->
<iframe
  src="https://www.google.com/maps/embed?pb=..."
  width="600"
  height="450"
  style="border:0;"
  allowfullscreen
  loading="lazy"
  title="Our location on Google Maps"
></iframe>
```

> **Always include `title` on iframes** — screen readers need it to tell users what's inside.

---

**Try it yourself!**

1. Find a YouTube video about HTML or web development. Embed it on your page using `<iframe>`.
2. Add `<audio controls>` with a free audio file (search "free music for websites" — many sites offer royalty-free tracks).

---

## Module 6 — Accessibility: Making Websites for Everyone

### Lesson 6.1 — What is Accessibility and Why Does It Matter?

About 1 in 4 people live with some kind of disability. That includes:
- People who are **blind** — they use screen readers that read the page out loud
- People who are **deaf** — they need captions on videos
- People with **mobility difficulties** — they navigate using a keyboard only (no mouse)
- People with **colour blindness** — certain colour combinations are invisible to them
- People with **dyslexia** — certain fonts and spacing are very hard to read

When you build an accessible website, it works for *everyone*. And good news — semantic HTML already gives you a huge head start!

**Four principles of accessible design (POUR):**

1. **Perceivable** — can everyone see or hear the content?
2. **Operable** — can everyone navigate and use the controls?
3. **Understandable** — is the content clear to everyone?
4. **Robust** — does it work with different devices and tools?

---

### Lesson 6.2 — Using Native HTML for Accessibility

The single most powerful thing you can do for accessibility is **use the right HTML element**:

```html
<!-- WRONG — a div that looks like a button -->
<!-- Can't be reached by Tab key, not announced as a button -->
<div class="btn" onclick="doSomething()">Click me</div>

<!-- RIGHT — a real button -->
<!-- Automatically keyboard-focusable, announced as "Click me, button" -->
<button type="button" onclick="doSomething()">Click me</button>
```

```html
<!-- WRONG — a div that looks like a link -->
<div onclick="location.href='/about'">About</div>

<!-- RIGHT — a real link -->
<a href="/about">About</a>
```

Native HTML elements come with built-in keyboard support, roles, and announcements. A `<button>` can be pressed with Enter or Space. An `<a>` can be followed with Enter. A `<input>` can be typed in. You get all this for free by using the right element.

---

### Lesson 6.3 — ARIA: When HTML Isn't Enough

**ARIA** (Accessible Rich Internet Applications) adds extra information for screen readers when HTML alone isn't enough.

**The most useful ARIA attributes:**

```html
<!-- aria-label: gives a name to something with no visible text -->
<!-- An icon-only button would be useless to a screen reader without this -->
<button aria-label="Close menu">✕</button>
<button aria-label="Search">🔍</button>

<!-- aria-current: tells screen readers which item is "active" -->
<nav>
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<!-- aria-expanded: for menus/accordions — is it open or closed? -->
<button aria-expanded="false" aria-controls="dropdown-menu">
  Menu
</button>
<ul id="dropdown-menu" hidden>
  <li><a href="/courses">Courses</a></li>
</ul>

<!-- aria-describedby: links an input to its hint or error text -->
<input type="email" id="email" aria-describedby="email-hint" />
<p id="email-hint">We will never share your email.</p>

<!-- role="alert": announces a message immediately to screen readers -->
<p role="alert">Error: your password is too short.</p>

<!-- aria-hidden: hides something from screen readers entirely -->
<!-- Good for decorative icons when there's also visible text -->
<button>
  <span aria-hidden="true">🗑️</span>
  Delete item
</button>
```

> **The ARIA rule:** Only use ARIA when native HTML doesn't do the job. Don't add `role="button"` to a `<div>` — just use a `<button>`.

---

### Lesson 6.4 — Keyboard Navigation

Every user should be able to use your website with only a keyboard. This is essential for:
- People who can't use a mouse
- Power users who are faster with keyboard shortcuts
- Screen reader users (they navigate via keyboard)

**Test your page right now:**
1. Click somewhere on your page
2. Press **Tab** to move to the next focusable element
3. Press **Shift + Tab** to go back
4. Press **Enter** or **Space** on a button to activate it
5. Press **Enter** on a link to follow it

Can you reach everything? Can you activate everything? If not, something is wrong.

---

**Focus rings — never hide them!**

When an element is focused (selected by keyboard), browsers show a visible ring around it. Some developers hide this ring because they think it looks ugly — but that makes the page unusable for keyboard users.

```css
/* NEVER DO THIS */
:focus { outline: none; }

/* DO THIS INSTEAD — style it nicely, but keep it visible */
:focus-visible {
  outline: 2px solid blue;
  outline-offset: 3px;
}
```

---

**Skip navigation link:**

Imagine being blind and using a screen reader. Every time you visit a page, you have to listen to the entire navigation menu before you can get to the content. A "skip" link lets you jump over the navigation:

```html
<!-- This is the FIRST thing in <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<header>
  <nav>... lots of navigation links ...</nav>
</header>

<main id="main-content">
  <!-- The user jumps straight here -->
  <h1>Page title</h1>
</main>
```

```css
.skip-link {
  position: absolute;
  top: -100%;          /* hidden off-screen by default */
}

.skip-link:focus {
  top: 0;              /* appears when focused by keyboard */
  /* style it so it's visible */
  background: blue;
  color: white;
  padding: 8px 16px;
}
```

---

**Try it yourself!**

1. Add a skip-navigation link to your bio page. Test it by pressing Tab as the very first action when the page loads — the skip link should appear.
2. Navigate your entire page using only Tab, Shift+Tab, Enter, and Space. Write down every element you couldn't reach or activate, and fix each one.
3. Find the icon-only buttons on your page (if any) and add `aria-label` to each.

---

### Lesson 6.5 — Colour Contrast and Text Readability

Colour contrast is how different the text colour is from the background colour. Low contrast (like light grey text on a white background) is very hard to read — especially for people with visual impairments or in bright sunlight.

**The rules (WCAG AA standards):**
- Normal text (under 18px): contrast ratio of at least **4.5:1**
- Large text (18px or bigger): at least **3:1**
- Icons and UI borders: at least **3:1**

A contrast ratio of 4.5:1 means the foreground colour is 4.5× brighter/darker than the background.

**How to check contrast:**
1. Open Chrome DevTools (right-click → Inspect)
2. Click on an element with text
3. Click the colour square in the Styles panel
4. A contrast ratio appears — check it passes

**Quick guide:**
- Black `#000000` on white `#FFFFFF` = 21:1 (perfect)
- Dark grey `#333333` on white = 12.6:1 (great)
- Medium grey `#767676` on white = 4.5:1 (passes AA)
- Light grey `#AAAAAA` on white = 2.3:1 (FAILS — don't use this!)

---

**Try it yourself!**

1. Check every text/background combination on your bio page using Chrome DevTools.
2. Fix any that fail the 4.5:1 ratio for normal text.
3. Make sure all your placeholder text has enough contrast too (it often fails!).

---

## Module 7 — Best Practices and Quality Checks

### Lesson 7.1 — Common HTML Mistakes (and How to Avoid Them)

Here are the most common mistakes beginners make:

**1. Using `<div>` for everything (divitis)**

```html
<!-- WRONG -->
<div class="header">
  <div class="nav">
    <div class="nav-item"><a href="/">Home</a></div>
  </div>
</div>

<!-- RIGHT -->
<header>
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
    </ul>
  </nav>
</header>
```

---

**2. Missing `alt` on images**

```html
<!-- WRONG -->
<img src="logo.png" />

<!-- RIGHT -->
<img src="logo.png" alt="My Website logo" />
```

---

**3. Using headings for size, not structure**

```html
<!-- WRONG — using <h4> because it "looks right" visually -->
<h4>This is actually a major section heading</h4>

<!-- RIGHT — use CSS to change the size, use the right heading for the structure -->
<h2 class="large-heading">This is a major section heading</h2>
```

---

**4. No label on form inputs**

```html
<!-- WRONG -->
<input type="email" placeholder="Enter your email" />

<!-- RIGHT -->
<label for="email">Email address</label>
<input type="email" id="email" name="email" placeholder="you@example.com" />
```

---

**5. Using `<br>` for spacing**

```html
<!-- WRONG — using <br> to add gaps between paragraphs -->
<p>First paragraph.</p>
<br />
<br />
<p>Second paragraph.</p>

<!-- RIGHT — use CSS margin for spacing -->
<p>First paragraph.</p>
<p>Second paragraph.</p>
```

```css
p { margin-bottom: 24px; }
```

---

**6. Skipping heading levels**

```html
<!-- WRONG — skips from h2 to h4 -->
<h2>Section</h2>
<h4>Sub-section</h4>

<!-- RIGHT — use levels in order -->
<h2>Section</h2>
<h3>Sub-section</h3>
```

---

**7. External links without `rel`**

```html
<!-- WRONG — security risk -->
<a href="https://example.com" target="_blank">Visit</a>

<!-- RIGHT -->
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Visit</a>
```

---

**8. Duplicate `id` values**

```html
<!-- WRONG — two elements with the same id -->
<section id="about">...</section>
<div id="about">...</div>

<!-- RIGHT — every id must be unique on the page -->
<section id="about">...</section>
<div id="about-sidebar">...</div>
```

---

### Lesson 7.2 — Validating Your HTML

A **validator** is a tool that checks your HTML for mistakes. It's like a spell-checker for code.

The official HTML validator is at **validator.w3.org**.

1. Go to validator.w3.org
2. Click "Validate by Direct Input"
3. Paste your HTML code
4. Click Check

It will tell you every error and warning. Fix them all, run it again, and keep going until you see "Document checking completed. No errors or warnings to show."

**What the validator catches:**
- Missing `alt` attributes on images
- Missing `</` closing tags
- Invalid nesting (like a `<p>` inside a `<p>`)
- Duplicate `id` values
- Missing `lang` attribute on `<html>`
- Typos in attribute names

---

### Lesson 7.3 — The Professional HTML Checklist

Before you consider a page "done", run through this checklist:

**Document structure**
- [ ] `<!DOCTYPE html>` is the very first line
- [ ] `<html>` has a `lang` attribute (e.g. `lang="en"`)
- [ ] `<meta charset="UTF-8">` is inside `<head>`
- [ ] `<meta name="viewport">` is inside `<head>`
- [ ] There is a descriptive `<title>` tag
- [ ] CSS is linked in `<head>`, JavaScript is linked at the bottom of `<body>`

**Semantic structure**
- [ ] Page uses `<header>`, `<nav>`, `<main>`, `<footer>`
- [ ] There is exactly ONE `<h1>` on the page
- [ ] Heading levels are in order — no skipped levels
- [ ] No unnecessary `<div>` or `<span>` tags (use semantic elements where possible)
- [ ] Navigation uses `<ul>` and `<li>`

**Images and media**
- [ ] Every `<img>` has an `alt` attribute (even if empty for decorative images)
- [ ] `<video>` and `<audio>` have `controls`
- [ ] `<iframe>` has a `title` attribute
- [ ] Images have `width` and `height` to prevent layout shift

**Links**
- [ ] External links have `rel="noopener noreferrer"`
- [ ] Navigation links use `aria-current="page"` for the active page
- [ ] "Back to top" and anchor links work correctly

**Forms**
- [ ] Every input has a connected `<label>` (matching `for` and `id`)
- [ ] Related fields are grouped with `<fieldset>` and `<legend>`
- [ ] Radio button groups share the same `name` attribute
- [ ] Error messages use `role="alert"` and `aria-describedby`

**Accessibility**
- [ ] Page has a skip-navigation link
- [ ] Tab through the whole page — every element is reachable
- [ ] Focus rings are visible (not hidden with `outline: none`)
- [ ] Icon-only buttons have `aria-label`
- [ ] All text meets WCAG AA colour contrast (4.5:1 for normal text)

**Validation**
- [ ] W3C Validator reports zero errors
- [ ] No duplicate `id` values on the page
- [ ] All tags are properly closed and correctly nested

---

### Lesson 7.4 — The Final Project

You've learned a huge amount. Now put it all together.

**Build a complete "About Me" website** with three pages:

---

**Page 1: `index.html` — Home Page**

- Full HTML boilerplate
- `<header>` with your name/logo and a `<nav>` linking to all three pages
- Skip-navigation link
- `<main>` with:
  - A hero `<section>` with an `<h1>`, a short description, and a photo of yourself
  - An "About Me" `<section>` with a few paragraphs, using `<strong>` and `<em>` naturally
  - A "Hobbies" `<section>` with `<article>` elements for each hobby
- `<aside>` with a fun fact or quote in a `<blockquote>`
- `<footer>` with copyright text and a "Back to top" link

---

**Page 2: `projects.html` — Projects Page**

- Same header/footer as Page 1
- A grid of project cards, each an `<article>`:
  - A screenshot or placeholder image (with `alt` text)
  - Project name as an `<h3>`
  - A short description
  - A link to see it live and a link to the code
- A `<table>` comparing your projects (e.g. language used, difficulty, time to build)

---

**Page 3: `contact.html` — Contact Page**

- Same header/footer as Page 1
- A complete contact form with:
  - Name (text, required)
  - Email (email, required)
  - Subject (select with at least 4 options)
  - Message (textarea, required, max 500 characters with live counter)
  - A "How did you find me?" radio group
  - Terms agreement checkbox
  - Submit button

---

**Requirements:**
- All 3 pages pass the W3C Validator with zero errors
- Complete checklist passes on all 3 pages
- Navigating with only a keyboard works on every page
- All images have meaningful alt text

This project is the foundation everything else in the course builds on. Take your time and do it properly!
