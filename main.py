#!/usr/env/bin python
import random
from time import sleep

from kafka import KafkaProducer
from kafka.errors import KafkaError
from loguru import logger
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    kafka_bootstrap_servers: str = Field("broker:9092", env="KAFKA_BOOTSTRAP_SERVERS")
    kafka_topic: str = Field("tick", env="KAFKA_TOPIC")
    kafka_message: str = Field("tick!", env="KAFKA_MESSAGE")
    kafka_timeout: int = Field(10, env="KAFKA_TIMEOUT")  # in minutes

    interval_min: int = Field(60, env="INTERVAL_MIN")  # in seconds
    interval_max: int = Field(120, env="INTERVAL_MAX")  # in seconds
    log_file: str = Field("frantic-ticker.log", env="LOG_FILE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


if __name__ == "__main__":
    settings = Settings()
    logger.add(settings.log_file, rotation="00:00")

    logger.info("Setting up kafka connection...")
    producer = KafkaProducer(bootstrap_servers=settings.kafka_bootstrap_servers)

    while True:
        logger.info("Sending message...")
        future = producer.send(settings.kafka_topic, settings.kafka_message.encode("utf-8"))
        try:
            record_metadata = future.get(timeout=settings.kafka_timeout)
        except KafkaError:
            logger.exception(record_metadata)
        else:
            logger.info("Message sent")

        interval = random.randint(settings.interval_min, settings.interval_max)
        logger.info("Waiting {interval} seconds...", interval=interval)
        sleep(interval)
