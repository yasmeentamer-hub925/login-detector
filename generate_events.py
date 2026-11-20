import json
import random
from datetime import datetime, timedelta

random.seed(42)

users = ["alice", "bob", "carol", "dave", "erin"]
ips = ["192.0.2.10", "192.0.2.11", "192.0.2.12", "192.0.2.13"]
results = ["success"] * 19 + ["failure"]


def make_event(t, username, ip, result):
    return {
        "event_id": "",
        "timestamp": t.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "username": username,
        "source_ip": ip,
        "result": result,
        "host": "lab-server-01",
    }


def get_time(e):
    return e["timestamp"]


events = []

# Normal activity: 500 events, one per minute from 9:00 AM
start = datetime(2026, 11, 2, 9, 0, 0)
for i in range(500):
    t = start + timedelta(minutes=i)
    events.append(make_event(t, random.choice(users), random.choice(ips), random.choice(results)))

# PLANTED: brute force - 6 failures against carol from one IP in 6 minutes
attack_start = datetime(2026, 11, 2, 11, 0, 30)
for k in range(6):
    t = attack_start + timedelta(minutes=k)
    events.append(make_event(t, "carol", "198.51.100.23", "failure"))

# PLANTED: ordinary mistake - dave fails twice, then succeeds (should NOT be flagged)
# PLANTED: ordinary mistake - dave fails twice, then succeeds (should NOT be flagged)
mistake_start = datetime(2026, 11, 2, 14, 0, 30)
for k in range(2):
    t = mistake_start + timedelta(minutes=k)
    events.append(make_event(t, "dave", "192.0.2.12", "failure"))
t = mistake_start + timedelta(minutes=2)
events.append(make_event(t, "dave", "192.0.2.12", "success"))

# Put all events in time order, then number them
events.sort(key=get_time)
for n, e in enumerate(events, start=1):
    e["event_id"] = f"evt-{n:04d}"

with open("data/auth_events.jsonl", "w") as f:
    for e in events:
        f.write(json.dumps(e) + "\n")

print("Wrote", len(events), "events to data/auth_events.jsonl")