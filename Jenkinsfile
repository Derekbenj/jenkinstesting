pipeline {
    agent {
        // docker {
        // image 'docker:dind'
        // args '-v /var/run/docker.sock:/var/run/docker.sock -p 2375:2375 --privileged' 
        // }
        node {
            label 'docker-agent-alpine'
        }
      }

    triggers {
        pollSCM '* * * * *'
    }   
    stages {
        stage('Build Image') {
            steps {
                script {
                    echo "Building image.."
                    sh "pip install docker-compose"
                    sh "docker compose build"
                }
            }
        }
        stage('Delete Old Docker Image') {
            steps {
                script {
                    echo "Deleting old image.."
                    def imageName = 'git_jenkins-python_project'
                    sh "docker rmi -f ${image_name}"
                }
            }
        }
        stage('Push Image To Host Daemon Local Registry') {
            steps {
                script {
                    echo "Pushing image.."

                    // get a list of built images
                    def images = sh(returnStdout: true, script: 'docker image ls -q').trim().split("\n")

                    // push each image to the registry
                    images.each { image ->
                        docker.withRegistry('http://localhost:5000') {
                            docker.image(image).push()
                        }
                    }
                }
            }
        }
    }
}