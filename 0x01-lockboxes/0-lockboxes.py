#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked
    Args:
    boxes: A list of lists; inner lists contain keys to other boxes (lists)
    Returns:
    bool: True if all boxes can be unlocked, False otherwise
    """
    if not boxes:
        return False

    unlocked = [0]

    for i in unlocked:
        for key in boxes[i]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    return len(unlocked) == len(boxes)
