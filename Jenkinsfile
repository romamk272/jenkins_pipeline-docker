def groovyScript
def os
<<<<<<< HEAD
// pipeline {
//     //agent { label 'CROSS-PLATFORM' }
//     agent {
//         node {
//             label 'CROSS-PLATFORM'
//         }
//     }
//     stages{
//         stage("Image build"){
//             def dockerfile = 'Dockerfile.test'
//             def customImage = docker.build("my-image:${env.BUILD_ID}",
//                                    "-f ${dockerfile} ./dockerfiles")
//         }
//         stage("Run container"){
//             docker.withServer(' tcp://localhost:2375', 'swarm-certs') {
//                 docker.image('jenkins-docker').withRun('-p 3306:3306') 
//             }
//         }
//     }
// }
=======

>>>>>>> e1d6257c024058f2e457056409f1d17b691f0707
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
            when {
                expression {
                    // Check if the commit message contains a specific keyword
                    def commitMessage = sh(script: 'git log -1 --pretty=%B', returnStdout: true).trim()
                    return commitMessage.contains("file")
                }
            }
            steps {
                // This stage will run only if the commit message contains the REQUIRED_KEYWORD
                echo "Running PR Stage"
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
