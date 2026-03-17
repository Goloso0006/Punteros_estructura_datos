from models.notification_node import NotificationNode


class NotificationLinkedList:
    """Manual singly linked list for notifications."""

    def __init__(self) -> None:
        # Head points to the first node in the list.
        self.head = None
        # Tail points to the last node in the list.
        self.tail = None
        # Total amount of stored notifications.
        self.length = 0

    def add_notification(self, message: str) -> None:
        """Creates a new node and links it at the end of the list."""
        new_node = NotificationNode(message)

        if self.head is None:
            # If the list is empty, head and tail point to the same node.
            self.head = new_node
            self.tail = new_node
        else:
            # The current tail points to the new node.
            self.tail.next = new_node
            # Tail moves to the new last node.
            self.tail = new_node

        self.length += 1

    def is_empty(self) -> bool:
        """Returns True when there are no nodes in the list."""
        return self.head is None

    @staticmethod
    def pointer_text(node) -> str:
        """Human-readable pointer text using Python memory id."""
        if node is None:
            return "None"
        return f"Node@{id(node)}"

    def display_in_console(self) -> None:
        """Traverses and prints each notification and its next pointer."""
        if self.is_empty():
            print("The notification list is empty.")
            return

        current_node = self.head
        position = 1

        while current_node is not None:
            print(f"Notification {position}: {current_node.message}")
            print(f"Next pointer: {self.pointer_text(current_node.next)}")
            print("-" * 45)
            current_node = current_node.next
            position += 1

    def build_view_text(self) -> str:
        """Returns a text block with all notifications for the UI."""
        if self.is_empty():
            return "No notifications stored."

        current_node = self.head
        position = 1
        result_text = ""

        while current_node is not None:
            result_text += f"{position}. {current_node.message}\n"
            result_text += f"   next -> {self.pointer_text(current_node.next)}\n\n"
            current_node = current_node.next
            position += 1

        return result_text.rstrip()
