# Using python 3.12.7 slim image as the base image
FROM python:3.12.7-slim
# Defining working directory (within the container) and copy the requirements file. We will run the commands inside this new directory
WORKDIR /usr/src/myapp
# Copy requirements.txt  to the working directory
COPY requirements.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy all files in prediction-ui local host directory to /usr/src/myapp in Docker container
COPY . .
# Expose the port that our app runs in
EXPOSE 5000
# Environment Variables
ENV PREDICTOR_API=http://predictor-api-server:5000/diabetes_predictor/
#Add some meta data if necessary
LABEL diabetes.predictor.api="0.0.1-beta"
# Run our App
CMD ["python3","app.py"]
# We can also use an ENTRYPOINT and a CMD
# Run our App
#ENTRYPOINT ["python3"]
#CMD ["app.py"]
