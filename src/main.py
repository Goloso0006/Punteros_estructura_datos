from notification_system import NotificationSystem
from ui.notification_viewer import NotificationViewer


def collect_notifications(notification_system: NotificationSystem) -> None:
    """Collects notifications from terminal input and stores them in the linked list."""
    print("Type one notification message per line.")
    print("Press ENTER on an empty line to finish.\n")

    while True:
        user_message = input("Notification message: ").strip()

        if user_message == "":
            break

        notification_system.add_notification(user_message)


def main() -> None:
    notification_system = NotificationSystem()

    collect_notifications(notification_system)

    print("\nLinked list content (node + pointer):")
    notification_system.show_notifications_console()

    # Open a read-only Tkinter interface to display stored notifications.
    viewer = NotificationViewer(notification_system)
    viewer.run()


if __name__ == "__main__":
    main()
