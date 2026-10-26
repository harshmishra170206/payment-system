pipeline {
    agent any
    environment {
        IMAGE = "harshmishra1702/payment-system"
        TAG = "${env.BRANCH_NAME}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker build -t ${IMAGE}:${TAG} ."
                    } else {
                        bat "docker build -t %IMAGE%:%TAG% ."
                    }
                }
            }
        }
        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'U',
                                                  passwordVariable: 'P')]) {
                    script {
                        if (isUnix()) {
                            sh 'echo $P | docker login -u $U --password-stdin'
                            sh "docker push ${IMAGE}:${TAG}"
                        } else {
                            bat 'echo %P%| docker login -u %U% --password-stdin'
                            bat "docker push %IMAGE%:%TAG%"
                        }
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh "kubectl apply -f k8s/deployment-${TAG}.yaml"
                    } else {
                        bat "kubectl apply -f k8s/deployment-%TAG%.yaml"
                    }
                }
            }
        }
    }
}
