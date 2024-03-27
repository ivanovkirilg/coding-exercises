# Task-Tracker

Implement an application for personal task-tracking, a.k.a. to-do list.
Include persistent storage (files/database) and a GUI.

It is recommended to first distribute the requirements among modules,
and to implement those using TDD.


## Requirements

1. The user shall be able to input new tasks.
1. A task shall have:
   - A headline,
   - A priority level (with a default),
   - A creation timestamp (date and time),
   - Optionally, a description,
   - Optionally, a deadline (date and time),
   - A status (to-do, done, cancelled).
1. The tasks shall be stored persistently. (Upon closing and reopening
   the application, previously input tasks are available.)
1. The user shall be able to list tasks:
   - Ordered by priority,
   - Ordered by creation time,
   - Ordered by deadline,
   - Filtered by status,
   - Filtered by contained text (in the headline and/or the description).
1. The user shall be able to edit a task's properties (except creation time).
1. The user shall be able to duplicate a task.
1. The user shall be able to delete tasks.

