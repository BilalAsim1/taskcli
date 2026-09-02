#!/usr/bin/env python3
"""taskcli - a tiny command-line task tracker."""
import json
import os
import sys

TASKS_FILE = os.environ.get("TASKS_FILE", "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(text):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "text": text, "done": False})
    save_tasks(tasks)
    print(f"Added task {len(tasks)}: {text}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['text']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: taskcli.py [add <text> | list]")
        return
    command = sys.argv[1]
    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
