# Git & GitHub — Web Fundamentals

**Track:** Web Fundamentals
**Modules:** 3
**Total Lessons:** 9
**Prerequisite:** None (runs alongside all other courses)

## Module 1 — Local Version Control

### Lesson 1.1 — What is Version Control?

**The problem without Git:**

You create `index.html`. You make changes. You want to go back to yesterday's version. Without Git, you either lost it or you have 12 files called `index_final_ACTUALLY_final_v3.html`.

With Git, every saved version of your project is stored permanently. You can go back to any point. You can see exactly what changed, when, and who changed it. Multiple developers can work on the same project without overwriting each other.

**Git vs GitHub:**

| Git | GitHub |
|-----|--------|
| Software on your computer | A website (cloud service) |
| Tracks local file history | Stores your Git repo online |
| Works offline | Requires internet |
| Command-line tool | Web interface, collaboration |
| Open source | Owned by Microsoft |

Git is the tool. GitHub is one place to store your Git repositories. (Others: GitLab, Bitbucket.)

**Installing and configuring:**

```bash
# Check if already installed
git --version

# Install (Ubuntu/Debian)
sudo apt install git

# Install (macOS via Homebrew)
brew install git

# Windows: download from git-scm.com

# Configure identity — runs once, stored globally
git config --global user.name  "Your Full Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"   # VS Code as editor
git config --global init.defaultBranch main      # use 'main' not 'master'

# Verify
git config --list
```

**Exercises**

**1.1.1** — Install Git and configure your name, email, and editor. Run `git config --list` and screenshot the output.

**1.1.2** — In three sentences: explain Git to someone who has never heard of it. Post in the community and read two classmates' explanations.

### Lesson 1.2 — Core Git Workflow

**The three stages:**

```
Working Directory   →    Staging Area    →    Repository
(files you edit)         (git add)             (git commit)

"I changed files"        "I chose which         "I saved a snapshot
                          changes to save"       permanently"
```

**Your first repository:**

```bash
# Create a project folder
mkdir my-portfolio && cd my-portfolio

# Initialise Git (creates hidden .git/ folder)
git init

# Create a file
echo "# My Portfolio" > README.md

# Check current state
git status
# → On branch main
# → Untracked files: README.md
```

**The commit cycle:**

```bash
# Stage a specific file
git add README.md

# Stage everything changed
git add .

# Preview exactly what will be committed
git diff --staged

# Commit with a message
git commit -m "feat: add README with project overview"

# View history
git log
git log --oneline            # compact — one line per commit
git log --oneline --graph    # with branch visualisation
git show abc1234             # details of a specific commit
```

**Conventional Commit Messages:**

Every commit message follows the format: `type(scope): description`

| Type | When to use |
|------|------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `style` | CSS / formatting only |
| `refactor` | Code restructure — no feature or bug |
| `docs` | Documentation only |
| `chore` | Build tools, config, dependencies |
| `test` | Adding or updating tests |

```bash
# Good messages
git commit -m "feat: add dark mode toggle"
git commit -m "fix: nav links not working on mobile"
git commit -m "style: update button hover colour"
git commit -m "docs: add setup instructions to README"

# Bad messages — never use these
git commit -m "update"
git commit -m "stuff"
git commit -m "wip"
git commit -m "asdfgh"
```

**.gitignore:**

```bash
# Create .gitignore in the project root
touch .gitignore
```

```gitignore
# Dependencies — always
node_modules/

# Environment variables — NEVER commit these
.env
.env.local
.env.*.local

# Build output
dist/
build/
.next/

# OS / editor
.DS_Store
Thumbs.db
.vscode/settings.json
.idea/

# Logs
*.log
```

**Exercises**

**1.2.1** — Create a new project folder. Initialise Git. Create three files (`index.html`, `style.css`, `script.js`). Make three commits — one file per commit — each using a conventional commit message.

**1.2.2** — Run `git log --oneline`. Screenshot it. How many commits? What would a reviewer learn from reading your commit history?

**1.2.3** — Create a `.gitignore` that ignores `node_modules`, `.env`, and `.DS_Store`. Verify with `git status` that those paths don't appear as untracked files.

### Lesson 1.3 — Undoing Mistakes

```bash
# ── Not yet staged ──
git restore index.html         # discard changes to one file
git restore .                  # discard ALL unstaged changes

# ── Staged but not committed ──
git restore --staged index.html  # unstage (keeps changes in working dir)
git restore --staged .           # unstage everything

# ── Committed ──

# Show what you're about to undo
git log --oneline

# Undo last commit, keep changes STAGED
git reset --soft HEAD~1

# Undo last commit, keep changes UNSTAGED (default)
git reset HEAD~1

# Undo last commit, DELETE the changes (irreversible)
git reset --hard HEAD~1

# Undo safely by creating a NEW commit that reverses changes
# Use this for commits already pushed to GitHub
git revert HEAD
git revert abc1234
```

**When to use what:**

| Situation | Command |
|-----------|---------|
| Changed my mind before staging | `git restore .` |
| Staged the wrong files | `git restore --staged .` |
| Last commit needs fixing, not yet pushed | `git reset --soft HEAD~1` |
| Need to undo a pushed commit safely | `git revert HEAD` |
| Nuclear option — abandon everything since last commit | `git reset --hard HEAD` |

**Git stash — park work temporarily:**

```bash
git stash                            # save current changes
git stash push -m "wip: search bar"  # save with description
git stash list                       # list all stashes
git stash pop                        # apply most recent + remove from list
git stash apply                      # apply most recent, keep in list
git stash apply stash@{2}            # apply specific stash
git stash drop stash@{0}             # delete a stash
git stash clear                      # delete all stashes
```

**Typical stash workflow:**

```bash
# Working on feature, urgent bug reported
git stash push -m "wip: half-built search"

# Switch to main, fix the bug, push
git switch main
git pull
git switch -c fix/nav-link-bug
# ... fix it ...
git commit -m "fix: nav links broken on mobile"
git push

# Back to feature
git switch feature/search-bar
git stash pop   # restore saved work
```

**Exercises**

**1.3.1** — Practice every undo: make a change → restore before staging. Stage it → restore --staged. Commit it → reset --soft. Commit and push → revert. Log the state after each step.

**1.3.2** — Stash your current work on one branch, switch to another branch, do some work, switch back, and pop the stash. Verify both sets of changes are intact.

## Module 2 — GitHub & Collaboration

### Lesson 2.1 — GitHub: Remote Repositories

**Creating a repository:**
1. github.com → **+** → **New repository**
2. Name: lowercase, hyphens (e.g. `bio-page`, `weather-app`)
3. Set to **Public** — builds your portfolio
4. Do **NOT** initialise with README if you have local files already
5. Click **Create repository**

**Connecting local to remote:**

```bash
# Add GitHub as a remote named "origin"
git remote add origin https://github.com/yourusername/bio-page.git

# Rename branch to main (if needed)
git branch -M main

# Push and set upstream (-u) — only needed the first time
git push -u origin main

# After the first push, just:
git push
git pull
```

**Working across machines or with teammates:**

```bash
# Download the entire repo (first time on a new machine)
git clone https://github.com/yourusername/bio-page.git
cd bio-page

# Get the latest changes others have pushed
git pull
```

**GitHub Pages — free static hosting:**
1. Repository → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main**, folder: **/ (root)**
4. Save → your site is live at `https://yourusername.github.io/repo-name/`

**Professional README template:**

```markdown
# Project Name

One-sentence description of what this project does.

## Built with
- HTML5, CSS3 (Flexbox, Grid, custom properties)
- Vanilla JavaScript (Fetch API, localStorage)
- Deployed to GitHub Pages

## Features
- Responsive — works on all screen sizes
- Dark / light theme with preference saved to localStorage
- Live data from [API name] API

## Setup
1. Clone: `git clone https://github.com/yourusername/project-name.git`
2. Open `index.html` in your browser, or use Live Server in VS Code.
3. Add your API key to `config.js` (see `config.example.js`).

## Screenshots
![Desktop](screenshots/desktop.png)
```

**Exercises**

**2.1.1** — Create a GitHub repository for your bio page. Push your local code. Enable GitHub Pages. Share the live URL in the community.

**2.1.2** — Write a proper README following the template. It must include: description, live URL, built-with, features, and setup instructions. Commit and push.

### Lesson 2.2 — Branching & Merging

**Why branch:** `main` should always be deployable, working code. Every new feature lives on its own branch until it's reviewed and ready.

```bash
# List branches (* = current)
git branch
git branch -a           # including remote branches

# Create a branch
git branch feature/dark-mode

# Switch to it (modern syntax)
git switch feature/dark-mode

# Create AND switch in one command (preferred)
git switch -c feature/contact-form

# Rename current branch
git branch -m new-name

# Delete a branch (safe — only if merged)
git branch -d feature/dark-mode

# Force delete (merged or not)
git branch -D feature/dark-mode
```

**The feature branch workflow:**

```bash
# 1. Start from fresh main
git switch main
git pull

# 2. Create a feature branch
git switch -c feature/search-bar

# 3. Work and commit often
git add .
git commit -m "feat: add search input to header"
git add .
git commit -m "feat: filter products by search query"

# 4. Merge when done
git switch main
git merge feature/search-bar

# 5. Delete the branch
git branch -d feature/search-bar

# 6. Push to GitHub
git push
```

**Resolving merge conflicts:**

When two branches change the same part of the same file, Git cannot decide which to keep:

```html
<<<<<<< HEAD   (your current branch — main)
<h1>Welcome to my portfolio</h1>
=======
<h1>Welcome to my website</h1>
>>>>>>> feature/update-heading
```

To resolve:
1. Open the file in VS Code
2. Choose what you want — delete the conflict markers
3. Save the file
4. `git add index.html`
5. `git commit -m "fix: resolve heading merge conflict"`

**Exercises**

**2.2.1** — Create a branch called `feature/skills-section`. Add a skills section to your bio page on that branch (two commits). Merge back to `main`. Run `git log --oneline --graph` and screenshot the merge.

**2.2.2** — Deliberately create a merge conflict: make a different change to the same line on two branches. Resolve the conflict. Write a post in the community explaining what caused it and how you fixed it.

### Lesson 2.3 — Pull Requests & Code Review

**Opening a pull request:**

```bash
# Push your feature branch
git push -u origin feature/search-bar
```

On GitHub: banner appears → "Compare & pull request" → click it.

- **Base:** `main` (where you're merging into)
- **Compare:** `feature/search-bar` (what you're proposing)

**A good PR description:**

```markdown
## What this does
Adds a real-time search bar to the products page. As the user types,
the product list filters without a page reload.

## Changes
- Added `<input id="search">` to `index.html`
- Added `filterProducts(query)` to `script.js`
- Added focus styles to `style.css`

## How to test
1. Open the products page
2. Type in the search box
3. Products should filter in real time
4. Clear the box — all products return

## Related issue
Closes #12
```

**Code review — what to look for:**
- Does it do what the description says?
- Any bugs or edge cases not handled?
- Readable variable and function names?
- Any security issues (e.g. `innerHTML` with user input)?
- Anything that could be simpler?

**How to write review comments:**
- Specific: "Line 34 — `innerHTML` with `item.name` is an XSS risk. Use `textContent` instead."
- Questioning: "Why is this called twice? Is that intentional?"
- Constructive: "This could be a one-liner: `items.filter(i => i.active).map(i => i.name)`"
- Positive: "Nice use of event delegation here — much cleaner than attaching individual listeners."

**Merging and cleanup:**
1. Get approval from reviewer
2. **Merge pull request** → Confirm
3. **Delete branch** (GitHub offers a button)

```bash
# Update local main
git switch main
git pull
git branch -d feature/search-bar
```

**Branch protection — required for professional projects:**
- Repository → Settings → Branches → Add rule
- Branch: `main`
- Enable: "Require a pull request before merging"
- Enable: "Require at least 1 approval"
- Enable: "Require status checks to pass"

**Exercises**

**2.3.1** — Push a feature branch. Open a PR with a description using the template above. Share the PR URL in the community and request a review.

**2.3.2** — Review a classmate's PR. Leave three specific comments: one genuine praise, one suggested improvement, one question. Use the proper GitHub review interface.

**2.3.3** — Address the feedback on your own PR. For each comment: make the change or explain why you disagree. Merge when approved.

## Module 3 — CI/CD & Professional Workflow

### Lesson 3.1 — GitHub Actions: Your First CI Pipeline

**CI/CD:**
- **CI** (Continuous Integration) — automatically run tests and checks on every push
- **CD** (Continuous Deployment) — automatically deploy when checks pass

A green CI badge on your PR tells reviewers: the code builds, passes lint, and tests pass. A red badge says "don't merge this."

**Workflow file:**

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  quality:
    name: Lint & Build
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint

      - name: Check formatting
        run: npm run format:check

      - name: Build
        run: npm run build
```

```json
// package.json scripts
{
  "scripts": {
    "lint":         "eslint src --ext .js,.jsx",
    "format":       "prettier --write .",
    "format:check": "prettier --check .",
    "build":        "vite build"
  }
}
```

**What happens on every push:**
1. GitHub spins up a fresh Ubuntu machine
2. Checks out your code
3. Installs Node 20 and your dependencies
4. Runs ESLint — any errors fail the workflow (red ✕)
5. Runs Prettier check — any formatting issues fail the workflow
6. Runs the build — any compile errors fail the workflow

A failing workflow blocks the PR from being merged if branch protection is enabled.

**Exercises**

**3.1.1** — Add `.github/workflows/ci.yml` to your project. Push it. Watch the Actions tab. Take a screenshot of the green workflow run.

**3.1.2** — Introduce a deliberate ESLint error (unused variable). Push it. Screenshot the red ✕. Fix the error. Push again. Screenshot the green ✓.

### Lesson 3.2 — Secrets & Environment Variables in CI

**The problem:** Your app needs an API key. That key must never go in your code (it would be public on GitHub). But CI also needs the key to run correctly.

**Solution: GitHub Secrets**

1. Repository → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**
3. Name: `ANTHROPIC_API_KEY`
4. Value: your actual key
5. Save

```yaml
# Use the secret in your workflow
jobs:
  test:
    runs-on: ubuntu-latest
    env:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      OPENAI_API_KEY:    ${{ secrets.OPENAI_API_KEY }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20", cache: "npm" }
      - run: npm ci
      - run: npm test
```

**In your codebase:**

```javascript
// .env.local (NEVER commit — in .gitignore)
ANTHROPIC_API_KEY=sk-ant-api03-...

// In code (Vite exposes VITE_ prefixed vars)
const apiKey = import.meta.env.VITE_ANTHROPIC_API_KEY;

// Or in Node/Next.js
const apiKey = process.env.ANTHROPIC_API_KEY;
```

**Rules:**
- `.env.local` is in `.gitignore` — never staged, never committed
- Provide a `.env.example` with placeholder values that IS committed
- GitHub Secrets are encrypted — even Anthropic employees can't read them
- Secret values are masked in CI logs (`***`)

**Exercises**

**3.2.1** — Add your weather API key as a GitHub Secret. Update your CI workflow to use `${{ secrets.WEATHER_API_KEY }}`. Verify the workflow still passes and the key is not visible in the logs.

**3.2.2** — Create a `.env.example` file in your project with placeholder values for all required environment variables. Commit it to GitHub.

### Lesson 3.3 — Professional Git Workflow & Review

**The complete professional workflow:**

```bash
# Start every feature
git switch main && git pull
git switch -c feature/my-feature

# Work — commit often
git add .
git commit -m "feat: add component structure"
git add .
git commit -m "feat: implement filter logic"
git add .
git commit -m "test: add unit tests for filter"

# Push and open PR
git push -u origin feature/my-feature
# → Open PR on GitHub with description

# After review — address feedback
git add .
git commit -m "fix: address review comments"
git push

# Merge on GitHub → delete branch on GitHub
# Locally
git switch main && git pull
git branch -d feature/my-feature
```

**Branch naming conventions:**

```
feature/  — new functionality       feature/user-authentication
fix/      — bug fix                 fix/nav-links-mobile
style/    — visual only             style/update-button-hover
docs/     — documentation           docs/add-api-reference
chore/    — build/config/deps       chore/upgrade-to-node-20
refactor/ — code cleanup            refactor/extract-api-helpers
```

**Complete checklist:**

- [ ] `git config` set up with real name and email
- [ ] All projects have a `.gitignore` with `node_modules`, `.env`, build folders
- [ ] Commit messages follow conventional commits format
- [ ] Every feature built on a branch, not directly on `main`
- [ ] PRs have a clear title and description
- [ ] At least one real PR reviewed — with comments left
- [ ] GitHub Pages deployed for at least two projects
- [ ] CI workflow running on at least one project
- [ ] API keys stored as GitHub Secrets, never in code
- [ ] Branch protection enabled on `main` of at least one project

**Exercises**

**3.3.1** — Apply the full checklist to all your projects so far. Fix every "not yet" before the workshop.

**3.3.2** — Enable branch protection on your bio-page repository: require a PR, require 1 approval, require CI to pass. Try pushing directly to `main` — it should be blocked.
