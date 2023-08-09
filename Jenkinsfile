def groovyScript
def os

pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Replace 'your-docker-image' with the name of your Docker image
                    dockerImage = docker.build('login-dev')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Remove the container if it's already running
                    docker.image('login-dev').withRun('-p 8081:8081 --name jenkins-container') {
                    }
                } 
            }
        }         
    }
}
