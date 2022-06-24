#!/usr/bin/python3

"""Defines a function canUnlockAll that returns true if
the boxes can open and false if otherwise
"""


def canUnlockAll(boxes):
    """Checks if boxes can be opened by keys in them
    """

    opened = [boxes[0]]
    keys = set()

    for box_number, box in enumerate(boxes):
        if box_number in keys and box not in opened:
            opened.append(box)
        for key in box:
            if key != 0:
                keys.add(key)

    for box in boxes:
        if box not in opened:
            return False

    return True                
