"""
Central settings for the Ransomware Early Warning System.

Change the values here instead of editing them in many files.
The dashboard settings page can later update these at run time.
"""

import os

# Folder that the system watches. Created automatically if missing.
WATCHED_FOLDER = os.path.join(os.path.dirname(__file__), "watched")

# --- Detection rule (Saeed) ---
# "Suspicious" = more than THRESHOLD file changes within WINDOW_SECONDS.
WINDOW_SECONDS = 5
THRESHOLD = 10

# File extensions that are a strong sign of ransomware.
BAD_EXTENSIONS = {".encrypted", ".locked", ".crypt", ".enc", ".crypto"}

# Temp / system files we ignore, so we do not raise false alarms.
IGNORE_SUFFIXES = {".tmp", ".swp", ".part", "~"}
IGNORE_NAMES = {".DS_Store", "Thumbs.db"}

# --- Web dashboard (Oche) ---
HOST = "127.0.0.1"
PORT = 5000

# --- Alerts / logging (Ammar) ---
ALERTS_FILE = os.path.join(os.path.dirname(__file__), "alerts.json")
MAX_HISTORY = 200
