# frantic-ticker
Sends predefined message to Kafka topic at random intervals.

## Run

### Locally
Set variables directly in environment or in `.env` file.

```bash
kafka.bootstrap_servers="broker:9092"
kafka.topic="tick"
kafka.message="tick!"
kafka.timeout=10  # in minutes

interval.min=60  # in seconds
interval.max=120  # in seconds
```

Run `main.py` file.

```bash
python main.py
```

### Using Docker
```bash
docker run \
    --network host \
    -e kafka.bootstrap_servers="broker:9092" \
    -e kafka.topic="tick" \
    -e kafka.message="tick!" \
    -e kafka.timeout=10 \
    -e interval.min=60 \
    -e interval.max=120 \
    norbiox/frantic_ticker
```
