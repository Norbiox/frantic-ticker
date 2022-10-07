# frantic-ticker
Sends predefined message to Kafka topic at random intervals.

## Config
Set variables directly in environment or in `.env` file.

```bash
kafka.bootstrap_servers="broker:9092"
kafka.topic="tick"
kafka.message="tick!"
kafka.timeout=10  # in minutes

interval.min=60  # in seconds
interval.max=120  # in seconds
```

## Usage
Run `main.py` file.

```bash
python main.py
```
