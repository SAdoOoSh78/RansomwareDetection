"""
Ransomware Early Warning System - entry point.

This file wires the four parts together:

    monitoring (Fady) -> detection (Saeed) -> alerts (Ammar) -> dashboard (Oche)

Run it with:  python app.py
Then open http://127.0.0.1:5000
"""

import os
import threading

import config
from monitoring.watcher import FolderWatcher
from detection.detector import Detector
from alerts.alerts import AlertStore
from dashboard.routes import create_app


def main():
    # Make sure the watched folder exists.
    os.makedirs(config.WATCHED_FOLDER, exist_ok=True)

    # Shared objects used across the app.
    alert_store = AlertStore()
    detector = Detector(alert_store)

    # When the watcher sees a file event, it hands it to the detector.
    watcher = FolderWatcher(
        folder=config.WATCHED_FOLDER,
        on_event=detector.handle_event,
    )

    # Run the folder watcher in the background.
    watcher_thread = threading.Thread(target=watcher.start, daemon=True)
    watcher_thread.start()

    print(f"Watching folder: {config.WATCHED_FOLDER}")
    print(f"Dashboard: http://{config.HOST}:{config.PORT}")

    # Start the web dashboard (this blocks until you stop the app).
    app = create_app(alert_store, detector)
    app.run(host=config.HOST, port=config.PORT, debug=True, use_reloader=False)


if __name__ == "__main__":
    main()
