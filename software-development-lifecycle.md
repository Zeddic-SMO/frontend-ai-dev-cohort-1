# Software Development Lifecycle (SDLC)

![Software Development Lifecycle](images/course-sdlc.svg)

> **Track:** Foundations · **Level:** Beginner · **Prerequisite:** None

---

## Course Overview

Every piece of software — from a mobile app to an enterprise platform — was built by following a process. That process is the Software Development Lifecycle: a structured sequence of phases that takes a vague idea and turns it into a shipped, maintained product. This course teaches you to think like a professional engineer before you write a single line of code. You will understand *why* teams follow processes, learn the dominant methodologies used in industry today, and practise the ceremonies and artefacts that real Agile teams produce every day.

---

## Learning Objectives

By the end of this course you will be able to:

- Name and describe each phase of the SDLC and its key deliverables
- Compare Waterfall, Agile, Scrum, Kanban, and DevOps and choose the right fit for a given project
- Write clear user stories with acceptance criteria
- Facilitate or participate in sprint planning, daily standups, reviews, and retrospectives
- Read a burn-down chart and interpret team velocity
- Explain what CI/CD is and why it matters to the SDLC
- Identify the key roles on a software team and describe their responsibilities

---

## Modules

| # | Module | Lessons |
|---|--------|---------|
| 1 | What Is the SDLC? | 4 |
| 2 | Phase by Phase | 6 |
| 3 | Development Methodologies | 4 |
| 4 | Agile in Practice | 4 |
| 5 | Modern Tools and DevOps | 2 |

---

## Module 1 — What Is the SDLC?

### Lesson 1.1 — The Software Crisis and Why Process Matters

In the 1960s and 70s, software projects were failing at an alarming rate — over budget, over deadline, unreliable, or simply abandoned. This period became known as the **Software Crisis**. The root cause was treating software like manufacturing: start coding, ship, fix later. The solution was to apply engineering discipline to software development — hence the SDLC.

**Common failure patterns without a process:**

| Problem | What happens |
|---------|-------------|
| No requirements phase | Team builds the wrong thing |
| No design phase | Code becomes unmaintainable quickly |
| No testing phase | Bugs reach production and cost 10–100× more to fix |
| No planning phase | Project overruns time and budget |
| No maintenance phase | Product degrades and loses users |

The SDLC is not about bureaucracy — it is about making sure the right thing gets built, correctly, sustainably.

---

### Lesson 1.2 — The Six Phases of the SDLC

The SDLC is typically broken into six phases. They may overlap or repeat depending on the methodology, but the concerns they address are universal.

```
  ┌─────────┐     ┌─────────────┐     ┌────────┐
  │ PLAN    │────►│ REQUIREMENTS│────►│ DESIGN │
  └─────────┘     └─────────────┘     └────────┘
                                           │
  ┌──────────┐     ┌──────────┐     ┌──────▼────┐
  │ MAINTAIN │◄────│  DEPLOY  │◄────│  DEVELOP  │
  └──────────┘     └──────────┘     └──────┬────┘
                                           │
                                      ┌────▼────┐
                                      │  TEST   │
                                      └─────────┘
```

| Phase | Core question | Key deliverables |
|-------|---------------|-----------------|
| **Plan** | Is this worth building? | Project scope, timeline, budget, risk assessment |
| **Requirements** | What exactly should it do? | Requirements document, user stories, use cases |
| **Design** | How will we build it? | Architecture diagram, data model, UI wireframes |
| **Develop** | Build it | Working code, code reviews, unit tests |
| **Test** | Does it work correctly? | Test plan, bug reports, test results |
| **Deploy** | Get it to users | Release notes, deployment scripts, monitoring |
| **Maintain** | Keep it working | Bug fixes, performance improvements, updates |

---

### Lesson 1.3 — Key Roles on a Software Team

Understanding who does what is essential before learning how teams work together.

| Role | Responsibilities |
|------|-----------------|
| **Product Manager (PM)** | Owns the product vision; decides what to build and why; prioritises the backlog |
| **Business Analyst (BA)** | Bridges the gap between stakeholders and engineers; writes requirements |
| **UX Designer** | Designs user flows, wireframes, and prototypes; conducts user research |
| **Software Engineer (Dev)** | Writes, tests, and reviews code; estimates effort |
| **QA Engineer** | Creates and executes test plans; reports and tracks bugs |
| **DevOps / Platform Engineer** | Manages infrastructure, CI/CD pipelines, and deployment |
| **Scrum Master** | Facilitates Agile ceremonies; removes blockers; coaches the team |
| **Tech Lead / Engineering Manager** | Makes architectural decisions; mentors engineers; coordinates delivery |

In small teams or startups, one person may cover several of these roles.

---

### Lesson 1.4 — Choosing the Right Model

No single SDLC model is universally best. The right choice depends on:

| Factor | Favours Waterfall | Favours Agile |
|--------|-------------------|---------------|
| Requirements stability | Fixed, well-understood | Changing, evolving |
| Customer involvement | Low (sign-off at start) | High (continuous feedback) |
| Delivery expectation | One big release | Frequent incremental releases |
| Team size | Large, geographically spread | Small, co-located |
| Risk tolerance | Low (compliance, safety) | Higher (startups, innovation) |
| Documentation needs | Heavy (regulated industries) | Lightweight (working software over docs) |

Most modern teams use some form of Agile. Waterfall is still used in aerospace, defence, medical devices, and large government contracts where requirements are legally fixed.

---

## Module 2 — Phase by Phase

### Lesson 2.1 — Planning: Scope, Feasibility, and Estimation

The planning phase determines whether a project should proceed, how long it will take, and what it will cost.

**Key activities:**

1. **Scope definition** — What is included? What is explicitly out of scope?
2. **Feasibility study** — Technical feasibility (can we build it?), financial feasibility (can we afford it?), operational feasibility (will users adopt it?)
3. **Risk assessment** — Identify risks and mitigation strategies
4. **Resource planning** — Team composition, tools, infrastructure
5. **Estimation** — Story points, T-shirt sizing, or time-based estimation

**Common estimation techniques:**

| Technique | How it works |
|-----------|-------------|
| **Planning Poker** | Team members independently pick an estimate card; discuss disagreements |
| **T-shirt sizing** | Assign XS / S / M / L / XL relative sizes |
| **Three-point estimation** | Average of Optimistic, Most Likely, and Pessimistic estimates |
| **Reference class forecasting** | Compare to similar past projects |

---

### Lesson 2.2 — Requirements: Gathering, Analysis, and Specification

Requirements describe *what* the system must do, not *how*. Getting this phase right is the single biggest predictor of project success.

**Types of requirements:**

| Type | Description | Example |
|------|-------------|---------|
| **Functional** | Specific behaviours the system must perform | "Users can reset their password via email" |
| **Non-functional** | Quality attributes of the system | "The login page must load in < 2 seconds" |
| **Business rules** | Constraints from the business domain | "Students must complete Module 1 before Module 2" |
| **User requirements** | What the end user needs to accomplish | "As a student, I want to track my progress" |

**Gathering techniques:**

- **Interviews** — One-on-one sessions with stakeholders
- **Workshops** — Group sessions with mixed roles
- **Observation** — Watch users do their current workflow
- **Surveys** — Collect data from many users at once
- **Document analysis** — Review existing manuals, processes, forms

**Good requirements are SMART:** Specific, Measurable, Achievable, Relevant, Testable.

---

### Lesson 2.3 — System Design: Architecture, Data Models, and Wireframes

Design translates requirements into a blueprint. It happens at two levels:

**High-level (architectural) design:**

```
  Browser  ──HTTP──►  API Server  ──SQL──►  Database
                           │
                     ──Queue──►  Worker  ──►  Email / Storage
```

Decisions made here:
- Monolith vs microservices
- Relational vs document database
- Synchronous vs asynchronous communication
- Authentication strategy (JWT, session, OAuth)

**Low-level (detailed) design:**
- Entity-Relationship (ER) diagrams
- API endpoint design (REST, GraphQL)
- Component diagrams
- UI wireframes and prototypes

**Artefacts produced:**
- Architecture Decision Records (ADRs)
- Database schema
- API contract (OpenAPI / Swagger)
- UI wireframes (Figma)

---

### Lesson 2.4 — Implementation: Coding Standards and Code Review

The development phase is where software is actually built. Professional teams make it structured, not chaotic.

**Version control workflow (GitFlow / trunk-based):**

```
main ─────────────────────────────────────────►
           │                    ▲
           ▼ git checkout -b    │ pull request
        feature/login ─────────┤
                  (code + commits + tests)
```

**Coding standards matter because:**
- Code is read far more often than it is written
- Consistent style reduces cognitive load during code review
- Automated linters catch issues before human review

**Code review checklist:**
- [ ] Does it solve the intended problem?
- [ ] Are edge cases handled?
- [ ] Is the logic understandable without excessive comments?
- [ ] Are there sufficient tests?
- [ ] Does it introduce any security vulnerabilities?
- [ ] Does it follow team conventions?

---

### Lesson 2.5 — Testing: Types, Levels, and Test Plans

Testing is not a single activity — it is a discipline with multiple levels and types, each catching different kinds of defects.

**Testing levels (the pyramid):**

```
           ▲
          /E2E\          ← Few, slow, expensive but test the full system
         /──────\
        /  Integ  \      ← Test interactions between components
       /────────────\
      /  Unit Tests  \   ← Many, fast, cheap — test individual functions
     /────────────────\
```

| Level | Scope | Speed | Maintained by |
|-------|-------|-------|---------------|
| **Unit** | Single function / class | Very fast (ms) | Developers |
| **Integration** | Multiple components together | Medium (seconds) | Developers / QA |
| **System** | Entire application | Slow (minutes) | QA |
| **Acceptance** | Business requirements met | Varies | QA + Product |
| **End-to-End (E2E)** | Full user flows in the browser | Slowest | QA / Automation |

**Other test types:**

| Type | Purpose |
|------|---------|
| **Regression** | Ensure new changes haven't broken existing features |
| **Performance** | Verify system handles expected load |
| **Security** | Find vulnerabilities before attackers do |
| **Usability** | Evaluate how easy the product is to use |
| **Smoke** | Quick sanity check after a deployment |

---

### Lesson 2.6 — Deployment and Maintenance

**Deployment strategies:**

| Strategy | How it works | Risk |
|----------|-------------|------|
| **Big Bang** | Replace old with new all at once | High |
| **Rolling** | Gradually replace instances over time | Medium |
| **Blue-Green** | Two identical environments; switch traffic instantly | Low |
| **Canary** | Route a small % of traffic to the new version first | Low |
| **Feature flags** | Ship code dark; enable features for specific users | Very low |

**Maintenance types:**

- **Corrective** — Bug fixes
- **Adaptive** — Updates for new OS, browser, or API changes
- **Perfective** — Performance improvements and refactoring
- **Preventive** — Proactive improvements to reduce future failures

The cost of fixing a bug grows significantly the later in the SDLC it is found:

| When found | Relative cost |
|------------|--------------|
| During requirements | 1× |
| During design | 5× |
| During development | 10× |
| During testing | 20× |
| After deployment | 100× |

---

## Module 3 — Development Methodologies

### Lesson 3.1 — Waterfall: Linear and Document-Driven

Waterfall is the original formalised SDLC model, introduced by Winston Royce in 1970. Each phase must be completed and signed off before the next begins.

```
Requirements
    │
    ▼
  Design
    │
    ▼
Implementation
    │
    ▼
 Verification
    │
    ▼
Maintenance
```

**Strengths:**
- Clear milestones and deliverables
- Easy to manage and report on
- Well-suited to fixed-price contracts with stable requirements
- Heavy documentation is useful for regulated industries

**Weaknesses:**
- Changes are expensive — backtracking means repeating phases
- No working software until late in the cycle
- Assumes requirements can be fully known upfront (rarely true)
- Testing happens too late to catch design problems

**Best used for:** Government contracts, safety-critical systems (aviation, medical), projects with legally fixed specifications.

---

### Lesson 3.2 — Agile: Values, Principles, and the Manifesto

Agile is not a methodology — it is a **philosophy**. It emerged from the 2001 **Agile Manifesto**, signed by 17 software practitioners who were frustrated by heavyweight, document-driven processes.

**The four core values:**

| We value... | Over... |
|-------------|---------|
| **Individuals and interactions** | Processes and tools |
| **Working software** | Comprehensive documentation |
| **Customer collaboration** | Contract negotiation |
| **Responding to change** | Following a plan |

*The right column still has value — we just value the left column more.*

**The twelve principles** (summarised):

1. Satisfy the customer through early, continuous delivery of working software
2. Welcome changing requirements, even late in development
3. Deliver working software frequently (weeks, not months)
4. Business and developers must work together daily
5. Build projects around motivated individuals — trust them
6. The most efficient way to convey information is face-to-face
7. Working software is the primary measure of progress
8. Sustainable pace — teams should be able to maintain their speed indefinitely
9. Continuous attention to technical excellence and good design
10. Simplicity — maximise the amount of work *not* done
11. Self-organising teams produce the best architectures and designs
12. Regularly reflect and adjust behaviour

---

### Lesson 3.3 — Scrum: Sprints, Ceremonies, and Artefacts

Scrum is the most widely used Agile framework. It divides work into fixed-length iterations called **Sprints** (typically 1–2 weeks).

**Roles:**

| Role | Responsibility |
|------|---------------|
| **Product Owner** | Owns and prioritises the Product Backlog; represents stakeholders |
| **Scrum Master** | Facilitates ceremonies; removes impediments; coaches the team |
| **Development Team** | Self-organising group that delivers the Sprint Goal |

**Artefacts:**

| Artefact | Description |
|---------|-------------|
| **Product Backlog** | Ordered list of everything that might go into the product |
| **Sprint Backlog** | Subset of Product Backlog items selected for the current Sprint |
| **Increment** | The sum of all completed items — must be "Done" and potentially shippable |

**Ceremonies:**

```
Sprint Planning ──► Daily Scrum (×n) ──► Sprint Review ──► Retrospective
│                                                                    │
└──────────────────────── Next Sprint ──────────────────────────────┘
```

| Ceremony | When | Duration (2-week sprint) | Purpose |
|----------|------|--------------------------|---------|
| **Sprint Planning** | Start of sprint | ≤ 4 hours | Select items, define Sprint Goal, estimate tasks |
| **Daily Scrum** | Every day | 15 minutes | Sync, surface blockers |
| **Sprint Review** | End of sprint | ≤ 2 hours | Demo increment to stakeholders, gather feedback |
| **Retrospective** | After review | ≤ 1.5 hours | Inspect team process and improve |

---

### Lesson 3.4 — Kanban, SAFe, and Choosing a Methodology

**Kanban:**

Kanban is a flow-based system focused on visualising work and limiting work in progress (WIP). Unlike Scrum, there are no sprints — work flows continuously.

```
┌──────────┬────────────┬──────────────┬──────────┐
│ BACKLOG  │  IN PROGRESS  │   REVIEW  │   DONE   │
│          │  (WIP: max 3)  │ (WIP: max 2)│         │
├──────────┼────────────┼──────────────┼──────────┤
│ Task A   │  Task D    │   Task F     │ Task G   │
│ Task B   │  Task E    │              │ Task H   │
│ Task C   │            │              │ Task I   │
└──────────┴────────────┴──────────────┴──────────┘
```

**Key Kanban principles:**
- Visualise the workflow
- Limit WIP to reduce context-switching and bottlenecks
- Manage flow — measure cycle time and throughput
- Make process policies explicit
- Improve continuously

**SAFe (Scaled Agile Framework):**
For large organisations running dozens of Agile teams, SAFe provides a framework that coordinates multiple teams towards a shared Programme Increment (PI) — typically 8–12 weeks of work broken into sprints.

**Choosing a methodology:**

| Situation | Recommendation |
|-----------|---------------|
| Small team, unclear requirements | Scrum |
| Support/ops work with unpredictable incoming tasks | Kanban |
| New product with active stakeholder involvement | Scrum |
| Large enterprise, multiple coordinated teams | SAFe |
| Government / regulated / fixed-requirements project | Waterfall |
| Continuous deployment, fast iteration | DevOps + Kanban or Scrum |

---

## Module 4 — Agile in Practice

### Lesson 4.1 — User Stories and Acceptance Criteria

A **user story** is a short description of a feature told from the perspective of the end user.

**Format:**

```
As a [type of user],
I want to [perform some action],
so that [I achieve some goal / value].
```

**Examples:**

> *As a student, I want to resume my last lesson when I return to the app, so that I don't have to scroll to find where I left off.*

> *As an instructor, I want to see how many students have completed each lesson, so that I can identify where learners are struggling.*

**Acceptance criteria** define the conditions that must be true for the story to be considered "done":

```
Story: Student can reset their password

Acceptance Criteria:
✓ A "Forgot password?" link appears on the login page
✓ Clicking it requests an email address
✓ An email is sent within 60 seconds with a reset link
✓ The reset link expires after 1 hour
✓ Clicking an expired link shows a clear error with an option to request a new one
✓ After a successful reset, the user is redirected to the login page
```

**The INVEST checklist for user stories:**

| Letter | Meaning |
|--------|---------|
| **I** | Independent — can be delivered alone |
| **N** | Negotiable — details can be discussed |
| **V** | Valuable — provides value to a user or business |
| **E** | Estimable — team can size it |
| **S** | Small — fits in a sprint |
| **T** | Testable — acceptance criteria can be verified |

---

### Lesson 4.2 — Sprint Planning and Backlog Refinement

**Backlog refinement** (also called grooming) is the ongoing process of keeping the backlog ready. It happens 1–2× per sprint:

- Add new items
- Remove items that are no longer relevant
- Split large stories into smaller ones
- Add detail and acceptance criteria
- Estimate items (planning poker)

**Sprint planning:**

1. **Part 1 — What:** The Product Owner presents the top backlog items. The team selects items it is confident it can complete in the sprint, forming the **Sprint Goal**.
2. **Part 2 — How:** The team breaks selected stories into tasks and estimates hours/effort for each task.

**Definition of Ready (DoR)** — a story is ready for the sprint if:
- It has clear acceptance criteria
- It is estimated
- Dependencies are identified
- It is small enough to complete in the sprint

**Definition of Done (DoD)** — a story is done when:
- Code is written and peer-reviewed
- Unit and integration tests pass
- Feature is tested against acceptance criteria
- Documentation is updated
- Code is merged and deployed to the test environment

---

### Lesson 4.3 — Daily Standups, Reviews, and Retrospectives

**Daily Standup (Daily Scrum):**

Each team member answers three questions in ≤15 minutes:
1. What did I complete yesterday?
2. What will I work on today?
3. Is anything blocking me?

The standup is *not* a status report to the manager — it is a synchronisation meeting for the team. Detailed discussions are taken offline.

**Sprint Review:**

- The team demos the working increment to stakeholders
- Product Owner confirms what is "Done"
- Stakeholders give feedback that may update the backlog
- No slides — live demos of working software only

**Retrospective:**

The retrospective is the team's opportunity to improve their own process. A common format is **Start / Stop / Continue**:

| Category | Question |
|----------|----------|
| **Start** | What should we begin doing that we aren't? |
| **Stop** | What are we doing that isn't helping? |
| **Continue** | What is working well that we should keep? |

Other formats: 4Ls (Liked, Learned, Lacked, Longed for), Mad/Sad/Glad, Sailboat.

**Key principle:** Retrospective actions must be SMART and assigned to a named person, or they will not get done.

---

### Lesson 4.4 — Velocity, Burn-Down Charts, and Metrics

**Velocity** is the average number of story points a team completes per sprint. It is used for forecasting, not performance management.

```
Sprint 1: 24 pts completed
Sprint 2: 31 pts completed
Sprint 3: 27 pts completed
─────────────────────────
Average velocity: 27 pts/sprint

Remaining backlog: 135 pts
Estimated sprints remaining: 135 ÷ 27 ≈ 5 sprints
```

**Burn-down chart:**

A burn-down chart shows remaining work (story points or tasks) against time in the sprint.

```
  SP
40 ┤╲
35 ┤ ╲  (ideal line)
30 ┤  ╲      ╮
25 ┤   ╲    actual
20 ┤    ╲  ╱
15 ┤     ╲╱
10 ┤
 5 ┤
 0 ┤─────────────────
   D1 D2 D3 D4 D5 D6 D7 D8 D9 D10
```

- Line **above** ideal: team is behind
- Line **below** ideal: team is ahead
- Flat line: work is not being completed (or nothing is being logged)

**Useful Agile metrics:**

| Metric | What it measures |
|--------|-----------------|
| **Velocity** | Team throughput per sprint |
| **Cycle time** | Time from "in progress" to "done" for a single item |
| **Lead time** | Time from item creation to delivery |
| **Sprint goal achievement rate** | % of sprints where the Sprint Goal was met |
| **Bug escape rate** | Bugs found in production vs. found in testing |

**Important:** Metrics should improve the team's process, not be used to compare teams or individuals.

---

## Module 5 — Modern Tools and DevOps

### Lesson 5.1 — DevOps: CI/CD and Continuous Delivery

**DevOps** is the practice of breaking down the wall between development and operations. The goal: ship software faster, more reliably, and sustainably.

**Core DevOps practices:**

| Practice | Description |
|----------|-------------|
| **Continuous Integration (CI)** | Every code commit is automatically built and tested |
| **Continuous Delivery (CD)** | Every passing build is automatically deployable to a staging environment |
| **Continuous Deployment** | Every passing build is automatically deployed to production |
| **Infrastructure as Code (IaC)** | Servers and infrastructure are defined in version-controlled files |
| **Monitoring and Observability** | Production systems are continuously monitored for errors and performance |

**A typical CI/CD pipeline:**

```
Developer pushes code
         │
         ▼
    Linting + Type Check
         │
         ▼
    Unit Tests
         │
         ▼
    Integration Tests
         │
         ▼
    Build (Docker image / bundle)
         │
         ▼
    Deploy to Staging
         │
         ▼
    Smoke Tests on Staging
         │
         ▼
    Deploy to Production   ◄── manual gate (CD) or automatic (Continuous Deployment)
         │
         ▼
    Monitor (alerts, dashboards, logs)
```

**CI tools:** GitHub Actions, GitLab CI, CircleCI, Jenkins
**Monitoring tools:** Datadog, Grafana, Sentry, PagerDuty

**The DORA metrics** (industry standard for measuring DevOps performance):

| Metric | Elite teams |
|--------|-------------|
| Deployment frequency | Multiple times per day |
| Lead time for changes | Less than 1 hour |
| Change failure rate | Less than 5% |
| Mean time to restore | Less than 1 hour |

---

### Lesson 5.2 — Project Management Tools

Knowing the tools every professional team uses is part of being job-ready.

**Backlog and issue tracking:**

| Tool | Best for |
|------|---------|
| **Jira** | Large teams, complex workflows, deep reporting |
| **Linear** | Engineering-focused teams, fast and keyboard-driven |
| **GitHub Projects** | Teams already on GitHub, lightweight kanban |
| **Trello** | Small teams, simple kanban boards |
| **Notion** | Documentation-heavy teams that also want basic project tracking |

**Communication:**

| Tool | Use case |
|------|---------|
| **Slack / Teams** | Real-time messaging, team channels |
| **Confluence / Notion** | Internal documentation and wikis |
| **Loom** | Async video updates and demos |

**Design and prototyping:**

| Tool | Use case |
|------|---------|
| **Figma** | UI design, prototyping, design handoff |
| **Miro / FigJam** | Collaborative diagramming, retrospectives, workshops |
| **draw.io / Lucidchart** | Architecture and flow diagrams |

**A healthy team combines these tools deliberately:**
1. Conversations happen in Slack
2. Decisions are documented in Confluence/Notion
3. Work is tracked in Jira/Linear
4. Code lives in GitHub/GitLab
5. Designs live in Figma

---

## Quick Reference

### SDLC Phases at a Glance

```
PLAN → REQUIREMENTS → DESIGN → DEVELOP → TEST → DEPLOY → MAINTAIN
  │          │           │         │         │       │         │
Scope    User stories  Architecture Code   Test    Release   Bug fixes
Budget   Wireframes    DB schema   Review  Reports Monitor   Updates
Risk     Use cases     API design  Tests           Rollback  Refactor
```

### Agile vs Waterfall Decision Matrix

```
Stable requirements + regulated industry + fixed price  →  Waterfall
Evolving requirements + active users + frequent releases →  Agile/Scrum
Continuous flow of support or ops work                  →  Kanban
Large org, multiple Agile teams                         →  SAFe
```

### Sprint Rhythm (2-week sprint)

```
Mon W1  │ Sprint Planning (4h)
Tue–Fri W1 │ Development + Daily Standup (15min)
Mon–Thu W2 │ Development + Daily Standup (15min)
Fri W2  │ Sprint Review (2h) + Retrospective (1.5h)
```

---

## Review Questions

**Module 1**
1. What was the Software Crisis and what caused it?
2. What are the six phases of the SDLC? Give one key deliverable for each.
3. What is the difference between a Product Owner and a Scrum Master?

**Module 2**
4. What is the difference between a functional and a non-functional requirement? Give one example of each.
5. What is the difference between Continuous Delivery and Continuous Deployment?
6. Name three deployment strategies and describe the risk level of each.

**Module 3**
7. What are the four values of the Agile Manifesto?
8. In Scrum, what is the difference between the Product Backlog and the Sprint Backlog?
9. What does WIP limit mean in Kanban, and why does limiting it help?

**Module 4**
10. Write a valid user story for the following scenario: "Learners want to download their certificate as a PDF."
11. What is the Definition of Done (DoD) and why is it important?
12. A burn-down chart shows a flat line for three days in a row. What could this indicate?

**Module 5**
13. What does CI stand for and what problem does it solve?
14. Name the four DORA metrics and state the elite benchmark for each.
15. Your team needs to track bugs, write technical documentation, and manage sprint backlog. Which combination of tools would you recommend and why?

---

## Practical Exercises

### Exercise 1 — Phase Identification
Read a news article about a major software failure (e.g. the Healthcare.gov launch in 2013, the Knight Capital trading glitch, or the Boeing 737 MAX MCAS software). Identify which SDLC phase the failure originated in and what could have prevented it.

### Exercise 2 — Write User Stories
For a simple to-do app, write five user stories covering:
1. Creating a task
2. Marking a task complete
3. Filtering tasks by status
4. Setting a due date on a task
5. Deleting completed tasks

For each, write at least three acceptance criteria.

### Exercise 3 — Planning Poker
In groups of 3–5, estimate the effort for the user stories written in Exercise 2 using the Fibonacci sequence (1, 2, 3, 5, 8, 13). Discuss disagreements until the group reaches consensus.

### Exercise 4 — Sprint Board
Using GitHub Projects, Linear (free tier), or a physical whiteboard, set up a sprint board with the following columns:
**Backlog → Ready → In Progress (WIP: 2) → Review → Done**

Move at least one user story from Exercise 2 through all columns.

### Exercise 5 — Mini Retrospective
After completing a group project or assignment, run a 30-minute retrospective using the Start / Stop / Continue format. Document at least two action items with assigned owners and a target completion date.

---

## Glossary

| Term | Definition |
|------|-----------|
| **SDLC** | Software Development Lifecycle — the structured process for planning, creating, testing, and deploying software |
| **Requirements** | A statement of what a system must do (functional) or how well it must do it (non-functional) |
| **Agile** | A philosophy of software development that values flexibility, collaboration, and delivering working software frequently |
| **Scrum** | An Agile framework using fixed-length Sprints, three roles (PO, SM, Dev), three artefacts, and four ceremonies |
| **Kanban** | A flow-based Agile method that visualises work and limits work in progress |
| **Sprint** | A fixed time-box (1–4 weeks) in Scrum during which a potentially shippable product increment is created |
| **User story** | A feature description written from the end-user's perspective: "As a…, I want to…, so that…" |
| **Acceptance criteria** | Conditions that must be met for a user story to be considered complete |
| **Product Backlog** | An ordered list of everything that might be needed in the product |
| **Sprint Backlog** | The set of items selected for the current sprint plus the plan to deliver them |
| **Velocity** | The average number of story points completed per sprint |
| **Burn-down chart** | A chart showing remaining work against time in a sprint |
| **CI** | Continuous Integration — automatically building and testing every code commit |
| **CD** | Continuous Delivery/Deployment — automatically releasing tested code to staging or production |
| **Definition of Done** | A shared agreement on what "complete" means for a story or sprint |
| **Technical debt** | The accumulated cost of shortcuts and quick fixes that make future changes harder |
| **Retrospective** | A ceremony held at the end of each sprint to reflect on and improve the team's process |
| **WIP limit** | A constraint on how many items can be in a given workflow stage simultaneously |
| **DORA metrics** | Four industry-standard metrics for measuring software delivery performance |
| **Feature flag** | A technique to deploy code that is hidden until deliberately enabled for specific users |

---

*Reference: [Agile Manifesto](https://agilemanifesto.org) · [Scrum Guide](https://scrumguides.org) · [DORA State of DevOps Report](https://dora.dev)*
