#!/usr/bin/env python3
"""
Demo script showing Alice and Bob communicating through the A2A Gateway
"""

import requests
import time
import json

GATEWAY_URL = "http://localhost:8000"

def send_message(sender, receiver, content):
    """Send a message through the Gateway"""
    message = {
        "sender": sender,
        "receiver": receiver,
        "content": content
    }
    
    response = requests.post(f"{GATEWAY_URL}/messages", json=message)
    if response.status_code == 200:
        print(f"✅ {sender} sent: '{content}' to {receiver}")
        return True
    else:
        print(f"❌ Failed to send message: {response.text}")
        return False

def get_messages(receiver):
    """Get messages for a receiver from the Gateway"""
    response = requests.get(f"{GATEWAY_URL}/messages?receiver={receiver}")
    if response.status_code == 200:
        return response.json()["messages"]
    else:
        print(f"❌ Failed to get messages: {response.text}")
        return []

def check_gateway_health():
    """Check if the Gateway is running"""
    try:
        response = requests.get(f"{GATEWAY_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Gateway is healthy: {data}")
            return True
        else:
            print(f"❌ Gateway health check failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to Gateway: {e}")
        return False

def main():
    print("🤖 Alice and Bob Agent Communication Demo")
    print("=" * 50)
    
    # Check Gateway health
    if not check_gateway_health():
        print("Please start the A2A Gateway first: npm run start:gateway")
        return
    
    print("\n📨 Starting conversation...")
    
    # Alice sends a message to Bob
    send_message("Alice", "Bob", "Hello Bob! How are you today?")
    time.sleep(1)
    
    # Check Bob's messages
    bob_messages = get_messages("Bob")
    print(f"📬 Bob has {len(bob_messages)} message(s)")
    for msg in bob_messages:
        print(f"   From {msg['sender']}: {msg['content']}")
    
    # Bob replies to Alice
    send_message("Bob", "Alice", "Hi Alice! I'm doing great, thanks for asking!")
    time.sleep(1)
    
    # Check Alice's messages
    alice_messages = get_messages("Alice")
    print(f"📬 Alice has {len(alice_messages)} message(s)")
    for msg in alice_messages:
        print(f"   From {msg['sender']}: {msg['content']}")
    
    # Alice sends another message
    send_message("Alice", "Bob", "That's wonderful! Would you like to work on a project together?")
    time.sleep(1)
    
    # Bob replies
    send_message("Bob", "Alice", "Absolutely! I'd love to collaborate. What do you have in mind?")
    
    print("\n🎉 Demo completed! Alice and Bob successfully communicated through the A2A Gateway.")
    print("\n📊 Final message counts:")
    print(f"   Bob's messages: {len(get_messages('Bob'))}")
    print(f"   Alice's messages: {len(get_messages('Alice'))}")

if __name__ == "__main__":
    main()
