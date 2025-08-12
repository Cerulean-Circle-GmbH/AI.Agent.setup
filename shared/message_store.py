from typing import List, Dict

MESSAGES: List[Dict] = []

def add_message(msg: Dict):
    MESSAGES.append(msg)

def get_messages(receiver: str) -> List[Dict]:
    return [m for m in MESSAGES if m["receiver"] == receiver]



