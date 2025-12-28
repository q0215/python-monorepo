FROM quay.io/debezium/connect-base:3.4

ARG DEBEZIUM_VERSION=3.3.2.Final

USER root

ADD https://repo1.maven.org/maven2/io/debezium/debezium-core/${DEBEZIUM_VERSION}/debezium-core-${DEBEZIUM_VERSION}.jar /kafka/connect/debezium-core/
RUN chmod +r /kafka/connect/debezium-core/debezium-core-${DEBEZIUM_VERSION}.jar

ADD https://repo1.maven.org/maven2/io/debezium/debezium-connector-postgres/${DEBEZIUM_VERSION}/debezium-connector-postgres-${DEBEZIUM_VERSION}-plugin.tar.gz /tmp/
RUN tar -xzf /tmp/debezium-connector-postgres-${DEBEZIUM_VERSION}-plugin.tar.gz -C /kafka/connect/
RUN rm /tmp/debezium-connector-postgres-${DEBEZIUM_VERSION}-plugin.tar.gz

USER kafka
