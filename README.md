# Quickstart

The easiest way to understand the setup is by diving into it and interacting with it.

## Running Docker Compose

To run docker compose simply run the following command in the current folder:

```
docker-compose up -d
To view the their status run

```
> docker-compose ps
If you want to see the logs, you can run:

```
docker-compose logs -f -t --tail=10 <container_name>
```

To see the memory and CPU usage (which comes in handy to ensure docker has enough memory) use:

```
docker stats
```

## Openining Shell Into Container

To open up a bash shell inside the spark container run the docker-compose exec command:

```
# From spark server
docker-compose exec spark bash
# Install Python
pip install -r requirements.txt

# it's for checking your topics
python check_kafka_topic.py

# it's for create topic.
python create_topic_send_data.py

# This is for starting to data-generator for streaming-data.
#python dataframe_to_kafka.py -i ./input/iot_telemetry_data.csv -t test1 -b kafka:9092

# This is for starting the spark-streaming python scrips.
# read data
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5 --jars kafka-clients-2.2.0.jar --driver-class-path kafka-clients-2.2.0.jar spark_read_from_topic_and_show.py
#spark-submit --packages io.delta:delta-core_2.12:2.4.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.1 project_main.py

# From kafka server
docker-compose exec kafka1 bash
# docker-compose exec kafka2 bash

# it's for checking your topics
kafka-topics.sh --bootstrap-server 172.25.0.12:9092 --list 

# it's for create topic.
kafka-topics.sh --bootstrap-server kafka:9092 \
--create --topic test1 \
--replication-factor 1 \
--partitions 3

# it's for reading your data in your topic
kafka-console-consumer.sh --bootstrap-server 172.25.0.12:9092 --topic SAMPLE_TOPIC_NAME 

# it's for delete the topic.
kafka-topics.sh --bootstrap-server 172.25.0.12:9092 --delete --topic SAMPLE_TOPIC_NAME
