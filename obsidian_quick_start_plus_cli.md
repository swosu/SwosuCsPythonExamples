# Obsidian Quick Start + CLI Starter

## What Obsidian is
Obsidian is a note-taking and knowledge-management app built around plain Markdown files stored in a folder called a **vault**. Instead of locking your notes into a proprietary format, it keeps them as regular files on your machine. That means your notes are portable, searchable, scriptable, and friendly to version control.

At its heart, Obsidian is about:
- writing notes in Markdown
- linking notes to each other with `[[double brackets]]`
- organizing knowledge over time without forcing everything into rigid folders
- keeping your notes usable outside the app

Think of it as a cross between a notebook, a wiki, and a local file system with superpowers.

---

## Why Obsidian is useful
Obsidian shines when you want your notes to be:

- **local-first**: your files live with you
- **future-proof**: Markdown is durable and widely supported
- **linked**: ideas can point to each other naturally
- **searchable**: full-text search is fast and practical
- **hackable**: you can use templates, plugins, scripts, Git, and CLI tools
- **scalable**: it works for a handful of notes or a sprawling second brain

It is especially good for:
- project notes
- research notebooks
- teaching prep
- documentation
- daily logs
- brainstorming
- personal knowledge management
- technical notes and command references

---

## How to get started fast

### 1. Install Obsidian
Download and install Obsidian for your platform.

### 2. Create a vault
A vault is just a folder of Markdown files.

Good starter vault names:
- `Notes`
- `Workbench`
- `Knowledge`
- `Thought_Garden`
- `Admin_Notes`

### 3. Make your first few notes
Start with only a few notes:
- `Inbox.md`
- `Projects.md`
- `Daily Notes/2026-04-08.md`
- `Ideas.md`
- `Reference.md`

Do not overengineer the structure on day one. Tiny vaults grow better than marble palaces.

### 4. Learn three core moves
These three moves do most of the magic:

#### Plain notes
Just write Markdown.

#### Internal links
Use:
```md
[[Project Alpha]]
```
This creates or links to another note.

#### Backlinks
When notes link to each other, Obsidian can show what points back to the current note. This is where scattered scraps start becoming a web.

---

## Simple starter structure
A low-drama starter layout:

```text
Vault/
  Inbox.md
  Daily Notes/
  Projects/
  Areas/
  Reference/
  Attachments/
  Templates/
```

Suggested meaning:
- **Inbox**: quick capture
- **Daily Notes**: day-by-day journal and scratchpad
- **Projects**: things with an outcome
- **Areas**: ongoing responsibilities
- **Reference**: things you want to keep
- **Attachments**: images, PDFs, screenshots
- **Templates**: reusable note skeletons

---

## Markdown cheat sheet

### Headings
```md
# Big heading
## Section
### Subsection
```

### Bullet list
```md
- item
- item
  - nested item
```

### Task list
```md
- [ ] todo
- [x] done
```

### Link to another note
```md
[[My Note]]
[[My Note|custom text]]
```

### Embed another note
```md
![[My Note]]
```

### Link to a heading inside a note
```md
[[My Note#Section Name]]
```

### Code block
````md
```bash
ls -la
```
````

### Callout
```md
> [!tip]
> Keep notes small and linked.
```

---

## Day-one cheat codes
These are the “less flailing, more flying” features.

### 1. Command Palette
Learn the Command Palette early. It is the universal remote.
- open commands
- search features
- run actions without hunting menus

### 2. Quick Switcher
Lets you jump to any note fast.
If you remember part of a note name, you can usually find it in seconds.

### 3. Daily Notes
Turn on Daily Notes and capture your day into one rolling log.
Great for:
- ideas
- commands you used
- meeting notes
- what broke
- what got fixed

### 4. Templates
Create a few reusable note templates.
Example templates:
- meeting note
- project note
- class prep note
- server incident note
- reading note

### 5. Properties
Use frontmatter or Properties for metadata.
Example:
```md
---
tags:
  - project
status: active
owner: jeremy
---
```

### 6. Backlinks + linked mentions
These help you discover how ideas relate without manually building giant indexes.

### 7. Keep folders simple
Use a few folders, not a baroque labyrinth with twelve sub-basements and a moat.

### 8. Search beats perfection
A searchable messy note often beats a perfectly organized note that never gets written.

---

## Best core plugins to enable first
Start light. You do not need a plugin carnival on day one.

Good first core plugins:
- **Daily notes**
- **Templates**
- **Backlinks**
- **Outline**
- **Canvas** if you like visual thinking
- **Bases** if you want database-style views of notes

Enable only what solves a real problem.

---

## Obsidian + CLI: the fun part
This is where Obsidian stops being “just notes” and starts becoming part of your system.

Obsidian’s official CLI lets you control the app from the terminal for scripting, automation, and integrations. That means you can trigger actions, work with vaults, automate routines, and even access developer-oriented commands from the command line.

### Why this matters
If your notes are Markdown files and Obsidian has CLI support, then you can combine it with:
- shell scripts
- Python
- PowerShell
- cron jobs
- Task Scheduler
- Git hooks
- external tools and local LLM workflows

In plain English: your notes can become inputs, outputs, logs, dashboards, prompts, indexes, and living documentation.

---

## CLI use ideas
Here are practical ways to tie Obsidian into CLI workflows.

### 1. Open a vault or specific note from a script
Use scripts to jump directly into the right note when starting work.

Use cases:
- open today’s daily note from a terminal alias
- open a project note from a script
- jump into a meeting note template before a call

### 2. Generate Markdown outside Obsidian
You can create `.md` files from scripts, Python programs, or shell commands and let Obsidian manage them visually.

Examples:
- export server status into `Daily Notes/`
- save AI summaries into `Reference/`
- create project logs automatically
- write meeting minutes from transcript tools

### 3. Pair Obsidian with Git
Because the vault is plain files, you can:
- version control notes
- track changes
- sync through Git remotes
- roll back mistakes
- branch experiments

This is excellent for documentation, research notes, lab notebooks, and technical writing.

### 4. Feed notes into scripts
Your Markdown files can act like structured inputs.

Examples:
- scan task checkboxes
- collect notes tagged with `#project`
- build weekly summaries from daily notes
- extract code blocks into runnable snippets
- turn notes into prompt files for LLM workflows

### 5. Automate recurring note creation
You can use shell or Python to create:
- daily notes
- weekly reviews
- project stubs
- class prep pages
- incident report shells

### 6. Use Headless mode for automation
Obsidian also documents **Obsidian Headless**, a standalone client for command-line and automated workflows without the desktop app. This is particularly interesting for automation, agents, servers, CI, and keeping synced vaults available to tooling.

That means your vault can become part of a larger workflow rather than just something you click open manually.

---

## Simple CLI-flavored starter ideas

### A. Daily note launcher
Create a script that opens or creates today’s note.

Pseudo-idea:
```text
1. Get today's date
2. Build filename like 2026-04-08.md
3. Create it if missing
4. Open it in Obsidian
```

### B. Meeting note generator
A small script could ask for:
- meeting title
- date
- attendees

Then write a templated Markdown note into `Meetings/`.

### C. System admin log
Have a script append command output to a dated note.

Example outputs you might log:
- uptime
- disk usage
- package updates
- service status
- quick problem notes

### D. AI workflow integration
Use local or hosted LLMs to generate Markdown artifacts and save them directly into your vault.

Examples:
- spark notes
- summaries
- action lists
- code review notes
- lecture prep ideas
- student feedback drafts

---

## Example Python idea for creating a note
This is not tied to any one Obsidian command. It just uses the vault as a Markdown workspace.

```python
from pathlib import Path
from datetime import date

vault = Path.home() / "ObsidianVault"
daily = vault / "Daily Notes"
daily.mkdir(parents=True, exist_ok=True)

note = daily / f"{date.today().isoformat()}.md"

if not note.exists():
    note.write_text("# Daily Note\n\n## Tasks\n- [ ] \n\n## Notes\n", encoding="utf-8")

print(f"Created: {note}")
```

That little script is enough to make Obsidian part of a repeatable workflow.

---

## Good beginner workflow
Here is a clean first-week workflow:

### Daily
- open Daily Note
- capture thoughts, tasks, links, commands, ideas

### During work
- create notes when something matters
- link notes instead of overfiling them
- use `[[links]]` freely

### Weekly
- review daily notes
- move important ideas into project or reference notes
- clean up a little, not obsessively

---

## How to learn more without drowning
Learn in this order:

### 1. Learn core note-taking first
Focus on:
- notes
- links
- search
- backlinks
- daily notes
- templates

### 2. Learn metadata next
Start using:
- tags
- properties
- filenames that make sense

### 3. Add one plugin at a time
Install only when you can name the problem it solves.

### 4. Then add CLI and automation
Once your vault has a little structure, scripting becomes much more valuable.

---

## Recommended “learn more” trail
A good progression:

1. Install Obsidian
2. Create a vault
3. Learn `[[links]]`
4. Turn on Daily Notes
5. Create 2 to 3 templates
6. Learn Properties/frontmatter
7. Explore core plugins
8. Learn the official CLI
9. Experiment with Git or scripts
10. Add community plugins only as needed

---

## Practical advice for not getting lost
- Do not try to build the perfect system in one day.
- Write notes first. Organize second.
- Use links more than folders.
- Keep templates simple.
- Let structure emerge from actual use.
- Prefer small repeated habits over giant redesigns.
- Treat the vault as a working desk, not a museum exhibit.

---

## Fast answers

### Is Obsidian good for beginners?
Yes. You can start with basic notes and ignore the advanced stuff until you want it.

### Is it good for technical people?
Very. Markdown + local files + scripting + plugins + CLI is catnip for technical workflows.

### Do I need plugins immediately?
No. Core features already go a long way.

### Can I use it with code and terminal workflows?
Absolutely. That is one of its strongest lanes.

---

## One-sentence summary
Obsidian is a Markdown-based, local-first note system that becomes especially powerful when you combine linked notes, templates, search, and automation through scripts, CLI, and plain files.

---

## Suggested next step
If you want the easiest possible on-ramp, do this:
1. install Obsidian
2. create a vault named `Workbench`
3. enable Daily Notes and Templates
4. make one project note and one daily note
5. add a tiny script that writes a note into the vault

That is enough to light the engine.
