pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World!!!'
                echo 'More change, trying to trigger a jenkins build'
            }
        }
        stage('Git') {
            steps {
                git 'https://github.com/choonghuh/leak_game'
            }
        }
    }
}
