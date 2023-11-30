pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Hello World, build success'
           }
        }
        stage('Test')
        {
            steps{
                echo 'Test success'
            }
        }
          stage('Deploy')
        {
            steps{
                echo 'Deploy success'
            }
        }
        stage('Final Done')
        {
            steps{
                echo 'Completed'
                date
            }
        }
        
    }
post{
    always{
        emailext body: '', subject: 'Failure', to: 'vineethac96@gmail.com'
    }
}
}
