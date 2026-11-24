"""
Suspicious-activity detection  (Owner: Saeed)

The detector receives file events from the monitor and decides whether the
recent activity looks like ransomware. When it does, it raises an alert.

Sprint 1 rule (done here as a baseline):
    "Suspicious" = more than THRESHOLD file changes within WINDOW_SECONDS.

Sprint 2 (your work - marked with TODO below):
    - explain WHY it is suspicious (with Ammar)
    - detect bad extensions (.encrypted / .locked ...)
    - reduce false alarms

Feel free to rewrite this file - it is your component.
"""

import time
from collections import deque

import config


class Detector:
    def __init__(self, alert_store):
        self.alert_store = alert_store
        # Timestamps of recent file changes (the "sliding window").
        self._events = deque()
        # The most recent events, kept so the dashboard can show activity.
        self.recent = deque(maxlen=50)
        # Avoid spamming: do not re-alert within this many seconds.
        self._last_alert_time = 0
        self._alert_cooldown = 5

    # Called by the monitor for every file change.
    def handle_event(self, event):
        now = event.time
        self.recent.appendleft(event)

        # 1. Add this change to the sliding window and drop old ones.
        self._events.append(now)
        self._trim_window(now)

        # 2. Count how many changes happened inside the window.
        count = len(self._events)

        # 3. Check the bad-extension signal (Sprint 2 - see helper below).
        bad_ext = self._has_bad_extension(event)

        # 4. Apply the rule.
        if count > config.THRESHOLD or bad_ext:
            reason = self._explain(count, bad_ext, event)
            self._maybe_alert(now, reason, count)

    def _trim_window(self, now):
        cutoff = now - config.WINDOW_SECONDS
        while self._events and self._events[0] < cutoff:
            self._events.popleft()

    def _has_bad_extension(self, event):
        # TODO (Saeed, Sprint 2): make this smarter / configurable.
        name = event.name.lower()
        return any(name.endswith(ext) for ext in config.BAD_EXTENSIONS)

    def _explain(self, count, bad_ext, event):
        # TODO (Saeed + Ammar, Sprint 2): build a clearer "why" message.
        parts = []
        if count > config.THRESHOLD:
            parts.append(
                f"{count} file changes in {config.WINDOW_SECONDS}s "
                f"(limit is {config.THRESHOLD})"
            )
        if bad_ext:
            parts.append(f"suspicious extension on '{event.name}'")
        return "; ".join(parts) or "unusual file activity"

    def _maybe_alert(self, now, reason, count):
        # TODO (Saeed, Sprint 2): tune the cooldown to reduce false alarms.
        if now - self._last_alert_time < self._alert_cooldown:
            return
        self._last_alert_time = now
        self.alert_store.add(reason=reason, change_count=count)

    # Used by the dashboard to show the current state.
    def status(self):
        self._trim_window(time.time())
        return {
            "changes_in_window": len(self._events),
            "window_seconds": config.WINDOW_SECONDS,
            "threshold": config.THRESHOLD,
        }
