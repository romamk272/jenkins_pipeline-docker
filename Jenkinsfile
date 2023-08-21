def groovyScript
def os
pipeline {
    agent any
    stages {
        stage('Build docker image') {
            steps {
                script {
                    // Replace 'your-docker-image' with the name of your Docker image
                    dockerImage = docker.build('login-dev')
                }
            }
        }
        stage('Conditional PR Stage') {
            echo "=============================================="
            echo "        PR stage"
            echo "=============================================="
            when {
                expression {
                    echo "Inside PR stage expression statement"
                    // Check if the commit message contains a specific keyword
                    def commitMessage = sh(script: 'git log -1 --pretty=%B', returnStdout: true).trim()
                    return commitMessage.contains("file")
                }
            }
            steps {
                // This stage will run only if the commit message contains the REQUIRED_KEYWORD
                echo "Running PR Stage"
                echo "=============================================="
                echo "        End of PR stage"
                echo "=============================================="
                // Add your PR stage steps here
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
