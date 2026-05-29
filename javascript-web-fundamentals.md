# JavaScript — Web Fundamentals

**Track:** Web Fundamentals
**Modules:** 4
**Total Lessons:** 14
**Prerequisite:** Course 1 — HTML, Course 2 — CSS

## Module 1 — Language Fundamentals

### Lesson 1.1 — Variables, Data Types & Operators

```javascript
// const — never reassigned (use by default)
const name    = "Sam";
const age     = 30;
const isAdmin = true;

// let — will be reassigned
let score  = 0;
let status = "pending";
score++;
status = "complete";

// NEVER use var — confusing scope rules, superseded by const/let
```

**The eight data types:**

```javascript
// Primitives (simple, immutable values)
const str     = "Hello";           // String
const num     = 42;                // Number
const big     = 9007199254740993n; // BigInt
const bool    = true;
const nothing = null;              // Null — intentional absence
let   undef;                       // Undefined — declared, not assigned
const sym     = Symbol("id");      // Symbol — unique identifier

// Object (complex, mutable)
const obj  = { name: "Sam", age: 30 };
const arr  = ["HTML", "CSS", "JS"];
const fn   = () => {};
const date = new Date();
```

**Operators:**

```javascript
// Arithmetic
5 + 3   // 8     | "5" + 3  // "53" (string concatenation — watch out)
5 - 3   // 2     | "5" - 3  // 2   (JS coerces "5" to number)
5 * 3   // 15    | 5 ** 2   // 25  (exponentiation)
10 / 3  // 3.333 | 10 % 3   // 1   (remainder)

// Strict equality — ALWAYS use ===
5 === 5       // true  — same type AND value
5 === "5"     // false — different types
null === null // true

// NEVER use == (loose equality coerces types — unpredictable)
0 == false        // true  ← unexpected
null == undefined // true  ← unexpected

// Logical
true && false  // false — AND (both must be true)
true || false  // true  — OR (at least one must be true)
!true          // false — NOT

// Nullish coalescing — right side if left is null or undefined
const label = user?.name ?? "Guest";

// Optional chaining — don't error if property doesn't exist
const city = user?.address?.city;  // undefined, not an error
```

**Exercises**

**1.1.1** — Declare five variables using `const` and two using `let`. Log all seven to the console using a single template literal.

**1.1.2** — Without running the code, predict the output of:
```javascript
console.log(typeof null);
console.log("5" + 3);
console.log("5" - 3);
console.log(0 == false);
console.log(0 === false);
```
Run it. Explain any result that surprises you.

### Lesson 1.2 — Functions

```javascript
// 1. Declaration — hoisted (available before its line)
function greet(name) {
  return `Hello, ${name}!`;
}

// 2. Expression — not hoisted
const greet = function(name) {
  return `Hello, ${name}!`;
};

// 3. Arrow — preferred in modern JS
const greet = (name) => `Hello, ${name}!`;  // implicit return

// 4. Arrow — multi-line needs explicit return
const greet = (name) => {
  const msg = `Hello, ${name}!`;
  return msg;
};

// Single parameter: parentheses optional
const double = n => n * 2;

// No parameters: parentheses required
const now = () => new Date();
```

**Parameters:**

```javascript
// Default values
const greet = (name = "Guest") => `Hello, ${name}!`;
greet("Sam");  // "Hello, Sam!"
greet();       // "Hello, Guest!"

// Rest — collects remaining args
const sum = (...nums) => nums.reduce((a, n) => a + n, 0);
sum(1, 2, 3, 4, 5);  // 15

// Destructuring
const display = ({ name, role = "student", email }) =>
  `${name} (${role}) — ${email}`;
```

**Scope and closures:**

```javascript
const multiplier = 10;   // global — accessible everywhere

function outer() {
  const x = 5;            // function scope

  function inner() {
    // Closure: inner "closes over" x from outer scope
    return x * multiplier;  // can access both
  }

  return inner();
}

// Counter using closure
function makeCounter(start = 0) {
  let count = start;
  return {
    increment: () => ++count,
    decrement: () => --count,
    value:     () => count,
    reset:     () => { count = start; },
  };
}

const counter = makeCounter(10);
counter.increment();  // 11
counter.increment();  // 12
counter.value();      // 12
```

**Exercises**

**1.2.1** — Write three versions of the same `add(a, b)` function: declaration, expression, and arrow. All must produce identical output. Then write a one-liner arrow that implicitly returns the sum.

**1.2.2** — Write `makeMultiplier(factor)` that returns a function. The returned function multiplies its argument by `factor`. Create `double`, `triple`, and `times10` from it.

**1.2.3** — Write a `formatPrice(amount, currency = "USD", locale = "en-US")` function using `Intl.NumberFormat`. Test it with at least three different currencies.

### Lesson 1.3 — Arrays

```javascript
const products = [
  { id: 1, name: "React Course",    price: 49, category: "course", inStock: true  },
  { id: 2, name: "CSS Masterclass", price: 29, category: "course", inStock: true  },
  { id: 3, name: "JS Handbook",     price: 19, category: "book",   inStock: false },
  { id: 4, name: "Dev T-shirt",     price: 25, category: "merch",  inStock: true  },
];

// map — transform every item, returns new array (same length)
const names  = products.map(p => p.name);
const priced = products.map(p => ({ ...p, priceWithTax: p.price * 1.075 }));

// filter — keep matching items, returns new array (shorter or equal)
const inStock = products.filter(p => p.inStock);
const courses = products.filter(p => p.category === "course");
const under30 = products.filter(p => p.price < 30);

// reduce — combine all items into one value
const total = products.reduce((sum, p) => sum + p.price, 0);  // 122
const byCat = products.reduce((acc, p) => {
  acc[p.category] = [...(acc[p.category] || []), p];
  return acc;
}, {});

// find — first match (or undefined)
const reactCourse = products.find(p => p.name.includes("React"));

// findIndex — index of first match (or -1)
const reactIndex = products.findIndex(p => p.name.includes("React"));

// some / every
const anyOutOfStock = products.some(p => !p.inStock);   // true
const allHaveName   = products.every(p => p.name);      // true

// Sorting (sort mutates — always copy first)
const byPrice = [...products].sort((a, b) => a.price - b.price);
const byName  = [...products].sort((a, b) => a.name.localeCompare(b.name));

// Chaining
const result = products
  .filter(p => p.inStock)
  .sort((a, b) => a.price - b.price)
  .map(p => `${p.name} — $${p.price}`);
```

**Adding and removing (non-mutating):**

```javascript
const arr = [1, 2, 3];
const withEnd      = [...arr, 4];               // [1, 2, 3, 4]
const withStart    = [0, ...arr];               // [0, 1, 2, 3]
const without2     = arr.filter(n => n !== 2);  // [1, 3]
const replaced     = arr.map(n => n === 2 ? 99 : n); // [1, 99, 3]
const withoutLast  = arr.slice(0, -1);          // [1, 2]
const withoutFirst = arr.slice(1);              // [2, 3]
```

**Exercises**

**1.3.1** — Given the products array above, write expressions (no loops) for: all in-stock products under $30 sorted by price, total value of all in-stock products, all product names as a comma-separated string.

**1.3.2** — Write a `groupBy(array, key)` function that groups an array of objects by a property. `groupBy(products, "category")` should return `{ course: [...], book: [...], merch: [...] }`.

### Lesson 1.4 — Objects & Destructuring

```javascript
const user = {
  id: 1,
  name: "Sam Adeyemi",
  email: "sam@cohort.dev",
  role: "student",
  address: { city: "Lagos", country: "Nigeria" },
};

// Reading
user.name      // dot notation (preferred)
user["email"]  // bracket notation (use for dynamic keys)
user.address.city  // nested

// Dynamic key
const key = "role";
user[key]  // "student"

// Updating (always return new object in React/functional code)
const updated = { ...user, role: "graduate" };

// Merging
const withDefaults = { theme: "light", lang: "en", ...userPrefs };

// Object methods
Object.keys(user)    // ["id", "name", "email", ...]
Object.values(user)  // [1, "Sam Adeyemi", ...]
Object.entries(user) // [["id", 1], ["name", "Sam"], ...]
Object.fromEntries([["a", 1], ["b", 2]])  // { a: 1, b: 2 }
```

**Destructuring:**

```javascript
// Object destructuring
const { name, email, role = "student" } = user;

// Rename while destructuring
const { name: fullName, email: userEmail } = user;

// Nested
const { address: { city, country } } = user;

// Array destructuring
const [first, second, ...rest] = ["HTML", "CSS", "JS", "React"];
// first = "HTML", second = "CSS", rest = ["JS", "React"]

// Skip items
const [, , third] = ["HTML", "CSS", "JS"];  // third = "JS"

// In function parameters
function renderUser({ name, email, role = "student" }) {
  return `${name} — ${role}`;
}

// Swap variables
let a = 1, b = 2;
[a, b] = [b, a];  // a = 2, b = 1
```

**Exercises**

**1.4.1** — Write a `pick(obj, keys)` function that returns a new object with only the specified keys. `pick(user, ["name", "email"])` → `{ name: "Sam", email: "..." }`.

**1.4.2** — Write an `omit(obj, keys)` function that returns a new object without the specified keys.

**1.4.3** — Given a nested user object, use destructuring to extract: `name`, `city` (from address), and `first` score (from an array of scores). Do it in one destructuring statement.

## Module 2 — The Browser

### Lesson 2.1 — DOM Manipulation

**Selecting elements:**

```javascript
// Single element — first match
const hero     = document.querySelector("#hero");
const firstBtn = document.querySelector("button");
const emailIn  = document.querySelector('input[type="email"]');

// Multiple elements — NodeList (use Array.from or spread to get array methods)
const cards    = document.querySelectorAll(".card");
const navLinks = [...document.querySelectorAll("nav a")];

// Relative to an element
const parent   = el.parentElement;
const children = [...el.children];
const next     = el.nextElementSibling;
const prev     = el.previousElementSibling;
```

**Reading and writing:**

```javascript
// Text content (safe — no HTML injection)
el.textContent;
el.textContent = "New text";

// Input values
input.value;
input.value = "";

// Attributes
el.getAttribute("href");
el.setAttribute("href", "https://...");
el.removeAttribute("disabled");
el.hasAttribute("required");

// Data attributes  <div data-user-id="42" data-role="admin">
el.dataset.userId;        // "42"
el.dataset.role = "mod";  // sets data-role="mod"

// CSS classes
el.classList.add("active");
el.classList.remove("open");
el.classList.toggle("selected");
el.classList.contains("active");       // true/false
el.classList.replace("old", "new");
```

**Creating and inserting:**

```javascript
// Create
const card = document.createElement("div");
card.className = "card";
card.dataset.id = "42";

// Build with innerHTML (NEVER use with user-provided content)
card.innerHTML = `
  <h3>${item.name}</h3>
  <p>${item.description}</p>
`;

// Insert
container.append(card);           // add to end
container.prepend(card);          // add to start
existing.insertAdjacentElement("afterend", card);  // after a sibling

// Efficient batch insert
function renderList(items, container) {
  container.innerHTML = "";
  const fragment = document.createDocumentFragment();
  items.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item.name;  // textContent is XSS-safe
    fragment.appendChild(li);
  });
  container.appendChild(fragment);
}

// Remove
el.remove();
```

**Exercises**

**2.1.1** — Build a dynamic list. Render five items from an array as `<li>` elements. Each item has a "Delete" button. Clicking delete removes the item from both the array and the DOM.

**2.1.2** — Build a character counter. As the user types in a `<textarea>`, update a `<span>` showing "X / 280 characters". Change the text red when over 280.

### Lesson 2.2 — Events

```javascript
// Adding listeners
element.addEventListener("click", (event) => {
  console.log(event.target, event.type);
});

// Named function — can be removed later
function handleClick(e) { ... }
btn.addEventListener("click", handleClick);
btn.removeEventListener("click", handleClick);  // same reference required

// Event object
form.addEventListener("submit", (e) => {
  e.preventDefault();   // stop page reload
  e.stopPropagation();  // stop bubbling to parent

  e.target         // element that fired the event
  e.currentTarget  // element the listener is on
});

document.addEventListener("keydown", (e) => {
  e.key     // "Enter", "Escape", "ArrowUp", "a"
  e.ctrlKey // true if Ctrl held
  e.shiftKey// true if Shift held

  if (e.key === "Escape") closeModal();
  if (e.key === "Enter" && e.ctrlKey) submitForm();
});
```

**Event delegation — one listener for many elements:**

```javascript
// Add one listener to the parent, not to each child
const list = document.querySelector(".task-list");

list.addEventListener("click", (e) => {
  const item = e.target.closest(".task-item");
  if (!item) return;

  const id = item.dataset.id;

  if (e.target.matches(".delete-btn"))   deleteTask(id);
  if (e.target.matches(".complete-btn")) toggleComplete(id);
});
// Works for dynamically added items too
```

**Common events reference:**

```javascript
// Mouse
"click" "dblclick" "mouseenter" "mouseleave" "mousemove"

// Keyboard
"keydown" "keyup"

// Form
"submit" "input" "change" "focus" "blur"

// Window / Document
"DOMContentLoaded" "load" "resize" "scroll"
```

**Exercises**

**2.2.1** — Build a keyboard shortcut system. Press `?` anywhere to open a shortcuts modal. Press `Escape` to close it. Press `k` to focus the search input. No `onclick` attributes — use `addEventListener` only.

**2.2.2** — Build an FAQ with event delegation: one click listener on the FAQ container. Clicking a question toggles its answer. The toggle button must update `aria-expanded`.

### Lesson 2.3 — Form Validation with JavaScript

```javascript
function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isValidDate(dateStr) {
  const date = new Date(dateStr);
  return date instanceof Date && !isNaN(date) && date > new Date();
}

function showError(input, message) {
  const field = input.closest(".field");
  field.classList.add("is-error");
  field.classList.remove("is-success");
  const errorEl = document.getElementById(
    input.getAttribute("aria-describedby").split(" ").find(id => id.includes("error"))
  );
  if (errorEl) { errorEl.textContent = message; errorEl.hidden = false; }
  input.setAttribute("aria-invalid", "true");
}

function showSuccess(input) {
  const field = input.closest(".field");
  field.classList.remove("is-error");
  field.classList.add("is-success");
  const errorId = input.getAttribute("aria-describedby")?.split(" ").find(id => id.includes("error"));
  const errorEl = errorId && document.getElementById(errorId);
  if (errorEl) { errorEl.hidden = true; }
  input.setAttribute("aria-invalid", "false");
}

const form        = document.querySelector("#register-form");
const submitBtn   = form.querySelector('[type="submit"]');
const allRequired = [...form.querySelectorAll("[required]")];

function validateField(input) {
  const value = input.value.trim();
  if (!value && input.required) { showError(input, "This field is required"); return false; }
  if (input.type === "email" && !validateEmail(value)) { showError(input, "Enter a valid email"); return false; }
  if (input.minLength && value.length < input.minLength) { showError(input, `Minimum ${input.minLength} characters`); return false; }
  showSuccess(input);
  return true;
}

// Validate on blur
allRequired.forEach(input => {
  input.addEventListener("blur", () => validateField(input));
  input.addEventListener("input", () => {
    if (input.getAttribute("aria-invalid") === "true") validateField(input);
    submitBtn.disabled = !allRequired.every(i => validateField(i) || false);
  });
});

// Validate on submit
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const allValid = allRequired.every(validateField);
  if (allValid) submitForm();
  else allRequired.find(i => i.getAttribute("aria-invalid") === "true")?.focus();
});
```

**Exercises**

**2.3.1** — Build a complete registration form with real-time validation: validate each field on `blur`, show a green tick on success and red error message on failure, disable submit until all fields are valid.

### Lesson 2.4 — localStorage

```javascript
// Store
localStorage.setItem("theme", "dark");
localStorage.setItem("user", JSON.stringify({ name: "Sam", score: 42 }));

// Retrieve
const theme = localStorage.getItem("theme");          // "dark"
const user  = JSON.parse(localStorage.getItem("user")); // object

// Remove
localStorage.removeItem("theme");
localStorage.clear();

// Safe helpers (always use these)
function getStorage(key, fallback = null) {
  try {
    const item = localStorage.getItem(key);
    return item !== null ? JSON.parse(item) : fallback;
  } catch { return fallback; }
}

function setStorage(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); }
  catch (e) { console.error("localStorage write failed:", e); }
}

// Usage
let tasks = getStorage("tasks", []);
tasks.push({ id: Date.now(), text: "New task", done: false });
setStorage("tasks", tasks);
```

**Persistent to-do list pattern:**

```javascript
let tasks = getStorage("tasks", []);

function render() {
  const list = document.querySelector("#task-list");
  if (!tasks.length) { list.innerHTML = '<p class="empty">No tasks.</p>'; return; }
  const fragment = document.createDocumentFragment();
  tasks.forEach(task => {
    const li = document.createElement("li");
    li.className = task.done ? "task task--done" : "task";
    li.dataset.id = task.id;
    li.innerHTML = `
      <input type="checkbox" ${task.done ? "checked" : ""} />
      <span>${task.text}</span>
      <button class="delete-btn" aria-label="Delete task">✕</button>
    `;
    fragment.appendChild(li);
  });
  list.innerHTML = "";
  list.appendChild(fragment);
}

document.querySelector("#add-form").addEventListener("submit", e => {
  e.preventDefault();
  const input = e.target.querySelector("input");
  const text  = input.value.trim();
  if (!text) return;
  tasks.push({ id: Date.now(), text, done: false });
  setStorage("tasks", tasks);
  input.value = "";
  render();
});

document.querySelector("#task-list").addEventListener("click", e => {
  const item = e.target.closest(".task");
  if (!item) return;
  const id = Number(item.dataset.id);
  if (e.target.type === "checkbox") tasks = tasks.map(t => t.id === id ? { ...t, done: !t.done } : t);
  if (e.target.classList.contains("delete-btn")) tasks = tasks.filter(t => t.id !== id);
  setStorage("tasks", tasks);
  render();
});

render();
```

**Exercises**

**2.4.1** — Build a persistent to-do list: add tasks, toggle complete, delete tasks. State survives page refresh via localStorage.

**2.4.2** — Add a "recently viewed" feature to a product list. The last 5 viewed products are stored and displayed in a sidebar. Refresh the page — they should still be there.

## Module 3 — Async JavaScript

### Lesson 3.1 — The Event Loop & Promises

**The event loop (simplified):**

```
Call Stack          |  Task Queue
--------------------|------------------
Running code        |  setTimeout callback
                    |  fetch response
                    |  click handler

When the call stack is empty, the event loop moves
the next task from the queue into the stack.
```

This is why `setTimeout(fn, 0)` doesn't run *immediately* — it queues the callback. The current call stack must finish first.

**Promises:**

```javascript
// A Promise represents a value that will be available in the future
const promise = new Promise((resolve, reject) => {
  const success = true;
  if (success) resolve("Data loaded");
  else reject(new Error("Load failed"));
});

// .then / .catch / .finally chaining
promise
  .then(data  => console.log(data))
  .catch(err  => console.error(err.message))
  .finally(() => console.log("Done either way"));

// Common pattern — wrapping a delay
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
await delay(1000);  // wait 1 second
```

**Multiple promises:**

```javascript
// All must succeed — rejects if any one fails
const [user, posts, settings] = await Promise.all([
  fetchUser(id),
  fetchPosts(id),
  fetchSettings(id),
]);

// All run, get results even if some fail
const results = await Promise.allSettled([fetchA(), fetchB()]);
results.forEach(r => {
  if (r.status === "fulfilled") console.log(r.value);
  if (r.status === "rejected")  console.error(r.reason);
});

// First one to succeed
const fastest = await Promise.any([fetchFromServer1(), fetchFromServer2()]);
```

**Exercises**

**3.1.1** — Write a `retry(fn, times)` function that calls `fn()` up to `times` attempts. If `fn` throws, wait 500ms and try again. Resolve with the first success; reject after all attempts fail.

**3.1.2** — Use `Promise.all` to fetch three JSONPlaceholder endpoints simultaneously. Render all three results in separate sections. Show a loading spinner until all are complete.

### Lesson 3.2 — Async/Await

```javascript
// Promise chain — reads backwards
function loadPage() {
  return fetchUser()
    .then(user  => fetchPosts(user.id))
    .then(posts => fetchComments(posts[0].id))
    .then(comments => render(comments))
    .catch(err  => showError(err));
}

// Async/await — reads top to bottom
async function loadPage() {
  try {
    const user     = await fetchUser();
    const posts    = await fetchPosts(user.id);
    const comments = await fetchComments(posts[0].id);
    render(comments);
  } catch (err) {
    showError(err);
  } finally {
    hideSpinner();  // runs regardless of success or failure
  }
}
```

**Async functions always return a Promise:**

```javascript
async function getUser(id) {
  return { id, name: "Sam" };  // automatically wrapped in Promise.resolve()
}

// So you can await them
const user = await getUser(1);
```

**Common patterns:**

```javascript
// Loading state
async function fetchAndRender(url) {
  showLoading();
  try {
    const data = await apiFetch(url);
    render(data);
  } catch (err) {
    showError(err.message);
  } finally {
    hideLoading();
  }
}

// Parallel when operations don't depend on each other
const [user, config] = await Promise.all([fetchUser(id), fetchConfig()]);

// Sequential when they do depend on each other
const user  = await fetchUser(id);
const posts = await fetchPosts(user.id);  // needs user first

// Async forEach pattern (forEach doesn't await — use for...of)
for (const item of items) {
  await processItem(item);
}
```

**Exercises**

**3.2.1** — Rewrite this callback-based code as async/await:
```javascript
getData(function(data) {
  processData(data, function(result) {
    saveResult(result, function(saved) { console.log("Done", saved); });
  });
});
```

**3.2.2** — Write an `asyncMap(array, asyncFn)` helper that applies an async function to every item in an array in parallel using `Promise.all`, and returns an array of results.

### Lesson 3.3 — Fetch API & REST

```javascript
// Always check response.ok — fetch only rejects on network failure
async function apiFetch(url, options = {}) {
  const response = await fetch(url, options);
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.message || `HTTP ${response.status} ${response.statusText}`);
  }
  return response.json();
}

const BASE = "https://jsonplaceholder.typicode.com";

// GET
const users = await apiFetch(`${BASE}/users`);
const user  = await apiFetch(`${BASE}/users/1`);

// POST
const created = await apiFetch(`${BASE}/posts`, {
  method:  "POST",
  headers: { "Content-Type": "application/json" },
  body:    JSON.stringify({ title: "My post", body: "Content", userId: 1 }),
});

// PATCH — update specific fields only
const patched = await apiFetch(`${BASE}/posts/1`, {
  method:  "PATCH",
  headers: { "Content-Type": "application/json" },
  body:    JSON.stringify({ title: "Updated title" }),
});

// DELETE
await apiFetch(`${BASE}/posts/1`, { method: "DELETE" });
```

**Complete UI with all states:**

```javascript
const grid    = document.querySelector("#product-grid");
const loading = document.querySelector("#loading");
const error   = document.querySelector("#error");
const empty   = document.querySelector("#empty");

function setState(state) {
  loading.hidden = state !== "loading";
  error.hidden   = state !== "error";
  empty.hidden   = state !== "empty";
  grid.hidden    = state !== "data";
}

async function loadProducts() {
  setState("loading");
  try {
    const products = await apiFetch(`${BASE}/products`);
    if (!products.length) { setState("empty"); return; }
    grid.innerHTML = "";
    products.forEach(p => grid.appendChild(createCard(p)));
    setState("data");
  } catch (err) {
    error.querySelector("p").textContent = err.message;
    setState("error");
  }
}

document.querySelector("#retry-btn").addEventListener("click", loadProducts);
loadProducts();
```

**Exercises**

**3.3.1** — Fetch posts from JSONPlaceholder. Show: loading skeleton while fetching, rendered cards when complete, error message with retry button on failure, "No posts yet" message when empty.

**3.3.2** — Build a mini CRUD interface: fetch a list of todos, add new ones (POST), toggle done (PATCH), delete (DELETE). Show optimistic updates — update the UI immediately, then sync with the server.

## Module 4 — Project & Review

### Lesson 4.1 — Putting It All Together

**Application structure pattern:**

```javascript
// state.js — all application state in one place
const state = {
  products: [],
  cart:     getStorage("cart", []),
  filter:   { category: "all", maxPrice: Infinity, query: "" },
  ui:       { isCartOpen: false, isLoading: false },
};

// data.js — all API calls
async function loadProducts() {
  return apiFetch("/api/products");
}

async function addToCartAPI(productId) {
  return apiFetch("/api/cart", {
    method:  "POST",
    headers: { "Content-Type": "application/json" },
    body:    JSON.stringify({ productId }),
  });
}

// render.js — all DOM updates
function renderProducts(products) {
  const grid = document.querySelector("#product-grid");
  grid.innerHTML = "";
  const fragment = document.createDocumentFragment();
  products.forEach(p => fragment.appendChild(createProductCard(p)));
  grid.appendChild(fragment);
}

function updateCartCount(count) {
  document.querySelector("#cart-count").textContent = count;
}

// app.js — event handlers and application logic
async function handleAddToCart(productId) {
  const product = state.products.find(p => p.id === productId);
  if (!product) return;

  // Optimistic update
  state.cart.push({ ...product, quantity: 1 });
  setStorage("cart", state.cart);
  updateCartCount(state.cart.length);

  // Sync with server
  try {
    await addToCartAPI(productId);
  } catch {
    // Roll back on failure
    state.cart = state.cart.filter(p => p.id !== productId);
    setStorage("cart", state.cart);
    updateCartCount(state.cart.length);
    showToast("Could not add to cart. Try again.");
  }
}
```

**Exercises**

**4.1.1** — Refactor your to-do list from Module 2 into the pattern above. Separate state, data, render, and event layers into four separate files.

### Lesson 4.2 — Debugging

**Console methods:**

```javascript
console.log("basic log");
console.error("red error");
console.warn("yellow warning");
console.table(array);          // displays an array as a table
console.group("Group label");
  console.log("inside group");
console.groupEnd();
console.time("fetch");
  await loadData();
console.timeEnd("fetch");      // "fetch: 234ms"
console.trace();               // prints current call stack
```

**Debugger and breakpoints:**

```javascript
async function processOrder(order) {
  debugger;  // execution pauses here — inspect in DevTools
  const validated = await validate(order);
  return submit(validated);
}
```

In DevTools → Sources:
- Click line number to set a breakpoint
- `F10` — step over (next line)
- `F11` — step into (into function)
- `Shift+F11` — step out (out of function)
- `F8` — resume execution

**Network tab:** Inspect every fetch request — see URL, method, request body, response, timing.

**Exercises**

**4.2.1** — Add `console.table` logging to your to-do list: log the full tasks array every time it changes. Remove all logs before submitting.

**4.2.2** — Deliberately introduce a bug: call a function that doesn't exist. Use the DevTools error message and stack trace to find exactly where the error is. Document the debugging steps.

### Lesson 4.3 — Module Checklist & Review

**Pre-React JavaScript checklist:**

- [ ] Can declare variables and choose correctly between `const` and `let`
- [ ] Can write functions using all three syntaxes and know when to use each
- [ ] Can transform arrays with map/filter/reduce without mutation
- [ ] Can destructure objects and arrays, including nested structures
- [ ] Can select, create, update, and remove DOM elements
- [ ] Can attach event listeners and use event delegation
- [ ] Can validate a form with JavaScript and show accessible error messages
- [ ] Can read and write to `localStorage` with JSON serialisation
- [ ] Understands the event loop and why async code is needed
- [ ] Can write async/await with try/catch/finally
- [ ] Can make GET, POST, PATCH, DELETE requests with fetch
- [ ] Can build a UI with loading, error, and empty states
- [ ] Can debug using console methods and DevTools breakpoints

**Exercises**

**4.3.1** — Score yourself against the checklist. For each "not yet", spend 30 minutes on targeted practice before the weekend workshop.

**4.3.2** — Build a "Movie Search" app: search input calls the OMDB API, results render as cards, clicking a card shows details in a modal, recent searches persist in localStorage. This should take 2–4 hours.
