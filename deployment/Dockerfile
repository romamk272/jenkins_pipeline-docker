FROM python:3.8.0-slim
# FROM ubuntu:18.04


RUN pip install --upgrade pip 
# RUN pip install curl ca-certificates git build-essential software-properties-common

WORKDIR /jenkins

# Build project
# RUN git clone https://github.com/romamk272/jenkins_pipeline-docker.git /jenkins/src

# WORKDIR /jenkins/src
COPY ./ ./jenkins/

COPY ./requirements.txt ./jenkins/requirements.txt
RUN pip install -r ./jenkins/requirements.txt

EXPOSE 5000
# ENTRYPOINT ["bash", "./start.bash"]
# CMD ["lambda.handler"]