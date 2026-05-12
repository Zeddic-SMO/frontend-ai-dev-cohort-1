# Frontend AI Development

**Track:** Frontend AI
**Modules:** 4
**Total Lessons:** 14
**Prerequisite:** Course 5 — React

## Module 1 — Understanding LLMs

### Lesson 1.1 — How LLMs Work

**What is an LLM?**

A Large Language Model predicts the most probable next token given everything before it. That simple mechanism, trained on hundreds of billions of text tokens, produces a system that can write code, answer questions, analyse images, and have complex conversations.

**Tokens:**

LLMs don't read words — they read tokens. A token is roughly 3–4 characters or 0.75 words.

```
"Hello, world!"         → 4 tokens
"Frontend Development"  → 3 tokens
"useCallback"           → 2 tokens
"Sam"                   → 1 token
```

Why this matters for you as a developer:
- **Cost** — you pay per token (input + output)
- **Speed** — more tokens = slower response
- **Limit** — every model has a maximum context window

Rule of thumb: 1,000 tokens ≈ 750 words ≈ 3 pages.

**Context window:**

Everything the model can "see" at once: system prompt + conversation history + current message. If the total exceeds the limit, older messages are dropped.

```
Claude Sonnet: 200,000 tokens (~150,000 words)
GPT-4o:        128,000 tokens (~96,000 words)
```

For a chat application, you must manage the conversation history — you cannot pass unlimited history.

**Temperature:**

| Value | Behaviour | Use case |
|-------|-----------|----------|
| 0.0 | Deterministic — same input, same output | Code generation, data extraction |
| 0.3 | Focused but natural | Q&A, summaries |
| 0.7 | Balanced | General chat, analysis |
| 1.0 | Creative | Brainstorming, writing |
| > 1.0 | Unpredictable | Experimental only |

**Streaming:**

```
Non-streaming:               Streaming:
User waits 5 seconds...      Token appears immediately
                             More tokens stream in
Full response appears         Response builds in front of user
```

Always stream for chat interfaces. The first token appears in ~200ms. Without streaming, users stare at a blank page for 3–10 seconds.

**Models:**

| Model | Best for |
|-------|---------|
| `claude-sonnet-4-5` | Default choice — fast, capable, affordable |
| `claude-opus-4-5` | Complex reasoning — use sparingly |
| `claude-haiku-3-5` | High-volume simple tasks — very fast, cheap |
| `gpt-4o` | Multimodal (text + images), great reasoning |
| `gpt-4o-mini` | Budget option for simple tasks |

**Exercises**

**1.1.1** — Sign up for Anthropic API access at console.anthropic.com. Open the API playground. Send a message with temperature 0. Send the same message five times — is it identical each time? Now try temperature 1.

**1.1.2** — Use tiktoken.com to count the tokens in: your bio, this lesson's opening paragraph, and a 1000-word essay. Calculate the approximate cost at Claude Sonnet pricing.

### Lesson 1.2 — Your First API Call

**Why Next.js API routes?** You cannot call Anthropic from the browser — your API key would be visible in DevTools. Next.js routes run on the server.

```
Browser → Next.js API route (server) → Anthropic API
              ↑ key lives here, never exposed to browser
```

```bash
npx create-next-app@latest ai-app --app --tailwind
cd ai-app
npm install ai @ai-sdk/anthropic
```

```bash
# .env.local — NEVER commit this file
ANTHROPIC_API_KEY=sk-ant-api03-...
```

```gitignore
# .gitignore
.env.local
.env
```

**API route:**

```javascript
// app/api/explain/route.js
import { anthropic }    from "@ai-sdk/anthropic";
import { generateText } from "ai";

export async function POST(req) {
  const { code } = await req.json();

  if (!code?.trim()) {
    return Response.json({ error: "Code is required" }, { status: 400 });
  }

  const { text } = await generateText({
    model:       anthropic("claude-sonnet-4-5"),
    system:      "Explain code clearly to a junior developer. Be concise.",
    prompt:      `Explain what this code does:\n\n\`\`\`\n${code}\n\`\`\``,
    maxTokens:   500,
    temperature: 0.3,
  });

  return Response.json({ explanation: text });
}
```

**React component:**

```jsx
// app/page.jsx
"use client";
import { useState } from "react";

export default function ExplainPage() {
  const [code,        setCode]        = useState("");
  const [explanation, setExplanation] = useState("");
  const [status,      setStatus]      = useState("idle");

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus("loading"); setExplanation("");

    try {
      const res  = await fetch("/api/explain", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ code }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error);
      setExplanation(data.explanation);
      setStatus("success");
    } catch (err) {
      setExplanation(err.message);
      setStatus("error");
    }
  }

  return (
    <main className="mx-auto max-w-2xl p-8 space-y-4">
      <h1 className="text-2xl font-bold">Code Explainer</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea value={code} onChange={e => setCode(e.target.value)}
                  rows={10} placeholder="Paste code here..."
                  className="w-full rounded-lg border p-3 font-mono text-sm" />
        <button type="submit" disabled={status === "loading"}
                className="rounded-lg bg-violet-600 px-6 py-2 text-white disabled:opacity-50">
          {status === "loading" ? "Explaining…" : "Explain"}
        </button>
      </form>
      {explanation && (
        <div className={`rounded-lg p-4 text-sm
          ${status === "error" ? "bg-red-50 text-red-700" : "bg-gray-50"}`}>
          {explanation}
        </div>
      )}
    </main>
  );
}
```

**Exercises**

**1.2.1** — Create the code explainer above. Then extend it: add a "language" select (JS, Python, CSS, SQL). Pass the language to the prompt: "Explain this {language} code…"

**1.2.2** — Add a token counter. Log `usage.promptTokens` and `usage.completionTokens` from the `generateText` response. Display them below the explanation.

### Lesson 1.3 — Streaming with the Vercel AI SDK

```javascript
// app/api/chat/route.js
import { anthropic }  from "@ai-sdk/anthropic";
import { streamText } from "ai";

export const maxDuration = 30;

export async function POST(req) {
  const { messages } = await req.json();

  const result = streamText({
    model:   anthropic("claude-sonnet-4-5"),
    system:  `You are a coding assistant for frontend developers.
You help with HTML, CSS, JavaScript, and React.
Always show code examples. Keep responses focused.`,
    messages,
    maxTokens: 1000,
  });

  return result.toDataStreamResponse();
}
```

```jsx
// app/chat/page.jsx
"use client";
import { useChat }           from "ai/react";
import { useRef, useEffect } from "react";
import ReactMarkdown         from "react-markdown";
import remarkGfm             from "remark-gfm";

export default function ChatPage() {
  const { messages, input, handleInputChange, handleSubmit,
          isLoading, error, reload, stop } = useChat({ api: "/api/chat" });

  const bottomRef = useRef(null);
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="flex h-screen flex-col">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <p className="text-center text-gray-400 mt-16">
            Ask anything about frontend development...
          </p>
        )}

        {messages.map(msg => (
          <div key={msg.id}
               className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
            <div className={`max-w-[80%] rounded-2xl px-4 py-3 text-sm
              ${msg.role === "user"
                ? "bg-violet-600 text-white"
                : "bg-gray-100 text-gray-900 prose prose-sm"}`}>
              {msg.role === "user"
                ? <p>{msg.content}</p>
                : <ReactMarkdown remarkPlugins={[remarkGfm]}>{msg.content}</ReactMarkdown>
              }
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="flex justify-start">
            <div className="rounded-2xl bg-gray-100 px-4 py-3">
              <span className="flex gap-1">
                {[0, 100, 200].map(d => (
                  <span key={d} className="animate-bounce" style={{ animationDelay: `${d}ms` }}>●</span>
                ))}
              </span>
            </div>
          </div>
        )}

        {error && (
          <p className="text-center text-red-500 text-sm">
            Something went wrong.{" "}
            <button onClick={reload} className="underline">Retry</button>
          </p>
        )}

        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div className="border-t p-4">
        <form onSubmit={handleSubmit} className="flex gap-3">
          <input value={input} onChange={handleInputChange}
                 placeholder="Ask a question..."
                 className="flex-1 rounded-xl border px-4 py-2 text-sm
                            focus:outline-none focus:ring-2 focus:ring-violet-500" />
          {isLoading
            ? <button type="button" onClick={stop}
                      className="rounded-xl bg-red-500 px-4 py-2 text-white text-sm">
                Stop
              </button>
            : <button type="submit" disabled={!input.trim()}
                      className="rounded-xl bg-violet-600 px-4 py-2 text-white text-sm disabled:opacity-50">
                Send
              </button>
          }
        </form>
      </div>
    </div>
  );
}
```

**Exercises**

**1.3.1** — Build the streaming chat above. Verify tokens appear one by one (not all at once). Add a "Clear conversation" button that calls `setMessages([])`.

**1.3.2** — Add a message count indicator. Add keyboard shortcut: `Ctrl+Enter` sends the message, `Escape` clears the input.

## Module 2 — Prompt Engineering

### Lesson 2.1 — System Prompts

```javascript
// ❌ Weak — no direction
system: "You are a helpful assistant."

// ✅ Strong — persona, purpose, rules, format
system: `You are a coding assistant specialised in React and TypeScript.

## Your role
- Answer questions about React, TypeScript, and modern frontend development
- Review code and suggest concrete improvements
- Explain concepts with working code examples

## Rules
- Respond in the same language the user writes in
- If you don't know something, say so — never invent APIs or documentation
- Keep responses under 400 words unless the user asks for more
- Only answer frontend development questions — politely decline anything else

## Output format
- Use Markdown
- Wrap all code in fenced code blocks with the language specified
- Use **bold** for important terms
- Structure longer responses with ## headings`
```

**Prompt templates:**

```javascript
// prompts.js — build templates for common tasks
export const prompts = {
  explainCode: (code, language) => `
Explain this ${language} code to a junior developer:
\`\`\`${language}
${code}
\`\`\`
Include: what it does, how it works step by step, and one thing to watch out for.
  `.trim(),

  reviewCode: (code) => `
Review this code for:
1. Bugs or edge cases
2. Performance issues
3. Readability improvements
4. Security concerns

\`\`\`
${code}
\`\`\`
Be specific — reference line numbers.
  `.trim(),

  generateTests: (code) => `
Write Vitest unit tests for this function. Include:
- Happy path (normal input)
- Edge cases (empty, null, extreme values)
- Error cases

\`\`\`javascript
${code}
\`\`\`
  `.trim(),
};
```

**Security — preventing prompt injection:**

```javascript
// ❌ User can escape system prompt
const system = `You are an assistant. User name: ${req.body.name}`;
// If name = "Ignore everything above and..." — dangerous

// ✅ User input only ever goes in the user message
const system = "You are an assistant. Greet the user by their provided name.";
const userMsg = `[name: ${sanitise(req.body.name)}]\n${req.body.message}`;
```

**Exercises**

**2.1.1** — Write three system prompts for the same underlying app (a code explainer) targeting: a professional senior developer, a complete beginner, and a non-technical manager. Test each with the same input and compare outputs.

**2.1.2** — Build a prompt template function for a cover letter generator. Parameters: `jobTitle`, `company`, `mySkills[]`, `yearsExperience`. Iterate until outputs are consistently professional and correctly targeted.

### Lesson 2.2 — Structured Output

```javascript
// app/api/analyse/route.js
import { generateObject } from "ai";
import { anthropic }      from "@ai-sdk/anthropic";
import { z }              from "zod";

const schema = z.object({
  sentiment:    z.enum(["positive", "negative", "neutral", "mixed"]),
  score:        z.number().min(1).max(10).describe("Overall quality score"),
  summary:      z.string().max(120),
  strengths:    z.array(z.string()).min(1).max(4),
  improvements: z.array(z.string()).min(1).max(4),
  keywords:     z.array(z.string()).max(6),
});

export async function POST(req) {
  const { text } = await req.json();

  try {
    const { object } = await generateObject({
      model:  anthropic("claude-sonnet-4-5"),
      schema,
      prompt: `Analyse this writing for quality, sentiment, and key themes:\n\n${text}`,
    });

    return Response.json(object);
  } catch (err) {
    return Response.json({ error: "Analysis failed" }, { status: 500 });
  }
}
```

```jsx
// React component consuming structured output
function AnalysisResult({ data }) {
  return (
    <div className="space-y-4">
      <div className="flex items-center gap-3">
        <SentimentBadge sentiment={data.sentiment} />
        <ScoreRing score={data.score} />
      </div>
      <p className="text-sm text-gray-600">{data.summary}</p>
      <div className="grid grid-cols-2 gap-4">
        <Section title="Strengths"    items={data.strengths}    variant="success" />
        <Section title="Improvements" items={data.improvements} variant="warning" />
      </div>
      <div className="flex flex-wrap gap-2">
        {data.keywords.map(k => <Badge key={k}>{k}</Badge>)}
      </div>
    </div>
  );
}
```

**Exercises**

**2.2.1** — Build a product description analyser: user pastes a description, AI returns a structured analysis (target audience, key benefits, tone, SEO keywords, suggested improvements). Render each field with appropriate UI.

**2.2.2** — Build a "quiz generator": user pastes a paragraph of text, AI generates three multiple-choice questions about it with four options and a marked correct answer. Render as an interactive quiz.

### Lesson 2.3 — Few-Shot Prompting & Chain of Thought

**Few-shot prompting — show examples before asking:**

```javascript
const { text } = await generateText({
  model:   anthropic("claude-sonnet-4-5"),
  system:  "Convert component descriptions to Tailwind class lists.",
  messages: [
    { role: "user",      content: "A primary button, medium size, rounded" },
    { role: "assistant", content: "px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 font-medium text-sm" },
    { role: "user",      content: "A danger badge, small, pill shape" },
    { role: "assistant", content: "px-2 py-0.5 bg-red-100 text-red-700 rounded-full text-xs font-medium" },
    { role: "user",      content: userQuery },
  ],
});
```

**Chain of thought — ask the model to reason step by step:**

```javascript
const { text } = await generateText({
  model:  anthropic("claude-sonnet-4-5"),
  prompt: `Debug this React code. Think step by step:
1. What is the code trying to do?
2. What is the actual behaviour?
3. Why does the bug occur?
4. What is the fix?

Code:
\`\`\`jsx
${buggyCode}
\`\`\`

Error: ${errorMessage}`,
});
```

**Exercises**

**2.3.1** — Build a "CSS class suggester" with few-shot prompting. User describes the element they need ("a success notification with icon"); AI returns the exact Tailwind classes. Include 4 example pairs in the prompt.

**2.3.2** — Build a "debugging assistant" using chain-of-thought. User pastes broken code and an error message. AI walks through the analysis step by step before giving the fix.

## Module 3 — AI-Powered Features

### Lesson 3.1 — Content Generation & Smart Fields

**Content generation toolkit:**

```jsx
function ContentToolkit() {
  const [input,  setInput]  = useState("");
  const [output, setOutput] = useState("");
  const [tool,   setTool]   = useState("title");
  const [loading,setLoading]= useState(false);

  const tools = {
    title: {
      label:  "Generate titles",
      prompt: (text) => `Generate 5 compelling blog post titles for this topic: "${text}"\nReturn as a numbered list.`,
    },
    outline: {
      label:  "Create outline",
      prompt: (text) => `Create a 6-point blog post outline for: "${text}"\nInclude an intro, 4 main points, and a conclusion.`,
    },
    meta: {
      label:  "Write meta description",
      prompt: (text) => `Write an SEO meta description (max 155 characters) for a blog post about: "${text}"`,
    },
  };

  async function generate() {
    setLoading(true); setOutput("");
    const res  = await fetch("/api/generate", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ prompt: tools[tool].prompt(input) }),
    });
    const data = await res.json();
    setOutput(data.text);
    setLoading(false);
  }

  return (
    <div className="space-y-4">
      <div className="flex gap-2">
        {Object.entries(tools).map(([key, t]) => (
          <button key={key} onClick={() => setTool(key)}
                  className={`rounded-full px-4 py-1.5 text-sm
                    ${tool === key ? "bg-violet-600 text-white" : "border"}`}>
            {t.label}
          </button>
        ))}
      </div>
      <textarea value={input} onChange={e => setInput(e.target.value)}
                rows={3} placeholder="Describe your topic..."
                className="w-full rounded-lg border p-3 text-sm" />
      <button onClick={generate} disabled={loading || !input.trim()}
              className="rounded-lg bg-violet-600 px-4 py-2 text-white text-sm disabled:opacity-50">
        {loading ? "Generating…" : "Generate"}
      </button>
      {output && (
        <div className="rounded-lg bg-gray-50 p-4 text-sm whitespace-pre-wrap">
          {output}
        </div>
      )}
    </div>
  );
}
```

**AI-assisted form field:**

```jsx
function BioField() {
  const [bio,     setBio]     = useState("");
  const [options, setOptions] = useState([]);
  const [loading, setLoading] = useState(false);

  async function improveWithAI() {
    setLoading(true);
    const res  = await fetch("/api/improve-bio", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ bio }),
    });
    const data = await res.json();
    setOptions(data.suggestions);
    setLoading(false);
  }

  return (
    <div className="space-y-2">
      <label className="text-sm font-medium">Your bio</label>
      <textarea value={bio} onChange={e => setBio(e.target.value)} rows={3}
                className="w-full rounded-lg border p-3 text-sm" />
      <div className="flex justify-between text-xs text-gray-400">
        <span>{bio.length} / 160</span>
        <button onClick={improveWithAI} disabled={loading || !bio}
                className="text-violet-600 underline disabled:opacity-50">
          {loading ? "Improving…" : "✨ Improve with AI"}
        </button>
      </div>
      {options.map((opt, i) => (
        <div key={i} onClick={() => { setBio(opt); setOptions([]); }}
             className="cursor-pointer rounded-lg border p-3 text-sm
                        hover:border-violet-400 hover:bg-violet-50">
          {opt}
        </div>
      ))}
    </div>
  );
}
```

**Exercises**

**3.1.1** — Build the content generation toolkit above. Add a fourth tool: "social post" (Twitter/LinkedIn-length post about the topic).

**3.1.2** — Add an AI-improve button to three different form fields in your project. Each should offer three alternatives. Clicking an alternative replaces the field value.

### Lesson 3.2 — Image Analysis

```javascript
// app/api/analyse-image/route.js
import { generateText } from "ai";
import { anthropic }    from "@ai-sdk/anthropic";

export async function POST(req) {
  const formData = await req.formData();
  const image    = formData.get("image");
  const task     = formData.get("task") || "describe";

  const allowed = ["image/jpeg", "image/png", "image/gif", "image/webp"];
  if (!allowed.includes(image.type)) {
    return Response.json({ error: "Please upload JPEG, PNG, GIF, or WebP" }, { status: 400 });
  }
  if (image.size > 5 * 1024 * 1024) {
    return Response.json({ error: "Image must be under 5MB" }, { status: 400 });
  }

  const prompts = {
    describe: "Describe this image in detail.",
    alt:      "Write a concise, descriptive alt text for this image (under 125 characters). Return only the alt text, no preamble.",
    extract:  "Extract all text visible in this image. Return the exact text, preserving layout where possible.",
    analyse:  "Analyse this image: describe the composition, colours, mood, and any notable elements.",
  };

  const buffer = Buffer.from(await image.arrayBuffer());
  const base64 = buffer.toString("base64");

  const { text } = await generateText({
    model:    anthropic("claude-sonnet-4-5"),
    messages: [{
      role:    "user",
      content: [
        { type: "image", source: { type: "base64", mediaType: image.type, data: base64 } },
        { type: "text",  text: prompts[task] },
      ],
    }],
  });

  return Response.json({ result: text });
}
```

```jsx
function ImageAnalyser() {
  const [preview, setPreview] = useState(null);
  const [file,    setFile]    = useState(null);
  const [result,  setResult]  = useState("");
  const [task,    setTask]    = useState("describe");
  const [loading, setLoading] = useState(false);

  const tasks = [
    { id: "describe", label: "Describe" },
    { id: "alt",      label: "Generate alt text" },
    { id: "extract",  label: "Extract text" },
    { id: "analyse",  label: "Analyse composition" },
  ];

  function handleFile(e) {
    const f = e.target.files[0];
    if (!f) return;
    setFile(f);
    setPreview(URL.createObjectURL(f));
    setResult("");
  }

  async function analyse() {
    if (!file) return;
    setLoading(true); setResult("");
    const fd = new FormData();
    fd.append("image", file);
    fd.append("task",  task);
    const res  = await fetch("/api/analyse-image", { method: "POST", body: fd });
    const data = await res.json();
    setResult(data.error || data.result);
    setLoading(false);
  }

  return (
    <div className="space-y-4">
      <input type="file" accept="image/*" onChange={handleFile} className="text-sm" />
      {preview && <img src={preview} alt="Upload preview" className="max-w-sm rounded-lg" />}
      <div className="flex flex-wrap gap-2">
        {tasks.map(t => (
          <button key={t.id} onClick={() => setTask(t.id)}
                  className={`rounded-full px-3 py-1 text-sm
                    ${task === t.id ? "bg-violet-600 text-white" : "border"}`}>
            {t.label}
          </button>
        ))}
      </div>
      <button onClick={analyse} disabled={!file || loading}
              className="rounded-lg bg-violet-600 px-4 py-2 text-white text-sm disabled:opacity-50">
        {loading ? "Analysing…" : "Analyse"}
      </button>
      {result && <div className="rounded-lg bg-gray-50 p-4 text-sm">{result}</div>}
    </div>
  );
}
```

**Exercises**

**3.2.1** — Build the image analyser above. Add a fifth task: "is this image accessible?" — have the AI assess the image for accessibility considerations.

### Lesson 3.3 — Voice Input & Tool Calling

**Voice input:**

```jsx
function VoiceMicButton({ onTranscript }) {
  const [listening, setListening] = useState(false);
  const recog    = useRef(null);
  const supported = "webkitSpeechRecognition" in window || "SpeechRecognition" in window;

  function toggle() {
    if (listening) {
      recog.current?.stop();
    } else {
      const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
      const r  = new SR();
      r.continuous     = false;
      r.interimResults = true;
      r.lang           = "en-US";
      r.onstart  = () => setListening(true);
      r.onend    = () => setListening(false);
      r.onresult = e => {
        const text  = [...e.results].map(r => r[0].transcript).join("");
        const final = e.results[e.results.length - 1].isFinal;
        onTranscript(text, final);
      };
      recog.current = r;
      r.start();
    }
  }

  if (!supported) return null;

  return (
    <button type="button" onClick={toggle} aria-label={listening ? "Stop" : "Voice input"}
            className={`rounded-full p-2 transition
              ${listening
                ? "animate-pulse bg-red-500 text-white"
                : "bg-gray-100 text-gray-600 hover:bg-gray-200"}`}>
      🎤
    </button>
  );
}
```

**Tool calling:**

```javascript
// app/api/chat-tools/route.js
import { anthropic }          from "@ai-sdk/anthropic";
import { streamText, tool }   from "ai";
import { z }                  from "zod";

export async function POST(req) {
  const { messages } = await req.json();

  const result = streamText({
    model:   anthropic("claude-sonnet-4-5"),
    system:  "You are a helpful assistant. Use tools when the user asks for current information.",
    messages,
    tools: {
      getCurrentTime: tool({
        description: "Get the current time in a timezone",
        parameters:  z.object({
          timezone: z.string().describe("IANA timezone, e.g. Africa/Lagos"),
        }),
        execute: async ({ timezone }) => ({
          time: new Intl.DateTimeFormat("en", {
            timeZone:  timezone,
            timeStyle: "short",
            dateStyle: "medium",
          }).format(new Date()),
        }),
      }),

      getWeather: tool({
        description: "Get weather for a city",
        parameters:  z.object({ city: z.string() }),
        execute:     async ({ city }) => {
          const res  = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${process.env.WEATHER_KEY}`
          );
          const data = await res.json();
          return { city: data.name, temp: Math.round(data.main.temp), desc: data.weather[0].description };
        },
      }),
    },
  });

  return result.toDataStreamResponse();
}
```

**Exercises**

**3.3.1** — Add voice input to your chat. Clicking the mic starts listening; when the user stops speaking, the transcript populates the input and submits automatically.

**3.3.2** — Add three tools to your chat: `getTime`, `calculateAge` (birthdate → years and days old), and `convertUnits` (e.g. kg to lb, km to miles). Test each by asking the AI naturally.

### Lesson 3.4 — Smart Search

```javascript
// app/api/smart-search/route.js
import { generateObject } from "ai";
import { anthropic }      from "@ai-sdk/anthropic";
import { z }              from "zod";

const intentSchema = z.object({
  keywords: z.array(z.string()).max(5),
  intent:   z.string(),
  filters:  z.object({
    maxPrice: z.number().optional(),
    category: z.string().optional(),
    inStock:  z.boolean().optional(),
  }),
});

// Simple in-memory cache
const cache = new Map();

export async function POST(req) {
  const { query } = await req.json();

  if (cache.has(query)) {
    return Response.json({ intent: cache.get(query) });
  }

  const { object } = await generateObject({
    model:  anthropic("claude-haiku-3-5"),  // haiku for fast, cheap extraction
    schema: intentSchema,
    prompt: `Extract search intent and filters from this e-commerce query: "${query}"`,
  });

  cache.set(query, object);
  return Response.json({ intent: object });
}
```

```jsx
function SmartSearch({ products }) {
  const [query,   setQuery]   = useState("");
  const [results, setResults] = useState(products);
  const [intent,  setIntent]  = useState(null);
  const [loading, setLoading] = useState(false);

  const debouncedQuery = useDebounce(query, 500);

  useEffect(() => {
    if (!debouncedQuery) { setResults(products); setIntent(null); return; }
    search(debouncedQuery);
  }, [debouncedQuery]);

  async function search(q) {
    setLoading(true);
    const res  = await fetch("/api/smart-search", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ query: q }),
    });
    const { intent: ai } = await res.json();
    setIntent(ai);

    const filtered = products.filter(p => {
      const matchKw    = ai.keywords.some(k =>
        p.name.toLowerCase().includes(k) || p.description?.toLowerCase().includes(k)
      );
      const matchPrice = !ai.filters.maxPrice || p.price <= ai.filters.maxPrice;
      const matchStock = ai.filters.inStock === undefined || p.inStock === ai.filters.inStock;
      return matchKw && matchPrice && matchStock;
    });

    setResults(filtered);
    setLoading(false);
  }

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)}
             placeholder='Try: "cheap courses under $30" or "in-stock books"'
             className="w-full rounded-xl border px-4 py-3" />
      {intent && (
        <p className="mt-2 text-xs text-gray-400">
          Understood: {intent.intent} · {results.length} results
        </p>
      )}
      <ProductGrid products={results} />
    </div>
  );
}
```

**Exercises**

**3.4.1** — Build the smart search above for a product list. Test it with natural language queries like "something cheap for beginners", "advanced courses only", "under twenty dollars in stock".

## Module 4 — AI Developer Workflow

### Lesson 4.1 — Claude Code

```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Start in your project directory
claude
```

**High-value Claude Code prompts:**

```bash
# Scaffold
> Scaffold a React component called SearchableProductList.
  It accepts a `products` prop (array of { id, name, price, category }).
  Features: search input (filter by name), category filter (select),
  sort by price (asc/desc), and renders each as a shadcn Card.
  Use Tailwind CSS and TypeScript. Include the full file.

# Refactor
> Refactor ProductCard.jsx to use React Hook Form instead
  of manual controlled inputs. Keep the same props interface.

# Debug
> This component causes infinite re-renders.
  Here is the code: [paste]. Here is the error: [paste].
  Explain the cause and fix it.

# Tests
> Write Vitest unit tests for useCartStore (Zustand).
  Test: addItem (new item, existing item increments qty),
  removeItem, updateQty (to 0 removes item), total, itemCount.
```

**Rules for using Claude Code effectively:**
- Be specific about your stack: "using React 18, Tailwind, shadcn/ui, TypeScript"
- Always review generated code before running it
- Ask for explanations: "refactor this AND explain each change"
- Use for boilerplate, not for complex business logic you don't understand

**Exercises**

**4.1.1** — Use Claude Code to scaffold the complete file structure for your capstone project. Ask for: folder structure, base components, API routes stub, Zustand store, and constants file.

### Lesson 4.2 — GitHub Copilot

**When Copilot is valuable:**

```
✓ Autocomplete — finishing boilerplate you started
✓ Repetitive patterns — 5th similar component
✓ Tests — structure and edge cases
✓ Comments — JSDoc, inline explanations
✓ Conversions — "convert this to async/await"

✗ Complex business logic — verify carefully
✗ Security code — never trust without audit
✗ Up-to-date APIs — may suggest deprecated patterns
✗ Your domain logic — it doesn't know your requirements
```

**Keyboard shortcuts:**

```
Tab           → accept suggestion
Ctrl+→        → accept one word
Escape        → dismiss
Alt+[ / Alt+] → cycle alternatives
Ctrl+I        → Copilot inline edit
Ctrl+Shift+I  → Copilot Chat
```

**Copilot Chat slash commands:**

```
/explain → explain selected code
/fix     → fix the current error
/tests   → generate tests for selection
/doc     → add documentation comments
```

**Exercises**

**4.2.1** — Use Copilot Chat to: explain your most complex component, generate tests for one hook, and add JSDoc to your prompt utilities. Note where Copilot was wrong.

### Lesson 4.3 — GitHub Actions for AI Projects

```yaml
# .github/workflows/ci.yml
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20", cache: "npm" }
      - run: npm ci
      - run: npm run lint
      - run: npm run build
        env:
          ANTHROPIC_API_KEY:    ${{ secrets.ANTHROPIC_API_KEY }}
          NEXT_PUBLIC_APP_URL:  ${{ vars.NEXT_PUBLIC_APP_URL }}
```

**Vercel auto-deploy:**
1. Push to GitHub
2. Connect repo at vercel.com
3. Add secrets: Settings → Environment Variables
4. Every push to `main` deploys automatically

**Monitoring usage and costs:**

```javascript
// Log token usage in every API route
const result = await generateText({ model, messages });
console.log({
  tokens: { prompt: result.usage.promptTokens, completion: result.usage.completionTokens },
  model:  "claude-sonnet-4-5",
  route:  req.url,
  ts:     new Date().toISOString(),
});
```

**Exercises**

**4.3.1** — Set up CI for your AI project. Add `ANTHROPIC_API_KEY` as a GitHub Secret. Verify the workflow passes on a green push.

### Lesson 4.4 — Capstone Preparation

**Capstone requirements:**

| Requirement | Detail |
|-------------|--------|
| Framework | Next.js App Router + Tailwind + shadcn/ui |
| AI features | At least 2 distinct AI features |
| Streaming | All generative features must stream |
| Prompts | At least 1 custom system prompt tailored to the product |
| Error handling | Graceful handling of rate limits, failures, empty responses |
| Responsive | Tested and working on mobile |
| CI | GitHub Actions lints and builds on every push |
| Deployment | Vercel with API keys as environment variables |
| Repository | Public GitHub with professional README |
| Demo | 5-minute live demo showing both AI features |

**Project ideas:**
- Study companion: upload notes → ask questions → auto-generate quizzes
- CV analyser: paste job description + CV → get gap analysis + rewrite suggestions
- Recipe builder: describe ingredients → get recipes + nutritional breakdown
- Interview prep: answer questions in text/voice → get structured feedback
- Writing assistant: draft, rewrite, expand, translate, summarise
- Language tutor: conversation practice with corrections and explanations
- Code explainer: paste any code → beginner-friendly walkthrough + improvements

**Project brief template:**

```markdown
## [Project Name]
**One-line description:** ...

## AI features
1. **Feature 1:** [description, input, output, why it streams]
2. **Feature 2:** [description, input, output, why it streams]

## Tech stack
- Next.js App Router, Tailwind, shadcn/ui
- Vercel AI SDK (claude-sonnet-4-5)
- [Any additional libraries]

## Pages
- `/` — landing page
- `/[feature-1]` — AI feature 1
- `/[feature-2]` — AI feature 2

## Data
- [What data the app uses, if any]

## Biggest unknowns
- [What you're not sure about yet]
```

**Exercises**

**4.4.1** — Write your capstone brief using the template above. Share in the community. Get feedback from at least two classmates before starting to build.

**4.4.2** — Set up the Next.js project, connect GitHub, configure Vercel auto-deploy, and verify CI passes — before writing a single feature. The scaffolding should take 1 hour.
