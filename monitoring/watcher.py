"""
File-system monitoring  (Owner: Fady)

Watches a folder and reports every file change (create / modify / delete /
rename) by calling the `on_event` function it was given.

Temp and system files are ignored here so the detector does not get noise.

Uses the `watchdog` library:  pip install watchdog
"""

import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import config


class FileEvent:
    """A simple description of one file change."""

    def __init__(self, action, path):
        self.action = action          # "created" | "modified" | "deleted" | "moved"
        self.path = path              # full path of the file
        self.name = os.path.basename(path)
        self.time = time.time()

    def __repr__(self):
        return f"<FileEvent {self.action} {self.name}>"


def _should_ignore(path):
    """Return True for temp / system files we do not care about."""
    name = os.path.basename(path)
    if name in config.IGNORE_NAMES:
        return True
    for suffix in config.IGNORE_SUFFIXES:
        if name.endswith(suffix):
            return True
    return False


class _Handler(FileSystemEventHandler):
    """Receives raw watchdog events and forwards the useful ones."""

    def __init__(self, on_event):
        self.on_event = on_event

    def _forward(self, action, path):
        if _should_ignore(path):
            return
        self.on_event(FileEvent(action, path))

    def on_created(self, event):
        if not event.is_directory:
            self._forward("created", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self._forward("modified", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self._forward("deleted", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            # A rename shows the new name, which is where bad extensions appear.
            self._forward("moved", event.dest_path)


class FolderWatcher:
    """Starts watching `folder` and calls `on_event(FileEvent)` for each change."""

    def __init__(self, folder, on_event):
        self.folder = folder
        self.handler = _Handler(on_event)
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.handler, self.folder, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()
