from models.notification_linked_list import NotificationLinkedList


class NotificationSystem:
    """Main service class that manages the notification linked list."""

    def __init__(self) -> None:
        self.notifications = NotificationLinkedList()

    def add_notification(self, message: str) -> None:
        """Adds one notification into the linked list."""
        clean_message = message.strip()

        if clean_message == "":
            # Empty messages are ignored to keep the list valid.
            return

        self.notifications.add_notification(clean_message)

    def show_notifications_console(self) -> None:
        """Displays notifications in the terminal."""
        self.notifications.display_in_console()

    def get_notifications_for_ui(self) -> str:
        """Returns formatted text for a read-only GUI."""
        return self.notifications.build_view_text()
