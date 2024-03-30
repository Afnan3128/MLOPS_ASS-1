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
                sh 'docker build -t A1 .'
            }
        }
        stage('Run Image') {
            steps {
                sh ''
            }
        }
        stage('Upload to Docker Hub') {
            environment {
                DOCKER_CREDENTIALS_ID = 'samahahaha'
            }
            steps {
                // Authenticate with Docker Hub
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, usernameVariable: 'samahahaha', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'

                    // Push the Docker image to Docker Hub
                    sh 'docker push samahahaha/A1:latest'
                }
        }
    }
}