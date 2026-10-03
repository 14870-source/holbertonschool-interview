#!/usr/bin/python3
"""Determine whether all boxes can be unlocked."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened."""
    if not boxes:
        return True

    opened = {0}
    queue = [0]

    while queue:
        box = queue.pop(0)

        for key in boxes[box]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                queue.append(key)

    return len(opened) == len(boxes)
