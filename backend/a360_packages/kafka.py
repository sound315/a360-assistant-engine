# -*- coding: utf-8 -*-
PACKAGE_NAME        = "Kafka"
PACKAGE_ID          = "command-group:kafka"
PACKAGE_DESCRIPTION = "Publish and consume messages on Apache Kafka topics. 주요 액션: Commit offsets(Commits an offset for a topic partition...)、Connect(Connects to Kafka using the selected sec...)、Consume message(Polls messages from a Kafka topic.)、Disconnect(Terminates the Kafka session and ends th...)、Publish message(Publishes a message to a Kafka topic.) (총 5개)."

ACTIONS = [
    {"action": "Commit offsets", "data_item_name": "kafka#commitoffsets", "description": "Commits an offset for a topic partition within a consumer group."},
    {"action": "Connect", "data_item_name": "kafka#connect", "description": "Connects to Kafka using the selected security protocol."},
    {"action": "Consume message", "data_item_name": "kafka#consumemessage", "description": "Polls messages from a Kafka topic."},
    {"action": "Disconnect", "data_item_name": "kafka#disconnect", "description": "Terminates the Kafka session and ends the current session."},
    {"action": "Publish message", "data_item_name": "kafka#publishmessage", "description": "Publishes a message to a Kafka topic."},
]