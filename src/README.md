# Notification System with OOP and Singly Linked List (Python)

This project implements a basic notification system using object-oriented programming.
Notifications are stored manually in a singly linked list.

## Project Structure

- `main.py`: Entry point. Reads messages from terminal, stores them, prints the linked list, and opens the GUI.
- `notification_system.py`: Service class that controls notification operations.
- `models/notification_node.py`: Node class with value and next pointer.
- `models/notification_linked_list.py`: Manual singly linked list implementation.
- `ui/notification_viewer.py`: Tkinter read-only interface for viewing notifications.

## How to Run

1. Open a terminal in `src`.
2. Run:

```bash
python main.py
```

3. Enter notification messages in terminal.
4. Press ENTER on an empty line to stop input.
5. The console prints the linked list traversal and pointer references.
6. The Tkinter window opens and displays only the stored notifications.
