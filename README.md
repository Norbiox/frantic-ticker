# frantic-ticker
Sends predefined message to Kafka topic at random intervals.

## Run

### Locally
Set variables directly in environment or in `.env` file.

```bash
KAFKA_BOOTSTRAP_SERVERS="broker:9092"
KAFKA_TOPIC="tick"
KAFKA_MESSAGE="tick!"
KAFKA_TIMEOUT=10  # in minutes

INTERVAL_MIN=60  # in seconds
INTERVAL_MAX=120  # in seconds
```

Run `main.py` file.

```bash
python main.py
```

### Using Docker
```bash
docker run \
    --network host \
    -e KAFKA_BOOTSTRAP_SERVERS="broker:9092" \
    -e KAFKA_TOPIC="tick" \
    -e KAFKA_MESSAGE="tick!" \
    -e KAFKA_TIMEOUT=10 \
    -e INTERVAL_MIN=5 \
    -e INTERVAL_MAX=20 \
    norbiox/frantic_ticker
```
