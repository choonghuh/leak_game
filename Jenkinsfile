pipeline {
    agent {
        node {
            label ''
            customWorkspace "workspace/pipe1/${BUILD_NUMBER}"
        }
    }
    
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World!!!'
                echo 'More change, trying to trigger a jenkins build'
            }
        }
        stage('Git Checkout') {
            steps {
                git 'https://github.com/choonghuh/leak_game'
            }
        }
    }
}
