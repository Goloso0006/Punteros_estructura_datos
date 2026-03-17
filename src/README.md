# Notification System with OOP and Singly Linked List (Python)

This project implements a basic notification system using object-oriented programming.
Notifications are stored manually in a singly linked list.

## Project Structure

- `main.py`: Entry point. Launches the Tkinter interface.
- `notification_system.py`: Service class that controls notification operations.
- `models/notification_node.py`: Node class with value and next pointer.
- `models/notification_linked_list.py`: Manual singly linked list implementation.
- `ui/notification_viewer.py`: Basic Tkinter interface for adding and viewing notifications.

## How to Run

1. Open a terminal in `src`.
2. Run:

```bash
python main.py
```

On Windows, `main.py` relaunches itself with `pythonw.exe` automatically, so the app runs without console interaction.

3. In the Tkinter window, write a notification in the input box.
4. Click **Add** (or press ENTER) to store it in the singly linked list.
5. The viewer updates and shows each node with its `next` pointer reference.
