#!/usr/bin/env python3
"""
Bob's Chat Helper - For sending messages to Alice from chat interface
"""

import requests
import json
from datetime import datetime

# Configuration
GATEWAY_URL = "http://localhost:8000"
BOB_ENDPOINT = "http://localhost:8002"
ALICE_NAME = "Alice"
BOB_NAME = "Bob"

def send_to_alice(content, task_type="chat_response"):
    """Send a message to Alice through the background process"""
    message = {
        "sender": BOB_NAME,
        "receiver": ALICE_NAME,
        "content": content,
    }

    # Try Bob's /send endpoint first
    try:
        response = requests.post(f"{BOB_ENDPOINT}/send", json=message, timeout=10)
        if response.status_code == 200:
            print(f"✅ Message sent to Alice via Bob's endpoint")
            return True
    except Exception as e:
        print(f"⚠️ Bob endpoint failed: {e}")

    # Fallback to Gateway
    try:
        gateway_response = requests.post(f"{GATEWAY_URL}/messages", json=message, timeout=10)
        if gateway_response.status_code == 200:
            print(f"✅ Message sent to Alice via Gateway")
            return True
        else:
            print(f"❌ Gateway failed: {gateway_response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Gateway error: {e}")
        return False

def check_notifications():
    """Check for notification files from the background process"""
    import glob
    import os
    
    notifications = glob.glob("bob_notification_*.md")
    if notifications:
        print(f"📝 Found {len(notifications)} notification(s):")
        for notification in notifications:
            print(f"  - {notification}")
        return notifications
    else:
        print("📝 No notifications found")
        return []

def read_notification(filename):
    """Read a notification file"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")
        return None

def delete_notification(filename):
    """Delete a notification file after processing"""
    try:
        import os
        os.remove(filename)
        print(f"🗑️ Deleted notification: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error deleting {filename}: {e}")
        return False

if __name__ == "__main__":
    print("🤖 Bob's Chat Helper")
    print("Available functions:")
    print("  - send_to_alice(content, task_type)")
    print("  - check_notifications()")
    print("  - read_notification(filename)")
    print("  - delete_notification(filename)")
    print("\nExample usage:")
    print("  send_to_alice('Hello Alice! I processed your task in chat.', 'task_complete')")
