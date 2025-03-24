pipeline {
    agent any

    environment {
       OPENAI_API_KEY = credentials('openai-api-key')
    }
stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/NandhiniRavi01/open-ai-devops.git'
    }
}

    

        stage('Setup Python Environment') {
            steps {
                sh 'pip install -r requirements.txt' // Install dependencies
            }
        }

        stage('AI-Based DevOps Automation') {
            steps {
                sh 'python automate_devops.py'  // AI generates Terraform script
            }
        }

        stage('Deploy Infrastructure') {
            steps {
                sh 'terraform init && terraform apply -auto-approve'  // Deploys AI-generated infrastructure
            }
        }

        stage('Monitor Logs with AI') {
            steps {
                sh 'python monitor_logs.py'  // AI detects anomalies in Jenkins logs
            }
        }

        stage('Optimize Testing with AI') {
            steps {
                sh 'python generate_tests.py'  // AI generates test cases
            }
        }

        stage('Run AI-Generated Tests') {
            steps {
                sh 'pytest test_cases.py'  // Executes AI-generated tests
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully! ✅"
        }
        failure {
            echo "Pipeline failed! ❌ Check logs for issues."
        }
    }
}

