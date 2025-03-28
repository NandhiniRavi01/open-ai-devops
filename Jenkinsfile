pipeline {
    agent any

    environment {
       GEMINI_API_KEY = credentials('gemini-key') // Secure API Key
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                echo "Setting up Python environment..."
                python3 -m venv /var/lib/jenkins/workspace/open-ai-devops/venv  # Create virtual environment once
                echo "Activating virtual environment..."
                . /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate && \
                pip install --upgrade pip && \
                pip install -r requirements.txt  # Install dependencies
                echo "Virtual environment setup complete."
                '''
            }
        }

        stage('AI-Based DevOps Automation') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                . /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Generating Terraform script using AI..."
                python3 automate_devops.py
                '''
            }
        }

        
        stage('Monitor Logs with AI') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                . /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Analyzing Jenkins logs using AI..."
                python3 monitor_logs.py
                '''
            }
        }

        stage('Optimize Testing with AI') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                . /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Generating test cases using AI..."
                python3 generate_tests.py
                '''
            }
        }

        stage('Run AI-Generated Tests') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                . /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Executing AI-generated test cases..."
                pytest test_cases.py
                '''
            }
        }
    }

    post {
        success {
            echo "🚀 Pipeline executed successfully! ✅"
        }
        failure {
            echo "❌ Pipeline failed! Check logs for errors."
        }
    }
}
