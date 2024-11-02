FROM bitnami/python:3.11 as build

FROM bitnami/spark:3.5.0

COPY --from=build /opt/bitnami/python/ /opt/bitnami/python/

USER root

RUN  apt-get update && apt-get install -y python3-wheel
# Copy requirements.txt  to the working directory
COPY requirements.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt

# Update the guava library needed by the gcs connector
RUN mv /opt/bitnami/spark/jars/guava-14.0.1.jar /opt/bitnami/spark/jars/guava-14.0.1.jar.bk
COPY *.jar /opt/bitnami/spark/jars/       
