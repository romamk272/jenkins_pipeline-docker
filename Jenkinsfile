def groovyScript
def os

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
        // stage('Check if Container is Running') {
        //     steps {
        //         script {
        //             try {
        //                 // Check if the container is running
        //                 docker.image('todo-dev').inside('-p 8081:8081 --name my-container') {
        //                     // Do nothing, just check the container status
        //                 }
        //             } catch (Exception e) {
        //                 // If the container is not running, it will throw an exception
        //                 // Handle the exception here, or do nothing if you want to proceed anyway
        //             }
        //         }
        //     }
        // }
 
        // stage('Stop Existing Container') {
        //     steps {
        //         script {
        //             // Stop the container if it's already running
        //             try {
        //                 sh 'docker stop my-container'
        //             } catch (Exception e) {
        //                 // If the container is not running, it will throw an exception
        //                 // Handle the exception here, or do nothing if you want to proceed anyway
        //             }
        //         }
        //     }
        // }
    
        stage('Run Docker Container') {
            steps {
                script {
                    // Remove the container if it's already running
                    docker.image('todo-dev').withRun('-p 8081:8081 --name jenkins-container') {
                        // The above line will run the container and map port 8081 inside the container to port 8081 on the host machine
                        // Add any other configuration or environment variables if required for your application
                    }
                } 
            }
        }         
    }
}
