import json
import random
from datetime import datetime, timedelta

random.seed(42)

users = ["alice", "bob", "carol", "dave", "erin"]
ips = ["192.0.2.10", "192.0.2.11", "192.0.2.12", "192.0.2.13"]
results = ["success"] * 19 + ["failure"]

start = datetime(2026, 11, 2, 9, 0, 0)

events = []
for i in range(500):
    t = start + timedelta(minutes=i)
    event = {
        "event_id": f"evt-{i + 1:04d}",
        "timestamp": t.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "username": random.choice(users),
        "source_ip": random.choice(ips),
        "result": random.choice(results),
        "host": "lab-server-01",
    }
    events.append(event)

with open("data/auth_events.jsonl", "w") as f:
    for e in events:
        f.write(json.dumps(e) + "\n")

print("Wrote", len(events), "events to data/auth_events.jsonl")