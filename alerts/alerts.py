"""
Alerts + logging  (Owner: Ammar)

Stores alerts in memory and on disk (alerts.json) so the history survives a
restart. Also writes a line to a log file for every alert.

Keep this simple: the detector calls `add(...)`, the dashboard calls
`all()` and `latest()`.
"""

import json
import logging
import os
import time
from datetime import datetime

import config

logging.basicConfig(
    filename="ransomware_alerts.log",
    level=logging.INFO,
    format="%(asctime)s  %(message)s",
)


class AlertStore:
    def __init__(self):
        self._alerts = []
        self._load()

    def add(self, reason, change_count=0):
        alert = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "timestamp": time.time(),
            "reason": reason,
            "change_count": change_count,
        }
        self._alerts.insert(0, alert)          # newest first
        del self._alerts[config.MAX_HISTORY:]  # cap the history
        logging.info("ALERT - %s (%s changes)", reason, change_count)
        self._save()
        print(f"[ALERT] {alert['time']}  {reason}")
        return alert

    def all(self):
        return list(self._alerts)

    def latest(self):
        return self._alerts[0] if self._alerts else None

    # --- persistence ---
    def _save(self):
        try:
            with open(config.ALERTS_FILE, "w", encoding="utf-8") as f:
                json.dump(self._alerts, f, indent=2)
        except OSError as err:
            logging.warning("Could not save alerts: %s", err)

    def _load(self):
        if os.path.exists(config.ALERTS_FILE):
            try:
                with open(config.ALERTS_FILE, encoding="utf-8") as f:
                    self._alerts = json.load(f)
            except (OSError, json.JSONDecodeError):
                self._alerts = []
