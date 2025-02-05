import hudson.console.*

pipeline {
    agent { label 'easyWorker' }
    options {
        timestamps()
    }
    stages {
        stage ('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage ('Checkout fem011-eiffel002 Repository') {
            steps {
                dir('abcdef') {
                    checkout([$class: 'GitSCM',
                        branches: [[name: 'FETCH_HEAD']],
                        extensions: [[$class: 'CloneOption', honorRefspec: true]],
                        userRemoteConfigs: [[refspec: "${FEM_REPO_PATCHSET_REVISION}",
                                            url: "${gitUrl}platform/jenkins-conf/fem011-eiffel002"]]])
                }
            }
        }

        stage('Preparation stage') {
            steps {

            }
        }
      }
