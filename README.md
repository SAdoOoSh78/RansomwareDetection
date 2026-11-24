# Ransomware Early Warning System

A small web application that **watches a folder, detects abnormal file-change bursts, and shows a clear warning on a dashboard**. It is a study project for Fontys ICT (IN-CST, Semester 2), built with Python and Flask using Scrum.

> The goal is *early warning*, not protection. The system detects and alerts. It does **not** block or remove ransomware, restore files, or scan a whole computer.

---

## What it does

1. **Monitor** a user-chosen folder for file changes (create / modify / delete / rename).
2. **Detect** suspicious activity: too many file changes in a short time window, or files getting bad extensions such as `.encrypted` / `.locked`.
3. **Alert**: save each alert with a timestamp and keep a history.
4. **Dashboard**: show the live status, recent events, and alert history in the browser.

### In scope
Folder watching, change detection, count-per-time-window rule, bad-extension detection, ignoring temp/system files, saving alerts + history, a dashboard, a settings page, (a chart if there is time).

### Out of scope
Blocking or removing ransomware, restoring files, whole-computer or multi-PC monitoring, real ransomware samples, email/SMS alerts, user login.

---

## Team & roles

| Area | Owner | Responsibility |
|------|-------|----------------|
| `monitoring/` | **Fady** | Watch the folder, detect modify/delete/rename, ignore temp files, build the fake-ransomware test script |
| `detection/` | **Saeed** | Count file changes per time window + the rule that decides "suspicious"; bad-extension detection; reduce false alarms |
| `dashboard/` | **Oche** | Flask web dashboard: status, events, history, settings |
| `alerts/` | **Ammar** | Alert system + logging: save alerts with timestamps, keep history, connect to the website |

*Product owner / assessor: Gayatri. Methodology: Scrum, two sprints.*

> Names map to folders so everyone knows which part is theirs. Edit this table if roles change.

---

## Project structure

```
RansomwareDetection/
├── app.py                  # Entry point: wires monitoring -> detection -> alerts -> dashboard
├── config.py               # Settings (watched folder, thresholds, ignore rules)
├── requirements.txt        # Python dependencies
├── monitoring/             # Fady  - file-system watcher
│   └── watcher.py
├── detection/              # Saeed - suspicious-activity detection
│   └── detector.py
├── alerts/                 # Ammar - alerts + logging
│   └── alerts.py
├── dashboard/              # Oche  - Flask web dashboard
│   ├── routes.py
│   └── templates/
│       └── index.html
├── tools/
│   └── fake_ransomware.py  # Test script: simulates a ransomware-style file-change burst
└── docs/
    ├── SPRINT_PLAN.md       # MoSCoW, user stories, sprint goals
    └── DEFINITION_OF_DONE.md
```

The files contain **working stubs** that already fit together, so the app runs from day one. Each owner fills in and improves their own part.

---

## Getting started

### 1. Requirements
- Python 3.10 or newer
- Git

### 2. Set up

```bash
# clone your copy of the repo
git clone https://github.com/SAdoOoSh78/RansomwareDetection.git
cd RansomwareDetection

# create and activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

### 3. Run

```bash
python app.py
```

Then open **http://127.0.0.1:5000** in your browser. By default the app watches a folder called `watched/` in the project (it is created automatically).

### 4. Test it

In a second terminal (with the venv active), run the test script to simulate a ransomware-style burst in the watched folder:

```bash
python tools/fake_ransomware.py
```

Watch the dashboard: an alert should appear within a second or two.

---

## How to work together (Git)

We use **feature branches** so no one edits `main` directly.

```bash
git checkout -b your-name/short-description   # e.g. saeed/detection-threshold
# ... make your changes ...
git add .
git commit -m "detection: add sliding-window counter"
git push -u origin your-name/short-description
```

Then open a **Pull Request** on GitHub and ask a teammate to review before merging into `main`.

**Golden rules**
- Work only in your own folder unless you agree a change with the owner.
- Pull `main` before you start, so you have the latest.
- Small, clear commits. One thing per commit.
- A change is done only when it meets the [Definition of Done](docs/DEFINITION_OF_DONE.md).

---

## Sprints

- **Sprint 1** — a first working version: watch a folder, detect a change burst, raise an alert, show it on the dashboard.
- **Sprint 2** — improve after teacher feedback: explain *why* something is suspicious, detect bad extensions, reduce false alarms, polish the dashboard.

See [docs/SPRINT_PLAN.md](docs/SPRINT_PLAN.md) for the backlog and sprint goals.
