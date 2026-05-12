# React

**Track:** React
**Modules:** 4
**Total Lessons:** 14
**Prerequisite:** Courses 1–4

## Module 1 — React Fundamentals

### Lesson 1.1 — Why React Exists

**The vanilla JS problem at scale:**

```javascript
// When state changes in vanilla JS, you must manually update every piece of UI
function renderCart(items) {
  const count    = document.querySelector("#cart-count");
  const total    = document.querySelector("#cart-total");
  const list     = document.querySelector("#cart-list");
  const emptyMsg = document.querySelector("#cart-empty");

  count.textContent = items.length;
  total.textContent = `$${items.reduce((s, i) => s + i.price, 0)}`;
  emptyMsg.hidden   = items.length > 0;
  list.innerHTML    = "";
  items.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item.name;
    list.appendChild(li);
  });
}

// Every time anything changes, you call renderCart() manually
// Forget one call → UI is out of sync with state
```

**React's approach — declare what the UI should look like:**

```jsx
function Cart({ items }) {
  // Describe the UI for this state — React handles the DOM
  return (
    <div>
      <span id="cart-count">{items.length}</span>
      <span id="cart-total">${items.reduce((s, i) => s + i.price, 0)}</span>
      {items.length === 0
        ? <p>Your cart is empty</p>
        : <ul>{items.map(item => <li key={item.id}>{item.name}</li>)}</ul>
      }
    </div>
  );
}
```

When `items` changes, React automatically figures out the minimum DOM updates needed. You never touch the DOM directly.

**Vite setup:**

```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

```
my-app/
├── public/
├── src/
│   ├── App.jsx          ← Root component
│   ├── main.jsx         ← Entry point — mounts React to #root
│   └── index.css
├── index.html           ← Contains <div id="root">
└── vite.config.js
```

**Install React DevTools** browser extension — adds a Components panel to DevTools so you can inspect the component tree, props, and state.

**Exercises**

**1.1.1** — Create a Vite project. Delete all starter content. Create `App.jsx` that renders a heading with your name and a paragraph with your bio. Verify it appears in the browser.

**1.1.2** — Open React DevTools → Components panel. Inspect the `App` component. What do you see?

### Lesson 1.2 — JSX & Components

**JSX rules:**

```jsx
// Use className (not class)
<div className="card">

// Self-close void elements
<img src="..." alt="..." />
<input type="text" />

// Wrap multiple elements — use Fragment (no DOM node)
<>
  <h1>Title</h1>
  <p>Body</p>
</>

// Embed JavaScript with {}
<p>Score: {score}</p>
<p>Name: {user.name.toUpperCase()}</p>
<p>Double: {n * 2}</p>

// Inline styles are objects (camelCase)
<div style={{ backgroundColor: "#1A56A0", fontSize: "24px" }}>

// Event handlers
<button onClick={handleClick}>Click</button>
<input onChange={e => setValue(e.target.value)} />

// camelCase HTML attributes
<label htmlFor="email">Email</label>
<div tabIndex={0}>
```

**Function components:**

```jsx
// Simple component
function Greeting() {
  return <h1>Hello, world!</h1>;
}

// With props — destructured in parameter
function Greeting({ name, role = "student" }) {
  return <h1>Hello, {name} ({role})!</h1>;
}

// Usage — components start with uppercase
<Greeting name="Sam" role="instructor" />
```

**Props and composition:**

```jsx
// Parent passes props
function App() {
  return (
    <div className="app">
      <Header title="Frontend AI Cohort" />
      <StageList stages={cohortStages} />
    </div>
  );
}

// Children prop — content between tags
function Card({ title, children }) {
  return (
    <div className="card">
      <h3 className="card-title">{title}</h3>
      <div className="card-body">{children}</div>
    </div>
  );
}

<Card title="Stage 1">
  <p>Web Fundamentals — weeks 1–8</p>
  <ul><li>HTML</li><li>CSS</li></ul>
</Card>
```

**Rendering lists:**

```jsx
const stages = [
  { id: 1, name: "Web Fundamentals", weeks: "1–8" },
  { id: 2, name: "React",            weeks: "9–14" },
];

function StageList({ stages }) {
  return (
    <ul>
      {stages.map(stage => (
        // key is required — use a stable ID, never the array index
        <StageItem key={stage.id} stage={stage} />
      ))}
    </ul>
  );
}

function StageItem({ stage }) {
  return <li>{stage.name} — Weeks {stage.weeks}</li>;
}
```

**Conditional rendering:**

```jsx
function UserStatus({ user, isLoading }) {
  if (isLoading) return <Spinner />;
  if (!user)     return <p>Please log in.</p>;

  return (
    <div>
      {/* && — renders right side only if left is truthy */}
      {user.isAdmin && <Badge label="Admin" />}

      {/* Ternary — one of two options */}
      <span>{user.isOnline ? "🟢 Online" : "⚫ Offline"}</span>

      {/* Dynamic className */}
      <div className={`card ${user.isPremium ? "card--premium" : ""}`}>
        {user.name}
      </div>
    </div>
  );
}
```

**Exercises**

**1.2.1** — Build a `ProfileCard` component with `name`, `role`, `bio`, and `avatar` props. Use it three times in `App.jsx` with different data. Add a default value for `role`.

**1.2.2** — Build a `StageList` from an array of stage objects. Each stage card should show: name, weeks, description, and a colour-coded badge. Conditionally add a "Current" badge on one stage.

### Lesson 1.3 — State with useState

```jsx
import { useState } from "react";

function Counter() {
  // [value, setter] = useState(initialValue)
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>+</button>
      <button onClick={() => setCount(c => c - 1)}>−</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

**Key rules:**
- Call hooks at the top of the component — never inside a loop or condition
- **Never mutate state directly:** `state.name = "x"` or `arr.push(x)` — always use the setter
- Each `setState` call schedules a re-render

**Functional update — when new state depends on previous:**

```jsx
// ❌ May read stale state
setCount(count + 1);

// ✅ Always uses latest state
setCount(prev => prev + 1);
```

**Object state:**

```jsx
const [form, setForm] = useState({ name: "", email: "" });

// Always spread existing state
function handleChange(e) {
  setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));
}
```

**Lifting state up:**

```jsx
// ❌ State in two components — can't share
function SearchBar() {
  const [query, setQuery] = useState("");
}
function ResultsList() {
  // No access to query
}

// ✅ State in the common parent
function SearchPage() {
  const [query, setQuery] = useState("");
  return (
    <>
      <SearchBar query={query} onSearch={setQuery} />
      <ResultsList query={query} />
    </>
  );
}
```

**Exercises**

**1.3.1** — Build a shopping cart: `ProductList` with "Add to cart" buttons and `CartSummary` showing count and total. State lives in `App` and is passed down as props.

**1.3.2** — Build a multi-step enrolment form (3 steps). State tracks current step number and accumulated form data. A step indicator shows progress.

### Lesson 1.4 — useEffect & useRef

```jsx
import { useEffect, useRef, useState } from "react";

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  // Runs once on mount (empty dependency array)
  useEffect(() => {
    console.log("Component mounted");
    return () => console.log("Component unmounted"); // cleanup
  }, []);

  // Runs when userId changes
  useEffect(() => {
    if (!userId) return;
    const controller = new AbortController();

    fetch(`/api/users/${userId}`, { signal: controller.signal })
      .then(r => r.json())
      .then(setUser)
      .catch(err => { if (err.name !== "AbortError") console.error(err); });

    // Cleanup — cancel the fetch if userId changes before it completes
    return () => controller.abort();
  }, [userId]);

  // ← no dependency array = runs on EVERY render (usually wrong)
}
```

**Debouncing with cleanup:**

```jsx
function SearchInput({ onSearch }) {
  const [query, setQuery] = useState("");

  useEffect(() => {
    const timer = setTimeout(() => onSearch(query), 400);
    return () => clearTimeout(timer);  // cancel previous timer
  }, [query]);

  return <input value={query} onChange={e => setQuery(e.target.value)} />;
}
```

**useRef:**

```jsx
function AutoFocusInput() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();  // focus on mount
  }, []);

  return <input ref={inputRef} />;
}

// Store mutable value without triggering re-render
function Timer() {
  const [elapsed, setElapsed] = useState(0);
  const intervalRef = useRef(null);

  const start = () => {
    intervalRef.current = setInterval(() => setElapsed(e => e + 1), 1000);
  };
  const stop = () => clearInterval(intervalRef.current);

  return (
    <>
      <p>{elapsed}s</p>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </>
  );
}
```

**Exercises**

**1.4.1** — Build a clock showing the current time, updating every second. The interval must be cleaned up when the component unmounts.

**1.4.2** — Build a "typing indicator" that shows "Searching..." 400ms after the user starts typing and disappears when typing stops. Use `useEffect` with cleanup.

## Module 2 — Routing & Navigation

### Lesson 2.1 — React Router Setup & Basic Routing

```bash
npm install react-router-dom
```

```jsx
// main.jsx
import { BrowserRouter } from "react-router-dom";
ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter><App /></BrowserRouter>
);

// App.jsx
import { Routes, Route } from "react-router-dom";
import Layout     from "./components/Layout";
import Home       from "./pages/Home";
import Curriculum from "./pages/Curriculum";
import NotFound   from "./pages/NotFound";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="curriculum" element={<Curriculum />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}

// Layout.jsx — nested routes render inside <Outlet>
import { Outlet } from "react-router-dom";
function Layout() {
  return (
    <>
      <Header />
      <main><Outlet /></main>
      <Footer />
    </>
  );
}
```

**Navigation:**

```jsx
import { Link, NavLink, useNavigate } from "react-router-dom";

// NavLink adds 'active' class automatically
<NavLink
  to="/curriculum"
  className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}
>
  Curriculum
</NavLink>

// Programmatic navigation
const navigate = useNavigate();
navigate("/dashboard");
navigate(-1);  // browser back
navigate("/home", { replace: true });  // replace history entry
```

**Exercises**

**2.1.1** — Add React Router to your app. Create Home, Curriculum, and About pages inside a shared Layout. NavLinks should show the active state visually.

### Lesson 2.2 — URL Parameters & Query Strings

```jsx
import { useParams, useSearchParams } from "react-router-dom";

// Route: /modules/:moduleId/lessons/:lessonId
function LessonPage() {
  const { moduleId, lessonId } = useParams();
  return <h1>Module {moduleId} — Lesson {lessonId}</h1>;
}

// URL: /search?q=react&sort=recent
function SearchPage() {
  const [params, setParams] = useSearchParams();
  const query = params.get("q")    || "";
  const sort  = params.get("sort") || "relevant";

  function handleSearch(e) {
    e.preventDefault();
    setParams({ q: e.target.query.value, sort });
    // URL updates automatically — shareable, bookmarkable
  }

  return (
    <form onSubmit={handleSearch}>
      <input name="query" defaultValue={query} />
      <select name="sort" defaultValue={sort}>
        <option value="relevant">Relevant</option>
        <option value="recent">Recent</option>
      </select>
      <button>Search</button>
    </form>
  );
}
```

**Exercises**

**2.2.1** — Build a products page where clicking a product navigates to `/products/:id`. The detail page fetches that product's data using the ID from `useParams`.

**2.2.2** — Add search and filter to the products list. Store `query` and `category` in the URL with `useSearchParams`. The filtered state should survive a page refresh.

### Lesson 2.3 — Protected Routes

```jsx
import { Navigate, Outlet, useLocation } from "react-router-dom";

// ProtectedRoute — wraps routes that require authentication
function ProtectedRoute() {
  const { user, isLoading } = useAuth();
  const location = useLocation();

  if (isLoading) return <FullPageSpinner />;

  if (!user) {
    // Remember where the user wanted to go
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return <Outlet />;
}

// App.jsx
<Route element={<ProtectedRoute />}>
  <Route path="dashboard" element={<Dashboard />} />
  <Route path="settings"  element={<Settings />} />
</Route>

// Login page — redirect back after login
function LoginPage() {
  const { login }  = useAuth();
  const navigate   = useNavigate();
  const location   = useLocation();
  const from       = location.state?.from?.pathname || "/dashboard";

  async function handleSubmit(data) {
    await login(data);
    navigate(from, { replace: true });
  }
}
```

**Exercises**

**2.3.1** — Implement a protected route. Create a mock `useAuth` hook that reads from localStorage. Unauthenticated users are redirected to `/login`. After "logging in", they return to the page they tried to visit.

## Module 3 — State Management & Data Fetching

### Lesson 3.1 — Context API & Custom Hooks

```jsx
import { createContext, useContext, useState } from "react";

// 1. Create context
const AuthContext = createContext(null);

// 2. Provider
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  async function login({ email, password }) {
    const u = await api.login(email, password);
    setUser(u);
  }
  function logout() { setUser(null); }

  return (
    <AuthContext.Provider value={{ user, login, logout, isLoggedIn: !!user }}>
      {children}
    </AuthContext.Provider>
  );
}

// 3. Hook
function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}

// 4. Usage anywhere in the tree
function Header() {
  const { user, logout } = useAuth();
  return user
    ? <button onClick={logout}>Sign out ({user.name})</button>
    : <Link to="/login">Sign in</Link>;
}
```

**Custom hooks:**

```jsx
// useLocalStorage — persist state
function useLocalStorage(key, initial) {
  const [value, setValue] = useState(() => {
    try { return JSON.parse(localStorage.getItem(key)) ?? initial; }
    catch { return initial; }
  });
  function set(v) {
    setValue(v);
    localStorage.setItem(key, JSON.stringify(v));
  }
  return [value, set];
}

// useDebounce — delay updates
function useDebounce(value, ms = 400) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), ms);
    return () => clearTimeout(t);
  }, [value, ms]);
  return debounced;
}

// useMediaQuery — responsive logic in JS
function useMediaQuery(query) {
  const [matches, setMatches] = useState(() => window.matchMedia(query).matches);
  useEffect(() => {
    const mq = window.matchMedia(query);
    const handler = e => setMatches(e.matches);
    mq.addEventListener("change", handler);
    return () => mq.removeEventListener("change", handler);
  }, [query]);
  return matches;
}
```

**Exercises**

**3.1.1** — Build a `ThemeContext` that provides `theme` and `toggleTheme`. Wrap the app in the provider. At least three different components use the theme — all update simultaneously when toggled.

**3.1.2** — Build a `useForm(initialValues)` custom hook that returns `values`, `handleChange`, `handleSubmit(onSubmit)`, `errors`, and `reset`. Use it in two different forms.

### Lesson 3.2 — Zustand for Global State

```bash
npm install zustand
```

```jsx
import { create }   from "zustand";
import { persist }  from "zustand/middleware";

const useCartStore = create(
  persist(
    (set, get) => ({
      items: [],

      addItem(product) {
        const existing = get().items.find(i => i.id === product.id);
        if (existing) {
          set({ items: get().items.map(i =>
            i.id === product.id ? { ...i, qty: i.qty + 1 } : i
          )});
        } else {
          set({ items: [...get().items, { ...product, qty: 1 }] });
        }
      },

      removeItem: (id) => set({ items: get().items.filter(i => i.id !== id) }),

      updateQty(id, qty) {
        if (qty <= 0) { get().removeItem(id); return; }
        set({ items: get().items.map(i => i.id === id ? { ...i, qty } : i) });
      },

      clear: () => set({ items: [] }),

      get total()     { return get().items.reduce((s, i) => s + i.price * i.qty, 0); },
      get itemCount() { return get().items.reduce((s, i) => s + i.qty, 0); },
    }),
    { name: "cart" }  // localStorage key
  )
);

// Usage — no Provider needed
function CartBadge() {
  // Selectors prevent re-renders when unrelated state changes
  const itemCount = useCartStore(s => s.itemCount);
  return <span className="badge">{itemCount}</span>;
}

function AddToCartButton({ product }) {
  const addItem = useCartStore(s => s.addItem);
  return <button onClick={() => addItem(product)}>Add to cart</button>;
}
```

**Exercises**

**3.2.1** — Build a complete cart with Zustand: add items, remove items, update quantity, clear cart, total and item count. Persist to localStorage. The cart survives a page refresh.

### Lesson 3.3 — TanStack Query

```bash
npm install @tanstack/react-query
```

```jsx
// main.jsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
const qc = new QueryClient({ defaultOptions: { queries: { staleTime: 5 * 60 * 1000 } } });
<QueryClientProvider client={qc}><App /></QueryClientProvider>
```

**useQuery:**

```jsx
function UserProfile({ userId }) {
  const { data: user, isLoading, isError, error, refetch } = useQuery({
    queryKey: ["user", userId],
    queryFn:  () => apiFetch(`/api/users/${userId}`),
    enabled:  !!userId,
  });

  if (isLoading) return <Skeleton />;
  if (isError)   return <ErrorCard message={error.message} onRetry={refetch} />;

  return <div><h1>{user.name}</h1><p>{user.email}</p></div>;
}
```

**useMutation with optimistic updates:**

```jsx
function TodoItem({ todo }) {
  const qc = useQueryClient();

  const { mutate: toggleTodo } = useMutation({
    mutationFn: (t) => apiFetch(`/api/todos/${t.id}`, {
      method:  "PATCH",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ done: !t.done }),
    }),

    onMutate: async (todo) => {
      await qc.cancelQueries({ queryKey: ["todos"] });
      const prev = qc.getQueryData(["todos"]);
      qc.setQueryData(["todos"], old =>
        old.map(t => t.id === todo.id ? { ...t, done: !t.done } : t)
      );
      return { prev };
    },

    onError:   (_, __, ctx) => qc.setQueryData(["todos"], ctx.prev),
    onSettled: () => qc.invalidateQueries({ queryKey: ["todos"] }),
  });

  return (
    <li onClick={() => toggleTodo(todo)} className={todo.done ? "done" : ""}>
      {todo.title}
    </li>
  );
}
```

**Exercises**

**3.3.1** — Use `useQuery` to build a user directory fetched from an API. Show a skeleton while loading, error with retry on failure, empty state when no results.

**3.3.2** — Add `useMutation` to create a new user. On success, add them to the list using `setQueryData`. Show loading state on the button.

### Lesson 3.4 — Forms with React Hook Form & Zod

```bash
npm install react-hook-form zod @hookform/resolvers
```

```jsx
import { useForm }      from "react-hook-form";
import { z }            from "zod";
import { zodResolver }  from "@hookform/resolvers/zod";

const schema = z.object({
  name:     z.string().min(2, "Name must be at least 2 characters"),
  email:    z.string().email("Please enter a valid email"),
  password: z.string()
    .min(8, "At least 8 characters")
    .regex(/[0-9]/, "Must include a number"),
  confirm:  z.string(),
}).refine(d => d.password === d.confirm, {
  path:    ["confirm"],
  message: "Passwords do not match",
});

function RegisterForm() {
  const {
    register, handleSubmit,
    formState: { errors, isSubmitting },
    setError, reset,
  } = useForm({ resolver: zodResolver(schema) });

  async function onSubmit(data) {
    try {
      await registerUser(data);
      reset();
    } catch (err) {
      setError("email", { message: "Email already registered" });
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} noValidate>
      <div className="field">
        <label htmlFor="name">Full name</label>
        <input id="name" {...register("name")} aria-invalid={!!errors.name} />
        {errors.name && <p className="error">{errors.name.message}</p>}
      </div>

      <div className="field">
        <label htmlFor="email">Email</label>
        <input id="email" type="email" {...register("email")} aria-invalid={!!errors.email} />
        {errors.email && <p className="error">{errors.email.message}</p>}
      </div>

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Creating account…" : "Create account"}
      </button>
    </form>
  );
}
```

**Exercises**

**3.4.1** — Build a "Book a session" form with RHF + Zod: name, email, date (future only), time slot (select), message (optional, max 500 chars with counter). All validated.

**3.4.2** — Add a settings form with pre-populated `defaultValues` loaded from a user object. Validate and save on submit.

## Module 4 — Styling & Production

### Lesson 4.1 — Tailwind CSS

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

```javascript
// tailwind.config.js
export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: { extend: {} },
  plugins: [],
};
```

```css
/* index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**Usage:**

```jsx
function Card({ title, description, badge, href }) {
  return (
    <a href={href}
       className="group block rounded-xl border border-gray-200 bg-white p-6
                  shadow-sm transition-all duration-200
                  hover:border-violet-300 hover:shadow-md
                  dark:border-gray-700 dark:bg-gray-800 dark:hover:border-violet-500">
      <span className="mb-3 inline-block rounded-full bg-violet-100 px-3 py-1
                       text-xs font-semibold text-violet-700">
        {badge}
      </span>
      <h3 className="mb-2 text-lg font-semibold text-gray-900
                     group-hover:text-violet-600 dark:text-white">
        {title}
      </h3>
      <p className="text-sm text-gray-500 dark:text-gray-400">
        {description}
      </p>
    </a>
  );
}

// Responsive utilities
<div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
// mobile: 1 col | sm (640px): 2 cols | lg (1024px): 3 cols
```

**Exercises**

**4.1.1** — Install Tailwind. Rebuild your ProfileCard using only Tailwind utilities — no custom CSS file. Include hover, focus, and dark mode variants.

### Lesson 4.2 — shadcn/ui

```bash
npx shadcn@latest init
npx shadcn@latest add button input card dialog badge select label
```

```jsx
import { Button }  from "@/components/ui/button";
import { Input }   from "@/components/ui/input";
import { Label }   from "@/components/ui/label";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter }
                   from "@/components/ui/card";
import { Badge }   from "@/components/ui/badge";
import { Dialog, DialogTrigger, DialogContent, DialogHeader, DialogTitle }
                   from "@/components/ui/dialog";

function LessonCard({ lesson }) {
  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>{lesson.title}</CardTitle>
          <Badge variant={lesson.completed ? "default" : "secondary"}>
            {lesson.completed ? "Complete" : "In progress"}
          </Badge>
        </div>
        <CardDescription>{lesson.module}</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-muted-foreground">{lesson.description}</p>
      </CardContent>
      <CardFooter>
        <Dialog>
          <DialogTrigger asChild>
            <Button>Start lesson</Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>{lesson.title}</DialogTitle>
            </DialogHeader>
            <LessonContent lesson={lesson} />
          </DialogContent>
        </Dialog>
      </CardFooter>
    </Card>
  );
}
```

**Exercises**

**4.2.1** — Install shadcn/ui. Build a login form with `Card`, `Input`, `Label`, and `Button`. Connect to React Hook Form + Zod.

**4.2.2** — Build a dashboard: sidebar with shadcn `Button` nav items, main area with shadcn `Card` components, and a `Dialog` that opens on click.

### Lesson 4.3 — Performance & Production Checklist

```jsx
import { useMemo, useCallback, memo } from "react";

// useMemo — memoize expensive computations
function ProductList({ products, query }) {
  const filtered = useMemo(() =>
    products.filter(p =>
      p.name.toLowerCase().includes(query.toLowerCase())
    ),
    [products, query]  // only recomputes when these change
  );
  return <ul>{filtered.map(p => <ProductItem key={p.id} product={p} />)}</ul>;
}

// useCallback — memoize functions passed as props
function Parent() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    console.log("clicked");
  }, []);  // stable reference — won't cause child re-renders

  return (
    <>
      <button onClick={() => setCount(c => c + 1)}>Re-render parent</button>
      <Child onClick={handleClick} />
    </>
  );
}

// memo — skip re-render if props haven't changed
const Child = memo(function Child({ onClick }) {
  console.log("Child rendered");  // only logs when onClick changes
  return <button onClick={onClick}>Click</button>;
});
```

**Production deployment to Vercel:**

```bash
# Build
npm run build

# Preview build locally
npm run preview

# Deploy (install Vercel CLI once)
npm install -g vercel
vercel
```

Or: push to GitHub → Vercel auto-deploys every push to `main`.

**Pre-deployment checklist:**
- [ ] `npm run build` completes with no errors
- [ ] All environment variables set in Vercel dashboard
- [ ] No `console.log` in production code
- [ ] Images have `width` and `height` or `aspect-ratio`
- [ ] Error boundaries in place for AI/async components
- [ ] Lighthouse Performance ≥ 80

**Exercises**

**4.3.1** — Add `useMemo` to a filtered/sorted list. Open React DevTools → Profiler. Record an interaction. Compare render counts before and after memoization.

**4.3.2** — Deploy your Stage 2 e-commerce project to Vercel. Share the live URL in the community.
