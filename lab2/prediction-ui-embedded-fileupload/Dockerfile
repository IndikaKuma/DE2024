# Using python 3.12.7 slim image as the base image
FROM python:3.12.7-slim
# Defining working directory and copy the requirements file. We will run the commands inside this new directory
WORKDIR /usr/src/myapp
# Copy requirements.txt  to the working directory
COPY requirements_prod.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements_prod.txt
# Copy all files in prediction-api local host directory to /usr/src/myapp in Docker container
COPY . .
ENV MODEL_NAME=model.h5
# Expose the port that our app runs in
EXPOSE 5000
# Run our App
CMD ["python3","app.py"]
# We can also use an ENTRYPOINT and a CMD
# Run our App
#ENTRYPOINT ["python3"]
#CMD ["app.py"]