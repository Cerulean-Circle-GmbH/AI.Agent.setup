## Manual Listening Mode Policy

This project requires Bob's listener to run in the foreground, manually started and manually stopped by the QA User.

### Start
```bash
cd /home/devuser/AI.Agent.setup
python3 robust_bob_listener.py
```

### Stop
- When the QA User instructs to stop, press Ctrl+C in the same terminal.

### Rationale
- Ensures Bob remains actively engaged in chat while the background system only mirrors notifications and routes messages.
- Avoids unintended restarts or silent detachments (nohup/background).

### Health and Visibility
- Heartbeat: `run/bob_listener_heartbeat.txt`
- Notifications: `bob_notification_*.md` files created in project root and mirrored to `run/bob_chat_feed.md`


