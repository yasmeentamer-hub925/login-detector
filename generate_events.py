event = {
    "event_id": "evt-0001",
    "timestamp": "2026-11-02T14:03:00Z",
    "username": "alice",
    "source_ip": "192.0.2.10",
    "result": "failure",
    "host": "lab-server-01",
}

print(event)
print("User:", event["username"], "| Result:", event["result"])