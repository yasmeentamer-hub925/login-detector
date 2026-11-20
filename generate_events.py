import json

events = [
    {
        "event_id": "evt-0001",
        "timestamp": "2026-11-02T14:03:00Z",
        "username": "alice",
        "source_ip": "192.0.2.10",
        "result": "failure",
        "host": "lab-server-01",
    },
    {
            "event_id": "evt-0002",
    "timestamp": "2026-11-02T14:05:00Z",
    "username": "bob",
    "source_ip": "192.0.2.55",
    "result": "success",
    "host": "lab-server-01",
    }
]

with open("data/auth_events.jsonl", "w") as f:
    for e in events:
        f.write(json.dumps(e) + "\n")

print("Wrote", len(events), "events to data/auth_events.jsonl")