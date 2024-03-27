# Domain Data

Task
 - Headline         : str
 - Priority         : int [0, 5] ; default = 3
 - Creation time    : datetime
 - Description      : str        ; optional
 - Deadline         : datetime   ; optional
 - Status           : enum


# Domain Actions

Task:
 - Input
 - Edit
 - Duplicate
 - Delete

Viewing:
 - Order
 - Filter

Persistence (*transparent to the user*):
 - Save
 - Load


# Modules

## User Interface
### Variants
 - Terminal User Interface
 - Ncurses User Interface?
 - Web-based User Interface?
 - Graphical User Interface?
### Responsibility
 - Show current state
 - Receive commands from the user

## Controller
### Responsibility
 - Execute Task domain actions

## Storage
### Variants
 - File Storage
 - Database Storage?
 - Cloud Storage?
### Responsibility
 - Persistence (Save and Load domain actions)

## Viewer
### Responsibility
 - Order and Filter domain actions


