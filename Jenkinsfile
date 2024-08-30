pipeline {
    agent {
        node {
            label ''
            customWorkspace "workspace/pipe1/${BUILD_NUMBER}"
        }
    }
    
    parameters {
        booleanParam(name: 'RUN_TEST_ADD', defaultValue: false, description: 'Run test_add')
        booleanParam(name: 'RUN_TEST_SUBTRACT', defaultValue: false, description: 'Run test_subtract')
        booleanParam(name: 'RUN_TEST_MULTIPLY', defaultValue: false, description: 'Run test_multiply')
    }
    
    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/choonghuh/leak_game'
            }
        }
        
        
        
        stage('Test') {
            steps{
                script {
                    def command = ''
                    if (params.RUN_TEST_ADD) {
                        command += 'py -m unittest validate.SimpleTestCase.test_add && '
                    }
                    if (params.RUN_TEST_SUBTRACT) {
                        command += 'py -m unittest validate.SimpleTestCase.test_subtract && '
                    }
                    if (params.RUN_TEST_MULTIPLY) {
                        command += 'py -m unittest validate.SimpleTestCase.test_multiply && '
                    }
                    
                    // Remove trailing '&& ' and run command
                    if (command) {
                        command = command[0..-5]  // Remove last '&& '
                        bat command
                    } else {
                        echo 'No tests selected.'
                    }
                }
            }
        }
        
        
        
        stage('Build') {
            steps {
                bat '''
                    pyinstaller --onefile unrelated.py
                '''
            }
        }
        

        stage('Archive') {
            steps {
                // Archive the 'dist' folder as an artifact
                archiveArtifacts artifacts: 'dist/**', allowEmptyArchive: true
            }
        }
    }
    
    post {
        always {
            // Cleanup: Remove the cloned repository
            cleanWs()
        }
    }
}
