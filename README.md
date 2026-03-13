# Autonomous Satellite Operations (Agentic AI)

## Mission Overview
A prototype multi-agent AI ground station designed to autonomously process satellite telemetry, detect anomalies, and execute safety-validated resolution protocols in simulated Disconnected, Intermittent, and Low-Bandwidth (DIL) environments.

This architecture demonstrates the integration of **Agentic AI** with modern, distributed messaging systems to solve complex aerospace challenges without requiring human-in-the-loop intervention.

## System Architecture
This system utilizes an event-driven microservices architecture:
1. **Telemetry Producer (`mock_telemetry.py`):** Simulates a satellite in orbit continuously broadcasting component health data.
2. **Message Broker (Apache Kafka / KRaft):** A highly-available, containerized message queue that ingests the telemetry stream and decouples the satellite from the ground station.
3. **AI Ground Station (`agent_consumer.py`):** Listens to the Kafka broker for telemetry anomalies. 
4. **The "Brain" (`langgraph_logic.py`):** A LangGraph state machine utilizing LLM agent routing. 
   - **Controller Agent:** Analyzes the anomaly.
   - **RAG Agent:** Queries simulated technical manuals to find the correct protocol.
   - **Validator Agent:** Performs an engineering safety check before approving the maneuver.

## Tech Stack
* **Languages/Frameworks:** Python, LangGraph, LangChain
* **Messaging:** Apache Kafka (KRaft mode, Zookeeper-less)
* **Infrastructure:** Docker, Docker-Compose
* **Paradigms:** Multi-Agent Systems, RAG (Retrieval-Augmented Generation), Event-Driven Architecture

## Quickstart Guide
To run this simulation locally, you need Docker Desktop and Python 3.10+ installed.

**1. Spin up the Infrastructure:**
```bash
docker-compose up -d
