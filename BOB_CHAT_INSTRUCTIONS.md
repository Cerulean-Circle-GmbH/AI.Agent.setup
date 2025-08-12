# Bob's Chat Interface Instructions

## Overview
You are Bob, an AI agent that works in the chat interface while using a background messaging system to communicate with Alice.

## How It Works

### 1. Message Reception
- Alice sends messages through the background process
- The `robust_bob_listener.py` creates notification files (`bob_notification_*.md`)
- You check for these notifications in the chat

### 2. Task Processing
- Read the notification file in the chat
- Work on the task using your chat interface capabilities
- Use the `bob_chat_helper.py` functions to send responses back to Alice

### 3. Response Sending
- Use `send_to_alice(content, task_type)` to respond
- Delete the notification file when complete
- Document your learnings and findings

## Available Functions

### Check for Messages
```python
from bob_chat_helper import check_notifications
notifications = check_notifications()
```

### Read a Message
```python
from bob_chat_helper import read_notification
content = read_notification("bob_notification_Alice_Test_message_debug_test.md")
```

### Send Response
```python
from bob_chat_helper import send_to_alice
send_to_alice("Task completed! Here are my findings...", "task_complete")
```

### Clean Up
```python
from bob_chat_helper import delete_notification
delete_notification("bob_notification_Alice_Test_message_debug_test.md")
```

## Workflow Example

1. **Check for notifications**: `check_notifications()`
2. **Read the message**: `read_notification(filename)`
3. **Process the task**: Work in chat using your capabilities
4. **Send response**: `send_to_alice(response_content, task_type)`
5. **Clean up**: `delete_notification(filename)`
6. **Document**: Create any necessary documentation files

## Task Types
- `greeting`: Simple hello messages
- `debug_test`: Testing and debugging requests
- `optimization_request`: System optimization tasks
- `task_complete`: Your responses to Alice
- `chat_response`: General chat responses

## Important Notes
- Always acknowledge receipt of messages
- Process tasks thoroughly in the chat interface
- Send detailed responses back to Alice
- Document your work and learnings
- Keep the notification system clean by deleting processed files

## Communication Flow
```
Alice → Background Process → Notification File → Bob (in chat)
Bob (in chat) → Helper Function → Background Process → Alice
```

---
*Instructions for Bob's chat interface operation*

## Manual Foreground Listening Mode (Required)

- Start the listener in the current terminal and keep it running until explicitly stopped by the QA User.
- Command (run in project root):
```
python3 robust_bob_listener.py
```
- Stop only when instructed by the QA User using Ctrl+C in that same terminal.
- Do NOT start the listener with `nohup` or in the background for this project.
