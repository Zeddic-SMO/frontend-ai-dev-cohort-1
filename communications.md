# Launch Day Communications

> **Date:** Saturday, 30 May 2026 — the program begins tomorrow.
> **Audience:** All enrolled subscribers.

---

## Email

### Assets

| Asset | Path |
|---|---|
| Banner image | `images/campaign/email_launch_banner.png` |
| WhatsApp banner | `images/campaign/whatsapp/day_14_we're_live.png` |

---

### Subject line

```
We start tomorrow — here's everything you need
```

### Preview text

```
The full curriculum is live. Read it tonight. Show up tomorrow. Let's build.
```

---

### Email body (HTML)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ICTZoid — Program starts tomorrow</title>
</head>
<body style="margin:0;padding:0;background:#08080A;font-family:Arial,sans-serif;">

  <!-- Wrapper -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#08080A;">
    <tr>
      <td align="center" style="padding:32px 16px;">

        <!-- Card -->
        <table width="600" cellpadding="0" cellspacing="0"
               style="background:#0F1628;border-radius:12px;overflow:hidden;max-width:600px;width:100%;">

          <!-- Banner image -->
          <tr>
            <td>
              <img
                src="https://[YOUR-CDN-OR-EMAIL-HOST]/email_launch_banner.png"
                alt="ICTZoid — The program starts tomorrow"
                width="600"
                style="display:block;width:100%;border-radius:12px 12px 0 0;"
              />
            </td>
          </tr>

          <!-- Body content -->
          <tr>
            <td style="padding:40px 44px 32px;">

              <!-- Greeting -->
              <p style="margin:0 0 24px;font-size:16px;color:#94A3B8;line-height:1.6;">
                Hey,
              </p>

              <p style="margin:0 0 24px;font-size:17px;color:#F8FAFC;line-height:1.7;">
                Tomorrow is day one. Everything we've been building toward starts in the morning,
                and we want you walking in with a clear picture of what's ahead.
              </p>

              <!-- CTA button -->
              <table cellpadding="0" cellspacing="0" style="margin:32px 0;">
                <tr>
                  <td style="background:#00D4FF;border-radius:8px;">
                    <a href="[CURRICULUM_LINK]"
                       style="display:inline-block;padding:16px 36px;font-size:16px;
                              font-weight:bold;color:#08080A;text-decoration:none;
                              border-radius:8px;letter-spacing:0.3px;">
                      View the full curriculum →
                    </a>
                  </td>
                </tr>
              </table>

              <!-- What's inside -->
              <p style="margin:0 0 12px;font-size:14px;font-weight:bold;
                         color:#00D4FF;text-transform:uppercase;letter-spacing:1px;">
                What's inside
              </p>

              <table cellpadding="0" cellspacing="0" width="100%" style="margin-bottom:28px;">
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #1E2D4A;">
                    <span style="font-size:15px;color:#F8FAFC;font-weight:bold;">
                      Master Session 1
                    </span>
                    <span style="font-size:14px;color:#94A3B8;"> — How the Internet Works</span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      DNS · TCP/IP · HTTP · Status codes · URL anatomy
                    </span>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #1E2D4A;">
                    <span style="font-size:15px;color:#F8FAFC;font-weight:bold;">
                      Master Session 2
                    </span>
                    <span style="font-size:14px;color:#94A3B8;"> — Software Development Lifecycle</span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      Agile · Scrum · Sprint planning · CI/CD
                    </span>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #1E2D4A;">
                    <span style="font-size:15px;color:#F8FAFC;font-weight:bold;">
                      Course 1 — HTML
                    </span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      Semantic structure · Accessibility · ARIA · Form validation
                    </span>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #1E2D4A;">
                    <span style="font-size:15px;color:#F8FAFC;font-weight:bold;">
                      Course 2 — CSS
                    </span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      Flexbox · Grid · Responsive design · Animations · Theme system
                    </span>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #1E2D4A;">
                    <span style="font-size:15px;color:#F8FAFC;font-weight:bold;">
                      Course 3 — JavaScript
                    </span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      DOM · Events · async/await · REST APIs · localStorage · DevTools
                    </span>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #1E2D4A;">
                    <span style="font-size:15px;color:#F8FAFC;font-weight:bold;">
                      Course 4 — Git & GitHub
                    </span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      Commits · Branching · Pull requests · CI pipelines
                    </span>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0;border-bottom:1px solid #1E2D4A;">
                    <span style="font-size:15px;color:#F8FAFC;font-weight:bold;">
                      Course 5 — React
                    </span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      Components · Hooks · Router · TanStack Query · Tailwind · shadcn/ui
                    </span>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0;">
                    <span style="font-size:15px;font-weight:bold;"
                          style="color:#22C55E;">
                      Course 6 — Frontend AI Development
                    </span>
                    <br/>
                    <span style="font-size:13px;color:#64748B;">
                      Claude & GPT-4o APIs · Streaming chat · Image analysis · Voice · Tool calling
                    </span>
                  </td>
                </tr>
              </table>

              <!-- Closing -->
              <p style="margin:0 0 8px;font-size:17px;color:#F8FAFC;line-height:1.7;">
                Read through the outline tonight so you know exactly what's coming.
                Tomorrow, show up. That's step one.
              </p>

              <p style="margin:24px 0 0;font-size:16px;color:#94A3B8;line-height:1.6;">
                See you tomorrow,<br/>
                <strong style="color:#00D4FF;">The ICTZoid Team</strong>
              </p>

            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding:20px 44px;border-top:1px solid #1E2D4A;">
              <p style="margin:0;font-size:12px;color:#475569;text-align:center;">
                ICTZoid Web Development Program &nbsp;|&nbsp;
                You're receiving this because you enrolled in the program.<br/>
                Questions? Reply to this email or message us in the WhatsApp group.
              </p>
            </td>
          </tr>

        </table>
        <!-- /Card -->

      </td>
    </tr>
  </table>

</body>
</html>
```

---

### Plain-text fallback

```
ICTZoid — The program starts tomorrow
======================================

Hey,

Tomorrow is day one. We've put together the full curriculum so you know
exactly what's coming before the first session begins.

View the full curriculum:
[CURRICULUM_LINK]

WHAT'S INSIDE
-------------
Master Session 1 — How the Internet Works
  DNS, TCP/IP, HTTP, status codes, URL anatomy

Master Session 2 — Software Development Lifecycle
  Agile, Scrum, sprint planning, CI/CD

Course 1 — HTML
  Semantic structure, accessibility, ARIA, form validation

Course 2 — CSS
  Flexbox, Grid, responsive design, animations, theme system

Course 3 — JavaScript
  DOM, events, async/await, REST APIs, localStorage, DevTools

Course 4 — Git & GitHub
  Commits, branching, pull requests, CI pipelines

Course 5 — React
  Components, hooks, routing, TanStack Query, Tailwind, shadcn/ui

Course 6 — Frontend AI Development
  Claude & GPT-4o APIs, streaming chat, image analysis, voice, tool calling

Read through the outline tonight. Show up tomorrow. That's step one.

See you tomorrow,
The ICTZoid Team

---
ICTZoid Web Development Program
Questions? Reply to this email or message us in the WhatsApp group.
```

---

## WhatsApp Group Message

> **Image to attach:** `images/campaign/whatsapp/day_14_we're_live.png`

```
We're live. 🚀

Tomorrow is day one — and everything is ready for you.

Here's the full curriculum so you can walk in knowing exactly what's ahead:
👉 [CURRICULUM_LINK]

What you're getting into:
📌 2 Master Sessions — How the Internet Works + SDLC
📌 6 Courses — HTML → CSS → JavaScript → Git → React → Frontend AI
📌 85+ lessons built to take you from zero to shipping apps with AI inside

No prerequisites. No guesswork. Just show up tomorrow.

You've been in this group this whole time — that already tells us you're serious. The people who show up on day one are the ones who finish.

See you there. 💪
— ICTZoid Team
```

---

## Placeholders to fill in before sending

| Placeholder | What to replace it with |
|---|---|
| `[CURRICULUM_LINK]` | The public URL to the course catalog on the LMS (e.g. `https://app.ictzoid.com/curriculum`) |
| `https://[YOUR-CDN-OR-EMAIL-HOST]/email_launch_banner.png` | Upload `images/campaign/email_launch_banner.png` to your email CDN or media host and paste the URL here |
