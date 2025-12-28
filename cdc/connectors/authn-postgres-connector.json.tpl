{
  "name": "authn-postgres-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "tasks.max": "1",
    "database.hostname": "${DB_HOST}",
    "database.port": "${DB_PORT}",
    "database.dbname": "${DB_NAME}",
    "database.user": "${DB_USER}",
    "database.password": "${DB_PASSWORD}",
    "plugin.name": "pgoutput",
    "table.include.list": "public.outbox",
    "snapshot.mode": "no_data",
    "topic.prefix": "authn",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false",
    "transforms": "outbox",
    "transforms.outbox.type": "io.debezium.transforms.outbox.EventRouter",
    "transforms.outbox.table.field.event.key": "aggregate_id",
    "transforms.outbox.route.by.field": "aggregate_type",
    "transforms.outbox.route.topic.replacement": "${routedByValue}",
    "transforms.outbox.table.delete.after.processing": "true"
  }
}
