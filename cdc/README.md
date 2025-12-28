# CDC (Change Data Capture) Setup

This directory contains the infrastructure for the Change Data Capture (CDC)
environment. It serves as the event streaming backbone for the entire system.

## Directory Structure

-   **`docker/`**: Contains Docker Compose files defining the infrastructure.
-   **`connectors/`**: Contains configuration templates (JSON) for Debezium connectors.
-   **`images/`**: Contains Dockerfiles for building custom Debezium Connect images.

## Components

The `docker/docker-compose.yml` file orchestrates the following services:

-   **Zookeeper**: Manages the Kafka cluster state.
-   **Kafka (broker1, broker2, broker3)**: A distributed event streaming platform
    consisting of three brokers.
-   **Debezium Connect**: A Kafka Connect service running on port 8083 to execute
    Debezium connectors.

> **Note**: This setup includes only the messaging and CDC infrastructure. Actual
> database services (e.g., `accountdb`) and application services are expected to be
> defined in separate Docker Compose files.

## How to Run

Run the following command from this `cdc` directory to start the infrastructure:

```bash
docker compose -f docker/docker-compose.yml up -d
```

To stop and remove the services:

```bash
docker compose -f docker/docker-compose.yml down --volumes
```

## Common Commands

The following commands are examples of how to interact with the running system.

---

### 1. Create a Kafka Topic

Since `KAFKA_AUTO_CREATE_TOPICS_ENABLE` is set to `false`, you must create topics
manually before they can be used.

```bash
docker exec broker1 kafka-topics --bootstrap-server broker1:19092 --create --topic accounts --partitions 3 --replication-factor 3
```

### 2. Register the Debezium Connector

This command tells Debezium to start monitoring the `outbox` table in the `accountdb`
database.

```bash
export DB_HOST=accountdb
export DB_PORT=5432
export DB_NAME=accountdb
export DB_USER=postgres
export DB_PASSWORD=postgres

envsubst '$DB_HOST $DB_PORT $DB_NAME $DB_USER $DB_PASSWORD' < connectors/account-postgres-connector.json.tpl \
| curl -X POST http://localhost:8083/connectors/ \
    -H "Content-Type: application/json" \
    --data @-
```

### 3. Produce an Event

To trigger the CDC process, insert a record into the `outbox` table.

```sh
docker exec -i accountdb psql -U postgres -d accountdb <<EOF
INSERT INTO public.outbox (id, aggregate_id, aggregate_type, payload) VALUES ('123e4567-e89b-12d3-a456-426614174000', '123e4567-e89b-12d3-a456-426614174000', 'accounts', '{"message": "hello world"}');
EOF
```

### 4. Consume Events from a Topic

Listen to the `accounts` topic to see the events published by Debezium.

```bash
docker exec -it broker1 kafka-console-consumer --bootstrap-server broker1:19092 --topic accounts --from-beginning
```

### 5. Manage the Connector

-   **Check connector status:**
    ```bash
    curl http://localhost:8083/connectors/account-postgres-connector/status
    ```
-   **Delete the connector:**
    ```bash
    curl -X DELETE http://localhost:8083/connectors/account-postgres-connector
    ```
