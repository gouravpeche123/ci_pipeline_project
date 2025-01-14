pipeline {
    agent any
    stages {
        stage("Checkout Code") {
            steps {
                git url:'https://github.com/gouravpeche123/ci_pipeline_project.git',branch:'main'
            }
        }
        stage("Cleanup Activity"){
            steps{
                sh 'docker rm -f $(docker ps -aq)'
            }
        }
        stage("Build Docker Image") {
            steps {
                sh 'docker build -t myimage .'
            }
        }
        stage("Create a Container") {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }
    }

}