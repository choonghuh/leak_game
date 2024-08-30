pipeline {
    agent {
        node {
            customWorkspace '${WORKSPACE}/${BUILD_NUMBER}'
        }
    }
    
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World!!!'
                echo 'More change, trying to trigger a jenkins build'
            }
        }

    }
}
