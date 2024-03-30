pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t samahahaha/assignment_1:latest'
            }
        }

       
        stage('Upload to Docker Hub') {
            environment {
                DOCKER_CREDENTIALS_ID = 'samaha-docker'
            }
            steps {
                // Authenticate with Docker Hub
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    echo 'Login Successful'    
                    // Push the Docker image to Docker Hub
                    sh 'docker push samahahaha/assignment_1:latest'
                }
            }
        }
    }
    post {
        success {
            // Send email notification
            emailext(
                subject: "Pipeline Successful: Merge to Main",
                body: "The pipeline for merging to the master branch was successful.",
                to: "khan.afnan3128@gmail.com",
            )
        }
        failure {
            // Send email notification
            emailext(
                subject: "Pipeline Failure: Merge to Main",
                body: "The pipeline for merging to the master branch failed.",
                to: "khan.afnan3128@gmail.com",
            )
        }
    }
}    
