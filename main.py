#!/usr/env/bin python
import random
from time import sleep

from kafka import KafkaProducer
from kafka.errors import KafkaError
from loguru import logger
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    kafka_bootstrap_servers: str = Field(..., env="kafka.bootstrap_servers")
    kafka_topic: str = Field(..., env="kafka.topic")
    kafka_message: str = Field(..., env="kafka.message")
    kafka_timeout: int = Field(..., env="kafka.timeout")

    interval_min: int = Field(..., env="interval.min")
    interval_max: int = Field(..., env="interval.max")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


if __name__ == "__main__":
    settings = Settings()
    producer = KafkaProducer(bootstrap_servers=settings.kafka_bootstrap_servers)

    while True:
        logger.debug("Sending message...")
        future = producer.send(settings.kafka_topic, settings.kafka_message.encode("utf-8"))
        try:
            record_metadata = future.get(timeout=settings.kafka_timeout)
        except KafkaError:
            logger.exception(record_metadata)
        else:
            logger.debug("Message sent")

        interval = random.randint(settings.interval_min, settings.interval_max)
        logger.debug("Waiting {interval} seconds...", interval=interval)
        sleep(interval)
