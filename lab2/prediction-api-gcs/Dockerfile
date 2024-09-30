# Using python 3.10 slim image as the base image
FROM python:3.10.7-slim
# Defining working directory and copy the requirements file. We will run the commands inside this new directory
WORKDIR /usr/src/myapp
# Copy requirements.txt  to the working directory
COPY requirements.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy all files in prediction-api local host directory to /usr/src/myapp in Docker container
COPY . .
# Expose the port that our app runs in
EXPOSE 5000
# Enviroment Variables
ENV PROJECT_ID=your-gcp-project-id
ENV MODEL_REPO=your-model-repos-gcs-bucket
ENV MODEL_NAME=model.h5
# Run our App
CMD ["python3","app.py"]
# We can also use an ENTRYPOINT and a CMD
# Run our App
#ENTRYPOINT ["python3"]
#CMD ["app.py"]