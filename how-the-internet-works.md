# How the Internet Works

![How the Internet Works](images/course-internet.svg)

> **Track:** Web Fundamentals · **Level:** Beginner · **Prerequisite:** None

---

## Course Overview

Before writing a single line of HTML, every web developer should understand what actually happens when a URL is typed into a browser. This course walks through the full journey — from keyboard to screen — covering the protocols, systems, and concepts that make the web function. By the end you will be able to explain DNS lookups, HTTP conversations, packet routing, and status codes with confidence.

---

## Learning Objectives

By the end of this course you will be able to:

- Describe the roles of clients and servers and how they interact
- Explain what DNS is and trace the steps of a DNS lookup
- Define TCP/IP and explain why it is the foundation of internet communication
- Read and write basic HTTP requests and responses
- Identify the most common HTTP status codes and what they mean
- Break down the components of a URL (protocol, domain, subdomain, path)
- Explain why data travels as packets and what benefits that brings

---

## Modules

| # | Module | Lessons |
|---|--------|---------|
| 1 | The Big Picture | 3 |
| 2 | The Internet's Toolkit | 4 |
| 3 | A Request's Journey | 4 |
| 4 | HTTP in Depth | 4 |
| 5 | URLs and Addresses | 3 |

---

## Module 1 — The Big Picture

### Lesson 1.1 — What Is the Web?

The web is a system built on top of the internet that lets you publish and retrieve documents (pages, images, videos, applications) using a common set of standards. It is not the internet itself — the internet is the global network of cables, routers, and wireless links; the web is one of many services that runs over it.

**Key distinction:**

| Term | What it means |
|------|---------------|
| The Internet | The physical + logical network connecting billions of devices worldwide |
| The Web (WWW) | A service that uses the internet to exchange hyperlinked documents via HTTP |

Other services that also run over the internet include email (SMTP/IMAP), file transfer (FTP), and video calls (WebRTC/SIP).

---

### Lesson 1.2 — Clients and Servers

Every interaction on the web involves two roles:

**Clients** are internet-connected devices that request information. Your laptop running Chrome, your phone running Safari, a smart TV browser — all are clients. The defining trait: a client *initiates* the conversation.

**Servers** are computers (usually powerful machines in data centres) that store websites, APIs, images, and files. A server *listens* for incoming requests and sends back the appropriate content.

```
   CLIENT                            SERVER
  ┌───────┐   ── HTTP Request ──►  ┌────────────┐
  │ You   │                        │ Web Server │
  │       │  ◄── HTTP Response ──  │            │
  └───────┘                        └────────────┘
```

**Analogy:** Think of a client as a customer walking into a shop and a server as the shop itself. The customer asks for a product; the shop hands it over.

---

### Lesson 1.3 — What Gets Transferred?

When a server responds it sends back two categories of files:

**Code files** — the browser interprets and assembles these to build the page:

- **HTML** — the structure and content
- **CSS** — the visual presentation
- **JavaScript** — behaviour and interactivity

**Asset files** — content that is displayed or used directly within the page:

- Images (JPEG, PNG, SVG, WebP)
- Video and audio
- Documents and PDFs
- Web fonts

A single page load often triggers dozens of separate requests — one for the HTML, then more for each stylesheet, script, image, and font referenced inside it.

---

## Module 2 — The Internet's Toolkit

### Lesson 2.1 — IP Addresses

Every device on the internet needs a unique address so data knows where to go. This is an **IP (Internet Protocol) address**.

**IPv4 example:** `192.0.2.172`
Four groups of numbers (0–255) separated by dots. Around 4.3 billion possible addresses — a number the world has already run out of.

**IPv6 example:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
Eight groups of four hex digits. 340 undecillion addresses — essentially unlimited.

Large websites operate clusters of servers in multiple locations, each with its own IP, for speed and reliability.

---

### Lesson 2.2 — DNS (Domain Name System)

IP addresses are precise but impossible to memorise. The **Domain Name System** solves this by acting as the internet's phone book — it maps human-readable names to numeric addresses.

**Flow of a DNS lookup:**

```
Browser Cache → OS Cache → Resolving Resolver → Root Nameserver
                                                      │
                                             TLD Nameserver (.com/.org)
                                                      │
                                          Authoritative Nameserver
                                                      │
                                              IP Address returned
                                                      │
                                             Browser caches result
```

1. You type `mozilla.org` into the browser.
2. The browser checks its local cache. If it has a recent result, it uses it.
3. If not, the OS asks a **recursive resolver** (usually run by your ISP or a public service like 8.8.8.8).
4. The resolver works up the DNS hierarchy until it finds the **authoritative nameserver** for `mozilla.org`.
5. That nameserver returns the IP address (e.g. `63.245.208.195`).
6. The browser stores it in cache and opens a connection to that IP.

**Why it matters:** Without DNS, the entire web would depend on users knowing numerical addresses. Every domain change would break every bookmark.

---

### Lesson 2.3 — TCP/IP

**TCP/IP** is not one thing — it is a suite of two complementary protocols:

| Protocol | Layer | Job |
|----------|-------|-----|
| **IP** (Internet Protocol) | Network | Addressing and routing — gets packets to the right machine |
| **TCP** (Transmission Control Protocol) | Transport | Reliability — ensures all packets arrive and are reassembled correctly |

**How TCP establishes a connection — the Three-Way Handshake:**

```
Client ──── SYN ────────────────────────► Server
Client ◄─── SYN-ACK ──────────────────── Server
Client ──── ACK ────────────────────────► Server
            (connection established)
```

1. **SYN** — client says "I want to connect."
2. **SYN-ACK** — server says "Acknowledged, I'm ready."
3. **ACK** — client says "Great, let's go."

After the handshake, data flows. TCP guarantees delivery: if a packet is lost, it is automatically resent.

**Analogy:** IP is the postal system that routes your envelope to the right building. TCP is the courier service that confirms the package was received and chases it up if it wasn't.

---

### Lesson 2.4 — Packets

Data on the internet does not travel as one continuous stream. It is broken into small chunks called **packets** (typically 1,500 bytes or less each).

**Structure of a packet:**

```
┌────────────────────────────────────┐
│            HEADER                  │
│  Source IP · Destination IP        │
│  Packet # · Total packets          │
│  Protocol info · Checksum          │
├────────────────────────────────────┤
│            PAYLOAD                 │
│  (the actual data chunk)           │
└────────────────────────────────────┘
```

**Why packets instead of one big stream?**

| Benefit | Explanation |
|---------|-------------|
| **Fault tolerance** | If a packet is lost, only that packet needs resending — not the whole file |
| **Efficiency** | Different packets can take different routes through the network simultaneously |
| **Fairness** | Many users can share the same network links without one download blocking another |
| **Scalability** | Thousands of conversations can be interwoven on the same cables |

Packets may arrive **out of order**. TCP uses the sequence numbers in the headers to reassemble them correctly.

---

## Module 3 — A Request's Journey

### Lesson 3.1 — The Full Step-by-Step Flow

Let's trace exactly what happens from the moment you press Enter after typing `https://developer.mozilla.org/en-US/`:

```
Step 1 ── DNS Lookup
          Browser has no cached IP for developer.mozilla.org
          → asks recursive resolver
          → resolver queries DNS hierarchy
          → returns IP address (e.g. 34.120.193.11)

Step 2 ── TCP Connection
          Browser initiates three-way handshake with server on port 443

Step 3 ── TLS Handshake (HTTPS only)
          Browser and server negotiate encryption
          Server presents its certificate
          Secure channel established

Step 4 ── HTTP Request sent
          GET /en-US/ HTTP/2
          Host: developer.mozilla.org

Step 5 ── Server processes request
          Looks up the resource, builds the response

Step 6 ── HTTP Response received
          HTTP/2 200
          Content-Type: text/html
          [45,227 bytes of HTML follow]

Step 7 ── Browser renders
          Parses HTML → fetches linked CSS, JS, images (new requests for each)
          Builds DOM and CSSOM → renders the page
```

---

### Lesson 3.2 — Ports

IP addresses identify machines; **ports** identify which service on that machine should handle the request.

| Port | Service |
|------|---------|
| 80 | HTTP |
| 443 | HTTPS |
| 25 | SMTP (email) |
| 22 | SSH |

When you request `https://mozilla.org`, the browser automatically connects to port 443. You never see it in the URL because browsers treat it as the default for HTTPS.

---

### Lesson 3.3 — TLS and HTTPS

**HTTPS** = HTTP + **TLS** (Transport Layer Security). The `S` stands for Secure.

TLS provides three things:

1. **Encryption** — data travelling between client and server cannot be read by anyone intercepting it.
2. **Authentication** — the server proves it is who it claims to be via a digital certificate issued by a trusted **Certificate Authority (CA)**.
3. **Integrity** — data cannot be tampered with in transit without detection.

Any site handling passwords, payment details, or personal data *must* use HTTPS. Modern browsers actively warn users on HTTP-only pages.

---

### Lesson 3.4 — Rendering Pipeline (overview)

Once the HTML arrives, the browser does not display it directly. It runs a **rendering pipeline**:

```
HTML bytes
    │
    ▼
Parse HTML → DOM (Document Object Model)
    │
    ├─── encounters <link rel="stylesheet"> → fetch CSS → CSSOM
    │
    └─── encounters <script> → fetch JS → execute
                │
                ▼
           Render Tree (DOM + CSSOM merged)
                │
                ▼
           Layout (calculate positions + sizes)
                │
                ▼
           Paint (draw pixels to screen)
```

Each external resource (image, font, script, stylesheet) triggers a brand new HTTP request, re-starting the request journey from Step 4 of the previous lesson.

---

## Module 4 — HTTP in Depth

### Lesson 4.1 — HTTP Requests

An HTTP request is a plain-text message with a defined structure:

```http
GET /en-US/ HTTP/2
Host: developer.mozilla.org
Accept: text/html
Accept-Language: en-GB,en;q=0.9
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X)
```

**Key parts:**

| Part | Example | Purpose |
|------|---------|---------|
| **Method** | `GET` | What action to perform |
| **Path** | `/en-US/` | Which resource on the server |
| **Protocol version** | `HTTP/2` | Which HTTP version to use |
| **Host header** | `developer.mozilla.org` | Which virtual host to reach (servers host multiple domains) |
| **Other headers** | `Accept`, `User-Agent` | Extra info about the client and what it accepts |

**Common HTTP methods:**

| Method | Meaning | Use case |
|--------|---------|---------|
| `GET` | Fetch a resource | Loading a page, downloading an image |
| `POST` | Send data to the server | Submitting a form, creating a record |
| `PUT` | Replace a resource | Updating a user profile |
| `PATCH` | Partially update a resource | Changing a single field |
| `DELETE` | Remove a resource | Deleting an account |

---

### Lesson 4.2 — HTTP Responses

The server replies with a response message:

```http
HTTP/2 200
date: Tue, 11 Feb 2025 11:13:30 GMT
content-type: text/html; charset=utf-8
content-length: 45227
server: Google frontend
last-modified: Tue, 11 Feb 2025 00:49:32 GMT

<!doctype html>
<html lang="en">
  ...
</html>
```

**Key parts:**

| Part | Example | Purpose |
|------|---------|---------|
| **Status line** | `HTTP/2 200` | Protocol version + outcome code |
| **Response headers** | `content-type`, `date` | Metadata about the response |
| **Body** | HTML / JSON / binary | The actual content requested |

---

### Lesson 4.3 — HTTP Status Codes

Status codes are three-digit numbers grouped by the first digit:

| Range | Category | Meaning |
|-------|----------|---------|
| `1xx` | Informational | Request received, processing continues |
| `2xx` | Success | Request was received, understood, and accepted |
| `3xx` | Redirection | Further action needed to complete the request |
| `4xx` | Client Error | The request contains bad syntax or cannot be fulfilled |
| `5xx` | Server Error | The server failed to fulfil a valid request |

**The codes you will encounter most:**

| Code | Name | What it means in practice |
|------|------|--------------------------|
| **200** | OK | Everything worked. Resource is in the response body. |
| **201** | Created | A new resource was successfully created (after POST). |
| **301** | Moved Permanently | URL has changed forever. Browser should update bookmarks. |
| **302** | Found | Temporary redirect. Keep using the original URL. |
| **304** | Not Modified | Cached version is still valid — no need to re-download. |
| **400** | Bad Request | The server could not understand the request (malformed syntax). |
| **401** | Unauthorized | Authentication required (you need to log in). |
| **403** | Forbidden | Server understood the request but refuses to authorise it. |
| **404** | Not Found | Resource does not exist at this URL. |
| **429** | Too Many Requests | Rate limit hit — slow down. |
| **500** | Internal Server Error | Something went wrong on the server. |
| **503** | Service Unavailable | Server is down for maintenance or overloaded. |

---

### Lesson 4.4 — HTTP Versions

| Version | Year | Key features |
|---------|------|-------------|
| **HTTP/1.0** | 1996 | New TCP connection per request — very slow |
| **HTTP/1.1** | 1997 | Persistent connections, pipelining, chunked transfer |
| **HTTP/2** | 2015 | Multiplexing (multiple requests over one connection), header compression, server push |
| **HTTP/3** | 2022 | Built on QUIC (UDP-based), faster handshakes, better loss recovery |

Most modern websites use HTTP/2 or HTTP/3. You can see which version is being used in browser DevTools → Network tab → Protocol column.

---

## Module 5 — URLs and Addresses

### Lesson 5.1 — Anatomy of a URL

A **URL** (Uniform Resource Locator) is the full address of a resource on the web.

```
https://developer.mozilla.org/en-US/docs/Web?q=http#intro
  │         │         │        │     │        │       │
  │         │         │        │     │        │       └── Fragment (section on page)
  │         │         │        │     │        └────────── Query string (?key=value)
  │         │         │        │     └─────────────────── Path
  │         │         │        └───────────────────────── Domain (TLD: .org)
  │         │         └────────────────────────────────── Subdomain
  │         └──────────────────────────────────────────── Domain name
  └────────────────────────────────────────────────────── Scheme (protocol)
```

**Breaking it down:**

| Component | Example | Notes |
|-----------|---------|-------|
| **Scheme** | `https` | Tells the browser which protocol to use. `http` or `https` for web; `mailto:` for email |
| **Subdomain** | `developer` | A separate section of a site. `support.mozilla.org` and `developer.mozilla.org` are distinct |
| **Domain** | `mozilla.org` | The registered name, purchased from a registrar |
| **TLD** | `.org` | Top-level domain — indicates type (.com, .org, .edu) or country (.uk, .ng, .de) |
| **Path** | `/en-US/docs/Web` | The specific resource on the server |
| **Query string** | `?q=http` | Key-value pairs passed to the server (e.g. search terms) |
| **Fragment** | `#intro` | Jumps to a specific section within the page (processed by the browser, not sent to the server) |

---

### Lesson 5.2 — Domain Names and Registration

Domain names are managed through a global hierarchy:

```
. (root)
├── .com
│   ├── google.com
│   └── mozilla.com
├── .org
│   └── wikipedia.org
└── .ng
    └── gov.ng
```

- **ICANN** (Internet Corporation for Assigned Names and Numbers) oversees the global namespace.
- **Registrars** (e.g. Namecheap, GoDaddy) sell domain registrations.
- Domains are leased annually — if you stop paying, someone else can register yours.
- DNS records (A, CNAME, MX, TXT) stored in authoritative nameservers tell the world where your domain points.

---

### Lesson 5.3 — The Road Analogy — Full Picture

The MDN documentation uses a shopping analogy to make these concepts stick. Here is the complete mapping:

| Internet concept | Real-world analogy |
|-------------------|--------------------|
| Your computer (client) | You, the customer |
| Web server | The shop |
| Internet connection | The road from your house to the shop |
| TCP/IP | The car or bike that carries you along the road |
| DNS | Your address book (you look up the shop's address) |
| HTTP | The language you speak when you walk in and order |
| Files / response body | The goods the shop hands you |
| Packets | The goods broken into boxes for transport |

---

## Quick Reference

### HTTP Request Template

```http
METHOD /path HTTP/version
Host: hostname
Header-Name: header-value

[optional body for POST/PUT/PATCH]
```

### HTTP Response Template

```http
HTTP/version STATUS_CODE Reason Phrase
Header-Name: header-value

[response body]
```

### DNS Lookup Chain

```
Browser → OS → Resolver → Root → TLD → Authoritative → IP address
```

### Full Page Load Chain

```
Type URL → DNS lookup → TCP handshake → TLS handshake (HTTPS)
         → HTTP GET → 200 OK + HTML → parse HTML
         → fetch CSS/JS/images → render pipeline → display
```

---

## Review Questions

**Module 1**
1. What is the difference between the internet and the World Wide Web?
2. Which role initiates an HTTP conversation — the client or the server?
3. Name three types of code files and three types of asset files a browser might request.

**Module 2**
4. What problem does DNS solve?
5. Describe the three steps of the TCP three-way handshake.
6. List three advantages of sending data as packets rather than as a single stream.

**Module 3**
7. In order, list the six major steps that happen after you press Enter on a URL.
8. What port does HTTPS use by default?
9. What three guarantees does TLS provide?

**Module 4**
10. What HTTP method should you use to submit a login form? Why not GET?
11. A user sees a 403 error. What does this mean and how is it different from a 401?
12. What improvement did HTTP/2 introduce over HTTP/1.1?

**Module 5**
13. Break this URL into its components: `https://api.example.com/v1/users?page=2#results`
14. What part of a URL is processed entirely by the browser and never sent to the server?
15. Who ultimately manages the global namespace for domain names?

---

## Practical Exercises

### Exercise 1 — Inspect a Real Request
1. Open Chrome or Firefox DevTools (`F12`).
2. Go to the **Network** tab and reload any webpage.
3. Click the first request (usually the HTML document).
4. Identify: the status code, the HTTP method, the response headers, the protocol version.

### Exercise 2 — Trace a DNS Lookup
Run the following in your terminal and observe each step:
```bash
# Linux / macOS
dig mozilla.org +trace

# Windows
nslookup mozilla.org
```
Note the IP address returned. Try opening that IP directly in your browser.

### Exercise 3 — Read Response Headers
Using DevTools or `curl`:
```bash
curl -I https://developer.mozilla.org/en-US/
```
Identify: `content-type`, `content-length`, `server`, `cache-control`.

### Exercise 4 — Status Code Hunt
Visit these paths on a site you control (or use a test server) and trigger:
- A `404` — request a path that doesn't exist
- A `301` — set up a redirect and observe it in DevTools

### Exercise 5 — URL Dissection
Break each of these URLs into scheme, subdomain, domain, TLD, path, query string, and fragment:
```
https://www.youtube.com/watch?v=abc123
https://mail.google.com/mail/u/0/#inbox
https://docs.github.com/en/actions
```

---

## Glossary

| Term | Definition |
|------|-----------|
| **Client** | A device or application that initiates requests to a server |
| **Server** | A computer that stores resources and responds to client requests |
| **IP Address** | A unique numerical label assigned to each device on a network |
| **DNS** | Domain Name System — translates domain names to IP addresses |
| **TCP** | Transmission Control Protocol — guarantees reliable, ordered delivery of data |
| **IP** | Internet Protocol — handles addressing and routing of packets |
| **HTTP** | Hypertext Transfer Protocol — the language of the web |
| **HTTPS** | HTTP with TLS encryption |
| **TLS** | Transport Layer Security — provides encryption, authentication, and integrity |
| **Packet** | A small chunk of data with a header (routing info) and payload (content) |
| **URL** | Uniform Resource Locator — the full address of a web resource |
| **Domain** | The human-readable name registered for a website |
| **TLD** | Top-level domain — the last part of a domain (`.com`, `.org`, `.ng`) |
| **Port** | A number identifying a specific service on a networked machine |
| **Status code** | A three-digit number in an HTTP response indicating the outcome |
| **Cache** | Stored copies of responses to speed up future requests |
| **Rendering pipeline** | The browser's process of turning HTML/CSS/JS into visible pixels |

---

*Source material: [MDN Web Docs — How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)*
