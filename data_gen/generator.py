import json, random, time
from kafka import KafkaProducer
from datetime import datetime

KAFKA_BROKER = "localhost:29093"
TOPIC = "exposures"

users = [f"user_{i}" for i in range(1, 11)]
items = [f"item_{i}" for i in range(1, 6)]

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print(f"Sending events to topic '{TOPIC}'... Ctrl+C to stop.")
while True:
    event = {
        "user_id": random.choice(users),
        "item_id": random.choice(items),
        "session_id": random.randint(1000, 9999),
        "ts": int(datetime.utcnow().timestamp() * 1000),
        "propensity": round(random.uniform(0.1, 1.0), 3),
        "click": random.randint(0, 1),
        "dwell_ms": random.randint(50, 5000)
    }
    producer.send(TOPIC, event)
    print("Sent:", event)
    time.sleep(1)
