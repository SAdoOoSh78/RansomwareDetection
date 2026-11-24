"""
Fake-ransomware test script  (Owner: Fady)

Simulates a ransomware-style burst: it quickly creates many files in the
watched folder and renames some of them to a "bad" extension. This is ONLY a
test tool - it does not touch anything outside the watched folder.

Run the app first (python app.py), then in a second terminal:
    python tools/fake_ransomware.py
"""

import os
import sys
import time

# Make the project root importable so we can read config.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config  # noqa: E402

NUM_FILES = 25
BAD_EXT = ".encrypted"


def main():
    folder = config.WATCHED_FOLDER
    os.makedirs(folder, exist_ok=True)
    print(f"Creating {NUM_FILES} files in {folder} ...")

    created = []
    for i in range(NUM_FILES):
        path = os.path.join(folder, f"test_file_{i}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write("important data\n")
        created.append(path)
        time.sleep(0.05)  # fast, but still a burst

    print("Renaming files to a bad extension ...")
    for path in created:
        try:
            os.rename(path, path + BAD_EXT)
        except OSError:
            pass
        time.sleep(0.05)

    print("Done. Check the dashboard - an alert should have appeared.")
    print("Clean up the test files by deleting the 'watched' folder when finished.")


if __name__ == "__main__":
    main()
