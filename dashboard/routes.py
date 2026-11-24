"""
Web dashboard  (Owner: Oche)

A small Flask app that shows:
  - the current status (how many changes in the window, the threshold)
  - the alert history
  - recent file events

The page refreshes itself every few seconds, and also pulls live data from
the /api/status endpoint.
"""

from flask import Flask, render_template, jsonify


def create_app(alert_store, detector):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template(
            "index.html",
            status=detector.status(),
            alerts=alert_store.all(),
            recent=list(detector.recent),
        )

    # Live data for the auto-refresh (used by JavaScript on the page).
    @app.route("/api/status")
    def api_status():
        return jsonify(
            {
                "status": detector.status(),
                "alerts": alert_store.all()[:20],
                "recent": [
                    {"action": e.action, "name": e.name}
                    for e in list(detector.recent)[:20]
                ],
            }
        )

    # TODO (Oche, Sprint 2): add a /settings page to change folder + threshold.

    return app
