from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="172.25.0.12:9092"
)
producer = KafkaProducer(bootstrap_servers='172.25.0.13:9092')

existing_topics = admin_client.list_topics()
print("Existing topics:", existing_topics)

