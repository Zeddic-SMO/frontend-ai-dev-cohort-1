# HTML — Web Fundamentals

HTML (HyperText Markup Language) gives every web page its structure and meaning. Before any styling or interactivity exists, HTML describes what the content *is* — a heading, a paragraph, a navigation link, a form. This course takes you from writing your first valid document all the way to building fully accessible, validated HTML that meets professional standards.

## Module 1 — Document Foundations

Write a correct, well-structured HTML5 document and understand why every line exists.

### Lesson 1.1 — What is HTML and How Does the Browser Use It?

HTML answers one question: **what is this content?** It is not responsible for how content looks (CSS) or how it behaves (JavaScript). When you write `<h1>Hello</h1>`, you are declaring "this text is the most important heading on this page." The browser, screen readers, and search engines all read that declaration and act on it differently.

**The three-layer model:**

```
HTML  →  Structure and meaning  ("what is it?")
CSS   →  Visual presentation    ("what does it look like?")
JS    →  Behaviour              ("what does it do?")
```

**How the browser builds the page:**

1. Downloads the HTML file
2. Parses it top to bottom, building the **DOM** (Document Object Model) — a tree of elements
3. Encounters a `<link>` tag → downloads CSS → builds the **CSSOM**
4. Combines DOM + CSSOM into a **Render Tree**
5. Calculates layout (positions and sizes)
6. Paints pixels to the screen

Understanding this order explains why the `<script>` tag goes at the bottom of `<body>` — by then, all elements exist in the DOM and are ready for JavaScript to interact with.

**Exercises:**

1. In your own words, write one sentence explaining the difference between HTML, CSS, and JavaScript. Share it in the community and give feedback on a classmate's explanation.
2. Open any website. Right-click → View Page Source. Find: the `<title>` tag, one `<meta>` tag, one semantic element (`<header>`, `<nav>`, `<main>`, etc.), and one place where a `<div>` is used where a semantic element would be better.

### Lesson 1.2 — The HTML5 Boilerplate

Every HTML document starts with the same skeleton. Memorise this — you will type it hundreds of times:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Page Title</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>

    <!-- visible content goes here -->

    <script src="script.js"></script>
  </body>
</html>
```

**Every line explained:**

| Line | Purpose |
|------|---------|
| `<!DOCTYPE html>` | Declares HTML5. The browser renders in standards mode, not quirks mode. Always the first line. |
| `<html lang="en">` | Root element. `lang` tells screen readers which language to use for pronunciation. |
| `<meta charset="UTF-8">` | Supports all characters — accents, Arabic, Chinese, emoji. Without it, special characters break. |
| `<meta name="viewport">` | Prevents mobile browsers from zooming out. Without it, your page looks tiny on phones. |
| `<title>` | The text in the browser tab and in search results. Describes the page, not the site. |
| `<link rel="stylesheet">` | Loads your CSS. The browser fetches and parses it before rendering. |
| `<script>` at bottom | JavaScript runs after HTML is parsed — so your elements exist when JS tries to find them. |

The `<head>` holds metadata invisible to the user — title, CSS links, meta tags, fonts, favicons. The `<body>` holds everything the user sees and interacts with — text, images, buttons, forms, navigation.

**Exercises:**

1. Close your notes. Type the full boilerplate from memory in a new file called `index.html`. Open it in Chrome. Validate it at validator.w3.org. Fix any errors.
2. Add a Google Font to the boilerplate. The `<link>` for the font must come *before* your `style.css` link — explain why in a comment.
3. Change `lang="en"` to `lang="fr"`. Open Chrome DevTools → Accessibility → enable screen reader simulation. Notice how the language declaration changes pronunciation.

### Lesson 1.3 — Semantic Elements and Heading Hierarchy

Both of these render identically in the browser — but only one communicates meaning:

```html
<!-- Non-semantic — tells the browser nothing -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="main">
  <div class="big-text">Welcome</div>
</div>

<!-- Semantic — communicates structure and meaning -->
<header>
  <nav>...</nav>
</header>
<main>
  <h1>Welcome</h1>
</main>
```

The semantic version lets screen readers jump directly to `<main>`, gives search engines a clear structure, and makes the code readable at a glance.

**Page-level semantic elements:**

| Element | Purpose |
|---------|---------|
| `<header>` | Site header: logo, site name, primary nav. Also valid as a section header inside `<article>` or `<section>`. |
| `<nav>` | Major navigation links only. Use `aria-label` when the page has multiple `<nav>` elements. |
| `<main>` | The primary unique content of this page. Only ONE `<main>` per document. |
| `<section>` | A thematic grouping — should always have a heading. |
| `<article>` | Self-contained, independently publishable content: blog posts, news articles, product cards, comments. |
| `<aside>` | Content tangentially related to the main content: sidebars, pull quotes, related links. |
| `<footer>` | Site or section footer: copyright, secondary nav, contact info. |

**A complete page structure:**

```html
<body>
  <header>
    <a href="/" class="logo">Cohort</a>
    <nav aria-label="Main navigation">
      <ul>
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/curriculum">Curriculum</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section id="hero">
      <h1>Learn Frontend Development with AI</h1>
      <p>A 22-week cohort for complete beginners.</p>
    </section>

    <section id="stages">
      <h2>What you will learn</h2>
      <article>
        <h3>Stage 1 — Web Fundamentals</h3>
        <p>HTML, CSS, JavaScript, and Git from week one.</p>
      </article>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 Frontend AI Cohort</p>
  </footer>
</body>
```

**Heading hierarchy rules:**
- `<h1>` appears **exactly once** per page — the page's main title
- Never skip levels (`<h2>` → `<h4>` is wrong — `<h3>` must come first)
- Use headings for structure, not visual size — sizing is CSS's job

**Exercises:**

1. Build a bio page using only semantic HTML — no `<div>` or `<span>`. Include `<header>`, `<nav>`, `<main>`, two `<section>` elements, one `<article>`, and `<footer>`.
2. Install the HeadingsMap browser extension. Open your bio page. Does your heading outline make sense as a table of contents? Fix any hierarchy issues.
3. Find a real website with heavy `<div class="header">` usage. Rewrite the top section using proper semantic elements. Share your before/after in the community.

## Module 2 — Content Elements

Mark up every type of content correctly — links, images, lists, tables, figures, and inline elements.

### Lesson 2.1 — Links and Images

**Links:**

```html
<!-- External — always add rel for security -->
<a href="https://developer.mozilla.org" target="_blank" rel="noopener noreferrer">
  MDN Web Docs
</a>

<!-- Internal page -->
<a href="/about">About us</a>

<!-- Same-page anchor -->
<a href="#week-3">Jump to Week 3</a>
<section id="week-3">...</section>

<!-- Email and phone -->
<a href="mailto:hello@cohort.dev">Email us</a>
<a href="tel:+2348001234567">Call us</a>

<!-- Download -->
<a href="/curriculum.pdf" download="Frontend-AI-Curriculum.pdf">
  Download curriculum
</a>

<!-- Mark the current page in navigation -->
<nav>
  <a href="/" aria-current="page">Home</a>
  <a href="/about">About</a>
</nav>
```

Without `rel="noopener noreferrer"`, an external page opened with `target="_blank"` can access your page via `window.opener` — a security vulnerability. Always include it on external links.

**Images:**

```html
<!-- Basic — alt is always required -->
<img src="hero.jpg" alt="A student typing at a laptop in a bright office" />

<!-- With explicit dimensions — prevents layout shift -->
<img src="logo.png" alt="Frontend AI Cohort logo" width="200" height="60" />

<!-- Image inside a link — alt describes the destination -->
<a href="/"><img src="logo.png" alt="Frontend AI Cohort — go to homepage" /></a>

<!-- Decorative image — empty alt so screen readers skip it -->
<img src="divider-wave.svg" alt="" />

<!-- Image with caption -->
<figure>
  <img src="component-tree.png" alt="Diagram showing App at the top with Header, Main, and Footer as children" />
  <figcaption>Figure 1: The React component tree for our e-commerce project</figcaption>
</figure>
```

**Writing good alt text:**

| Image type | Alt text approach |
|-----------|-------------------|
| Logo | "Company name logo" |
| Photo | Describe what is happening: "Two students pair-programming at a standing desk" |
| Chart | Describe the insight: "Bar chart showing React at 40% market share" |
| Icon button | Describe the action: "Close menu" |
| Decorative | `alt=""` — empty string, not missing attribute |

**Exercises:**

1. Add a navigation bar with: a home link, two internal page links, one external link (new tab, correct `rel`), and a "Back to top" anchor link. Test each one.
2. Add five images to your bio page. Write alt text for each. Have a classmate read only your alt text — can they understand what the images show without seeing them?

### Lesson 2.2 — Lists

```html
<!-- Unordered — when order does not matter -->
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>

<!-- Ordered — when sequence matters -->
<ol>
  <li>Install VS Code</li>
  <li>Install the Live Server extension</li>
  <li>Create index.html</li>
  <li>Open with Live Server</li>
</ol>

<!-- Description — key/value pairs, glossaries, FAQs -->
<dl>
  <dt>useState</dt>
  <dd>A React hook that adds local state to a function component.</dd>

  <dt>useEffect</dt>
  <dd>A React hook that runs side effects after the component renders.</dd>
</dl>

<!-- Nested list -->
<ul>
  <li>Stage 1 — Web Fundamentals
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>Stage 2 — React</li>
  <li>Stage 3 — Frontend AI</li>
</ul>
```

**Which list type to use:**

| Use case | Type |
|---------|------|
| Navigation links | `<ul>` |
| Step-by-step instructions | `<ol>` |
| Ingredients list | `<ul>` |
| Table of contents | `<ol>` |
| Glossary or FAQ | `<dl>` |
| Feature list | `<ul>` |

**Exercises:**

1. Mark up a recipe: use `<ul>` for ingredients, `<ol>` for steps, and a `<dl>` for nutritional facts. Nest a list inside one ingredient for sub-options (e.g. "any oil" → olive oil, sunflower oil, etc.).
2. Build a navigation menu that uses `<ul>` with a nested `<ul>` for a dropdown submenu. Just the HTML structure — no CSS yet.

### Lesson 2.3 — Tables

Tables are for **tabular data** — data with rows and columns that have a meaningful relationship. Never use tables for page layout.

```html
<table>
  <caption>Frontend AI Cohort — Stage Overview</caption>

  <thead>
    <tr>
      <th scope="col">Stage</th>
      <th scope="col">Topic</th>
      <th scope="col">Weeks</th>
      <th scope="col">Assessment</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Web Fundamentals</td>
      <td>1–8</td>
      <td>Vanilla JS app</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>React</td>
      <td>9–14</td>
      <td>E-commerce catalogue</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Frontend AI</td>
      <td>15–20</td>
      <td>AI-powered product</td>
    </tr>
  </tbody>

  <tfoot>
    <tr>
      <td colspan="2">Total duration</td>
      <td>22 weeks</td>
      <td>4 projects</td>
    </tr>
  </tfoot>
</table>
```

**Key accessibility rules:**
- `<caption>` — describes the table (like `alt` for images). Always include it.
- `scope="col"` on `<th>` — connects the header to every cell in its column
- `scope="row"` on `<th>` — connects the header to every cell in its row
- `colspan` / `rowspan` — merge cells horizontally or vertically

**Exercises:**

1. Create a weekly timetable (Mon–Fri, three time slots per day). Use `scope="col"` for day headers and `scope="row"` for time headers. Add a `<caption>`.
2. Find a data table on a real website. Inspect it in DevTools. Does it use `<th>` with `scope`? Does it have a `<caption>`? Write what you would fix.

### Lesson 2.4 — Figures and Inline Elements

**Figures:**

```html
<!-- Image with caption -->
<figure>
  <img src="flexbox-diagram.png" alt="Diagram showing main axis (horizontal) and cross axis (vertical) in a flex container" />
  <figcaption>Figure 2: Flexbox axes. Items lay out along the main axis by default.</figcaption>
</figure>

<!-- Code with caption -->
<figure>
  <pre><code>const double = n => n * 2;
console.log(double(5)); // 10</code></pre>
  <figcaption>An arrow function using implicit return syntax</figcaption>
</figure>

<!-- Blockquote with source -->
<figure>
  <blockquote>
    <p>Make it work, make it right, make it fast.</p>
  </blockquote>
  <figcaption>— Kent Beck</figcaption>
</figure>
```

**Semantic inline elements:**

```html
<p>You <strong>must</strong> commit before the deadline.</p>      <!-- strong importance -->
<p>The deadline is <em>tomorrow</em>, not next week.</p>           <!-- stress emphasis -->
<p>Run <code>git commit -m "message"</code> to save your work.</p><!-- inline code -->
<p>Press <kbd>Ctrl</kbd> + <kbd>S</kbd> to save the file.</p>    <!-- keyboard input -->
<p>The expected output is <samp>Hello, world!</samp></p>           <!-- sample output -->
<p>The cohort starts on <time datetime="2025-05-30">30 May 2025</time>.</p>
<p><abbr title="HyperText Markup Language">HTML</abbr> is the backbone of the web.</p>
<p>The price is <del>$100</del> <ins>$80</ins>.</p>              <!-- deleted / inserted -->
<p>E = mc<sup>2</sup></p>                                          <!-- superscript -->
<p>Water is H<sub>2</sub>O</p>                                     <!-- subscript -->
```

**Exercises:**

1. Add three `<figure>` elements to your bio page: one with an image and caption, one with a blockquote and attribution, and one with a code snippet and explanation.
2. Write a paragraph explaining a technical concept. Use at least four different inline semantic elements naturally within the prose — not forced, each must genuinely fit.

## Module 3 — Forms and User Input

Build complete, accessible, validated forms from scratch.

### Lesson 3.1 — Form Structure and Labels

```html
<form action="/submit" method="POST" novalidate>
  <!-- inputs -->
  <button type="submit">Submit</button>
  <button type="reset">Clear form</button>
</form>
```

- `action` — the URL to send data to (omit when JavaScript handles submission)
- `method="POST"` — data in the request body (use when creating or updating data)
- `method="GET"` — data appended to the URL (use for search forms)
- `novalidate` — disables browser validation when you handle it with JavaScript

**Labelling inputs — always required:**

```html
<!-- Method 1: for + id (preferred — elements can be anywhere on the page) -->
<label for="email">Email address</label>
<input type="email" id="email" name="email" />

<!-- Method 2: wrapping — no for/id needed -->
<label>
  Email address
  <input type="email" name="email" />
</label>

<!-- NEVER do this — no accessible association -->
<p>Email address</p>
<input type="email" name="email" />
```

Clicking a label focuses its input. This doubles the click target — critical for mobile and for checkboxes/radio buttons.

**Grouping with fieldsets:**

```html
<form>
  <fieldset>
    <legend>Your details</legend>
    <div class="field">
      <label for="first">First name</label>
      <input type="text" id="first" name="firstName" required />
    </div>
    <div class="field">
      <label for="last">Last name</label>
      <input type="text" id="last" name="lastName" required />
    </div>
  </fieldset>

  <fieldset>
    <legend>Choose your plan</legend>
    <label class="radio-option">
      <input type="radio" name="plan" value="free" checked /> Free
    </label>
    <label class="radio-option">
      <input type="radio" name="plan" value="pro" /> Pro — $29/month
    </label>
  </fieldset>
</form>
```

**Exercises:**

1. Build a "Contact us" form: name, email, subject, message, and a submit button. Every input must use Method 1 (for + id). Use fieldset and legend to group the fields.
2. Break one of your labels intentionally. Validate at validator.w3.org — it should report the missing association. Fix it and validate again.

### Lesson 3.2 — Input Types and Attributes

```html
<!-- Text family -->
<input type="text"     name="username"   autocomplete="username" />
<input type="email"    name="email"      autocomplete="email" />
<input type="password" name="password"   autocomplete="new-password" />
<input type="url"      name="website" />
<input type="tel"      name="phone"      autocomplete="tel" />
<input type="search"   name="q"          placeholder="Search..." />

<!-- Numbers -->
<input type="number" name="age"    min="16"  max="99"  step="1" />
<input type="range"  name="volume" min="0"   max="100" value="50" />

<!-- Dates -->
<input type="date"           name="birthday" />
<input type="time"           name="appointment" />
<input type="datetime-local" name="event" />

<!-- Files -->
<input type="file" name="avatar" accept="image/*" />
<input type="file" name="docs"   accept=".pdf,.docx" multiple />

<!-- Choices -->
<input type="checkbox" id="agree" name="agree" />
<input type="radio"    name="plan" value="free" id="plan-free" />

<!-- Hidden — sent with form but not shown -->
<input type="hidden" name="csrf_token" value="abc123" />
```

**Textarea and Select:**

```html
<textarea name="message" rows="5" placeholder="Your message..."></textarea>

<select name="country">
  <option value="">Select your country</option>
  <optgroup label="West Africa">
    <option value="NG">Nigeria</option>
    <option value="GH">Ghana</option>
  </optgroup>
  <optgroup label="East Africa">
    <option value="KE">Kenya</option>
    <option value="TZ">Tanzania</option>
  </optgroup>
</select>
```

**Validation attributes:**

```html
<input type="email" name="email" required minlength="5" maxlength="100" />

<input
  type="text" name="username"
  required minlength="3" maxlength="20"
  pattern="[a-zA-Z0-9_]+"
  title="Letters, numbers, and underscores only"
/>

<input type="number" name="score" required min="0" max="100" step="5" />
```

**Exercises:**

1. Build a "Book a call" form: name, email, phone (tel input), preferred date (future dates only using `min`), time slot (select), and optional message. Use correct input types for each field.
2. Add an `<input type="range">` for a satisfaction score (1–10). Display the current value next to the slider, updating live as the user drags it using only HTML and `oninput`.

### Lesson 3.3 — Validation and Error States

Use `aria-describedby` to link error messages to inputs, `aria-invalid` to signal invalid state, and `role="alert"` so screen readers announce errors as soon as they appear.

```html
<div class="field">
  <label for="reg-email">Email address</label>
  <input
    type="email"
    id="reg-email"
    name="email"
    required
    aria-describedby="email-hint email-error"
    aria-invalid="false"
  />
  <span id="email-hint" class="hint">We'll never share your email.</span>
  <span id="email-error" class="error" role="alert" hidden>
    Please enter a valid email address.
  </span>
</div>
```

**A complete accessible registration form:**

```html
<form id="register-form" novalidate>
  <fieldset>
    <legend>Create your account</legend>

    <div class="field">
      <label for="full-name">Full name <span aria-hidden="true">*</span></label>
      <input type="text" id="full-name" name="fullName"
             required minlength="2" autocomplete="name"
             aria-describedby="name-error" />
      <p id="name-error" class="error" role="alert" hidden>
        Name must be at least 2 characters.
      </p>
    </div>

    <div class="field">
      <label for="email">Email <span aria-hidden="true">*</span></label>
      <input type="email" id="email" name="email"
             required autocomplete="email"
             aria-describedby="email-error" />
      <p id="email-error" class="error" role="alert" hidden>
        Please enter a valid email address.
      </p>
    </div>

    <div class="field">
      <label for="password">Password <span aria-hidden="true">*</span></label>
      <input type="password" id="password" name="password"
             required minlength="8" autocomplete="new-password"
             aria-describedby="password-hint password-error" />
      <p id="password-hint" class="hint">Minimum 8 characters.</p>
      <p id="password-error" class="error" role="alert" hidden>
        Password must be at least 8 characters.
      </p>
    </div>
  </fieldset>

  <button type="submit">Create account</button>
</form>
```

**Exercises:**

1. Add error messages to your form from Lesson 3.1. Each field should have a `<p role="alert">` linked via `aria-describedby`. Toggle `hidden` and `aria-invalid` with JavaScript when validation fails.
2. Build a password field with a "Show/hide password" toggle button. Toggle `type="password"` ↔ `type="text"` and update the button's `aria-label` accordingly.

### Lesson 3.4 — A Complete Form Project

This lesson is project-driven. You will build a complete "Cohort Enrolment" form covering every form element type from this module.

**Form requirements:**
1. Full name (text, required, min 2 chars)
2. Email address (email, required)
3. Phone number (tel, optional)
4. Country (select with optgroups, required)
5. Date of birth (date, required, must be 16+ years — set `max` dynamically with JavaScript)
6. Plan selection (radio buttons in a fieldset, required)
7. Short bio (textarea, optional, max 300 chars with live character counter)
8. Agreement to terms (checkbox, required)
9. Submit button (disabled until all required fields are valid)

```html
<form id="enrolment-form" novalidate>

  <fieldset>
    <legend>Personal Information</legend>

    <div class="field">
      <label for="e-name">Full name <span aria-hidden="true">*</span></label>
      <input type="text" id="e-name" name="fullName"
             required minlength="2" autocomplete="name"
             aria-describedby="name-err" />
      <p id="name-err" class="error" role="alert" hidden>
        Please enter your full name (at least 2 characters).
      </p>
    </div>

    <div class="field">
      <label for="e-email">Email <span aria-hidden="true">*</span></label>
      <input type="email" id="e-email" name="email"
             required autocomplete="email"
             aria-describedby="email-err" />
      <p id="email-err" class="error" role="alert" hidden>
        Please enter a valid email address.
      </p>
    </div>

    <div class="field">
      <label for="e-dob">Date of birth <span aria-hidden="true">*</span></label>
      <input type="date" id="e-dob" name="dob"
             required aria-describedby="dob-err dob-hint" />
      <p id="dob-hint" class="hint">You must be at least 16 years old.</p>
      <p id="dob-err" class="error" role="alert" hidden>
        You must be at least 16 to enrol.
      </p>
    </div>

    <div class="field">
      <label for="e-country">Country <span aria-hidden="true">*</span></label>
      <select id="e-country" name="country" required>
        <option value="">Select your country</option>
        <optgroup label="West Africa">
          <option value="NG">Nigeria</option>
          <option value="GH">Ghana</option>
        </optgroup>
        <optgroup label="Other">
          <option value="GB">United Kingdom</option>
          <option value="US">United States</option>
        </optgroup>
      </select>
    </div>
  </fieldset>

  <fieldset>
    <legend>Cohort Plan <span aria-hidden="true">*</span></legend>
    <label class="radio-opt">
      <input type="radio" name="plan" value="free" />
      Community only — free
    </label>
    <label class="radio-opt">
      <input type="radio" name="plan" value="cohort" checked />
      Full cohort — starts 30 May 2025
    </label>
  </fieldset>

  <div class="field">
    <label for="e-bio">Short bio <span class="optional">(optional)</span></label>
    <textarea id="e-bio" name="bio" rows="4" maxlength="300"
              aria-describedby="bio-count"
              placeholder="Tell us a bit about yourself..."></textarea>
    <p id="bio-count" class="hint">
      <span id="bio-remaining">300</span> characters remaining
    </p>
  </div>

  <div class="field">
    <label class="checkbox-opt">
      <input type="checkbox" name="terms" required id="e-terms" />
      I agree to the <a href="/terms">terms and conditions</a>
      <span aria-hidden="true">*</span>
    </label>
  </div>

  <button type="submit" id="submit-btn" disabled>
    Complete enrolment
  </button>
</form>
```

**Exercises:**

1. Build the complete form above. Add JavaScript to: update the character counter, toggle error messages on blur, and enable/disable the submit button.
2. Navigate the entire form using only the keyboard. Fix anything you cannot reach or operate.
3. Run the form through the W3C Validator. Fix all errors. Run Chrome Lighthouse → Accessibility. Target a score of 95+.

## Module 4 — Accessibility and Validation

Make your HTML work for everyone and meet professional quality standards.

### Lesson 4.1 — Accessibility Fundamentals

**The four WCAG principles (POUR):**
1. **Perceivable** — content can be seen, heard, or otherwise perceived
2. **Operable** — interface can be navigated without a mouse
3. **Understandable** — content and behaviour are predictable
4. **Robust** — works with assistive technologies (screen readers, voice control)

Native HTML elements already carry the correct role, keyboard behaviour, and ARIA properties built in. Semantic HTML gives you accessibility for free.

```html
<!-- WRONG — not keyboard focusable, not announced as a button -->
<div class="btn" onclick="submit()">Submit</div>

<!-- RIGHT — keyboard focusable, announced as "Submit, button" -->
<button type="button" onclick="submit()">Submit</button>
```

**ARIA — use only when native HTML is not enough:**

```html
<!-- Landmarks with labels (when you have multiple of the same element) -->
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Breadcrumb">...</nav>

<!-- Icon-only buttons need a label -->
<button aria-label="Close dialog">✕</button>

<!-- Associate a description with an input -->
<input type="password" aria-describedby="pw-requirements" />
<p id="pw-requirements">Must be 8+ characters with at least one number.</p>

<!-- Mark the current page -->
<a href="/" aria-current="page">Home</a>

<!-- Expandable sections -->
<button aria-expanded="false" aria-controls="menu-list">Menu</button>
<ul id="menu-list" hidden>...</ul>

<!-- Live regions — announce dynamic content to screen readers -->
<div role="status" aria-live="polite">Saved successfully.</div>
<div role="alert"  aria-live="assertive">Error: connection lost.</div>
```

**Exercises:**

1. Run your bio page through Chrome Lighthouse → Accessibility. Screenshot every issue. Fix them all. Re-run and screenshot the improved score.
2. Add `aria-label` to every icon-only button on your page. Add `aria-current="page"` to the active nav link. Add `role="alert"` to all form error messages.

### Lesson 4.2 — Keyboard Navigation and Colour Contrast

Every interactive element on a page must be reachable and operable using only a keyboard.

**Skip navigation (required on every page):**

```html
<!-- First thing in <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>
...
<main id="main-content">...</main>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  background: #1A56A0;
  color: white;
  padding: 8px 16px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}

/* NEVER do this — removes keyboard visibility */
:focus { outline: none; }

/* DO this — style the outline, but keep it visible */
:focus-visible {
  outline: 2px solid #7C3AED;
  outline-offset: 2px;
}
```

**Tab order and tabindex:**

```html
<!-- tabindex="0" — adds to natural tab order -->
<div tabindex="0" role="button">Custom button</div>

<!-- tabindex="-1" — focusable by script only, NOT by Tab key -->
<!-- Use for modal focus management -->
<div id="dialog" tabindex="-1" role="dialog">...</div>

<!-- NEVER use tabindex > 0 — it breaks natural tab flow -->
```

**Colour contrast minimums (WCAG AA):**
- Normal text (under 18px / 14px bold): **4.5:1**
- Large text (18px+ / 14px+ bold): **3:1**
- UI components and icons: **3:1**

Use the WebAIM Contrast Checker or Chrome DevTools → Inspect → Accessibility → Contrast ratio to check.

**Exercises:**

1. Add a skip navigation link to your page. Press Tab immediately after the page loads — the link should become visible and, when activated, jump focus to `<main>`.
2. Navigate your entire page using only Tab, Shift+Tab, Enter, and Space. Document every element you cannot reach or activate. Fix them all.
3. Check every text/background colour combination on your page against WCAG AA. Fix any that fail.

### Lesson 4.3 — Validation and the Professional Checklist

**The ten most common HTML mistakes:**

```html
<!-- 1. Divitis -->
<div class="nav"><div class="nav-item">Home</div></div>              <!-- WRONG -->
<nav><ul><li><a href="/">Home</a></li></ul></nav>                    <!-- RIGHT -->

<!-- 2. Missing alt -->
<img src="logo.png" />                                               <!-- WRONG -->
<img src="logo.png" alt="Company logo" />                            <!-- RIGHT -->

<!-- 3. Heading used for visual size, not structure -->
<h4>Section that is logically an h2</h4>                             <!-- WRONG -->
<h2 class="display-heading">Section heading</h2>                     <!-- RIGHT -->

<!-- 4. Placeholder instead of label -->
<input placeholder="Your email" />                                   <!-- WRONG -->
<label for="e">Email</label><input id="e" placeholder="you@example.com" /> <!-- RIGHT -->

<!-- 5. Empty interactive elements -->
<button><img src="icon.svg" /></button>                              <!-- WRONG -->
<button><img src="icon.svg" alt="Submit form" /></button>            <!-- RIGHT -->

<!-- 6. Broken nesting -->
<p>Text <strong>bold <em>both</strong></em></p>                     <!-- WRONG -->
<p>Text <strong>bold <em>both</em></strong></p>                     <!-- RIGHT -->

<!-- 7. Duplicate IDs -->
<div id="hero">...</div> ... <div id="hero">...</div>               <!-- WRONG -->
<!-- IDs must be unique per page -->

<!-- 8. Missing lang attribute -->
<html>                                                               <!-- WRONG -->
<html lang="en">                                                     <!-- RIGHT -->

<!-- 9. Using <br> for spacing -->
<p>Line 1</p><br><br><p>Line 2</p>                                  <!-- WRONG -->
<!-- Use CSS margin/padding for spacing -->

<!-- 10. External links without rel -->
<a href="..." target="_blank">Link</a>                               <!-- WRONG -->
<a href="..." target="_blank" rel="noopener noreferrer">Link</a>    <!-- RIGHT -->
```

**Pre-submission checklist:**
- Passes W3C Validator with zero errors
- `<html>` has `lang` attribute
- Descriptive `<title>` tag present
- Viewport meta tag present
- Every `<img>` has `alt` attribute (even if empty for decorative images)
- All inputs have an associated `<label>` element
- Heading levels are in order — no skipped levels
- No duplicate `id` values on the page
- `<main>` appears exactly once
- All external links have `rel="noopener noreferrer"`
- All interactive elements are keyboard-accessible
- Colour contrast meets WCAG AA (4.5:1 for body text, 3:1 for large text)
- Chrome Lighthouse Accessibility score ≥ 90
- Forms have `<fieldset>` and `<legend>` for grouped inputs

**Exercises:**

1. Apply the full checklist to your bio page. Document each item as Pass / Fail / N/A. Fix every failure before the weekend workshop.
2. Deliberately introduce 6 errors from the list above into your HTML. Swap with a classmate — validate each other's pages and fix each other's errors. Discuss what you found.
3. Run the W3C Validator on three real websites. Screenshot the errors. Which site has the most? What are the most common error types across all three?
