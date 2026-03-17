class NotificationNode:
    """Represents one node in a singly linked list."""

    def __init__(self, message: str) -> None:
        # Stored notification message for this node.
        self.message = message
        # Pointer to the next node in memory.
        self.next = None
