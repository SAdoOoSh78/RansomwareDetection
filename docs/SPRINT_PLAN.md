# Sprint Plan

Scrum, two sprints. Product owner / assessor: **Gayatri**.
Fill in the real dates and names as a team.

---

## Product backlog (MoSCoW)

### Must have
- Watch a user-chosen folder for file changes *(Fady)*
- Count changes per time window + rule that decides "suspicious" *(Saeed)*
- Raise and store an alert with a timestamp *(Ammar)*
- Dashboard showing status + alert history *(Oche)*
- Fake-ransomware test script *(Fady)*

### Should have
- Detect bad extensions (`.encrypted`, `.locked`, ...) *(Saeed)*
- Explain *why* an alert happened *(Saeed + Ammar)*
- Ignore temp / system files *(Fady)*
- Alert history saved on disk / survives restart *(Ammar)*

### Could have
- Settings page (change folder + threshold) *(Oche)*
- A chart of activity over time *(Oche)*
- Reduce false alarms (cooldown / smarter rule) *(Saeed)*

### Won't have (out of scope)
- Blocking or removing ransomware, restoring files
- Whole-computer / multi-PC monitoring
- Real ransomware samples
- Email / SMS alerts
- User login

---

## User stories (examples - add your own)

- *As a user, I want the system to watch a folder I choose, so that my important files are monitored.*
- *As a user, I want a clear warning when many files change at once, so that I can react quickly to a possible ransomware attack.*
- *As a user, I want to see a history of alerts, so that I can review what happened and when.*

---

## Sprint 1 - first working version
**Goal:** watch a folder, detect a change burst, raise an alert, show it on the dashboard.

| Story | Owner | Done? |
|-------|-------|-------|
| Folder watcher reports file changes | Fady | ☐ |
| Sliding-window counter + threshold rule | Saeed | ☐ |
| Alert store (save + history) | Ammar | ☐ |
| Dashboard (status + history) | Oche | ☐ |
| Fake-ransomware test script | Fady | ☐ |
| Everything integrated + demo to teacher | All | ☐ |

**Sprint 1 review:** capture Gayatri's feedback here → ______

---

## Sprint 2 - improve after feedback
**Goal:** act on teacher feedback; explain *why*, detect bad extensions, reduce false alarms, polish.

| Story | Owner | Done? |
|-------|-------|-------|
| Turn feedback into concrete goals | All | ☐ |
| Explain why an alert is suspicious | Saeed + Ammar | ☐ |
| Detect bad extensions | Saeed | ☐ |
| Reduce false alarms | Saeed | ☐ |
| Settings page / chart | Oche | ☐ |
| Final integration + final demo | All | ☐ |
