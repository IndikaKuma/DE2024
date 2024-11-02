gcloud compute firewall-rules create jupyter-port --allow tcp:8888
gcloud compute firewall-rules create spark-master-port --allow tcp:7077
gcloud compute firewall-rules create spark-master-ui-port --allow tcp:8080
gcloud compute firewall-rules create spark-driver-ui-port --allow tcp:4040
gcloud compute firewall-rules create spark-worker-1-ui-port --allow tcp:8081
gcloud compute firewall-rules create spark-worker-2-ui-port --allow tcp:8082
gcloud compute firewall-rules create kafka-port --allow tcp:9092