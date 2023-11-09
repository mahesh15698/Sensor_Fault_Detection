# Sensor-Fault-Detection

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
# confluent-kafka-python


This repo help us to know how to publish and consume data to and from kafka confluent in json format.

Step 1: Create a conda environment
```
conda --version
```

Step2: Create  a conda environment
```
conda create -p venv python==3.8 -y
```

Step3:
```
conda activate venv/
```
Step4:
```
pip install -r requirements.txt
```

Make account on Kafka by using following Link
```
https://confluent.cloud/login
```
Create cluster envrinment and create one topic
Cluster Environment Variable in Confluent Kafka
```
API_KEY
API_SECRET_KEY
BOOTSTRAP_SERVER
```
Schema related Environment Variable
```
SCHEMA_REGISTRY_API_KEY
SCHEMA_REGISTRY_API_SECRET
ENDPOINT_SCHEMA_URL
```
Data base related Environment Variable
Download MongoDB compass to local and Create Cluster on MongoDB atlas
```
MONGO_DB_URL
```

## Update the credential in .env file and run below command to run your application in docker container


Create .env file in root dir of your project if it is not available
paste the below content and update the credentials
```
API_KEY=asgdakhlsa
API_SECRET_KEY=dsdfsdf
BOOTSTRAP_SERVER=sdfasd
SCHEMA_REGISTRY_API_KEY=sdfsaf
SCHEMA_REGISTRY_API_SECRET=sdfasdf
ENDPOINT_SCHEMA_URL=sdafasf
MONGO_DB_URL=sdfasdfas
```

Build docker image
```
docker build -t data-pipeline:lts .
```

For linux or mac
Run docker image
```
docker run -it -v $(pwd)/logs:/logs  --env-file=$(pwd)/.env data-pipeline:lts
```

## What is -e . in the requirements.txt file?
Answer:
```
In Python, the -e option is typically used with the pip command, which is the package manager for Python, not as part of a Python library. The -e option is used to install a package in "editable" mode, which means that the package is installed in a way that allows you to make changes to the source code of the package and have those changes immediately take effect without needing to reinstall the package.

When you use pip install -e . in a directory containing a Python package, it tells pip to install the package in editable mode from the current directory. This can be useful during development when you are working on a Python package and want to see the effects of your code changes without the need to reinstall the package each time you make a modification.

Here's an example of how you might use it:
Navigate to the root directory of your Python package.
Open a terminal or command prompt.
```