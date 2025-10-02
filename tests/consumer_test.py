from kafka import KafkaConsumer
import json

TOPIC = "exposures"
BROKER = "localhost:29093"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[BROKER],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(f"Listening to topic '{TOPIC}' at {BROKER}... Ctrl+C to stop.")
for msg in consumer:
    print("Received:", msg.value)
