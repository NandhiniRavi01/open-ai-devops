pipeline {
    agent any

    environment {
       GEMINI_API_KEY = credentials('gemini-key') // Secure API Key
    }

    stages {
        
      
  stage('install dependencies') {
    steps {
    sh '''
        echo "Setting up Python environment..."
        python3 -m venv venv  # Create virtual environment
        echo "Activating virtual environment..."
        . venv/bin/activate && \
        pip install --upgrade pip && \
        pip install -r requirements.txt  # Install dependencies
        echo "Virtual environment setup complete."
    '''
}
  }


       stages {
        stage('AI-Based DevOps Automation') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                source /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Generating Terraform script using AI..."
                python3 automate_devops.py
                '''
            }
        }

        stage('Deploy Infrastructure') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                source /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Initializing Terraform..."
                terraform init
                
                echo "Applying AI-generated Terraform configurations..."
                terraform apply -auto-approve
                '''
            }
        }

        stage('Monitor Logs with AI') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                source /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Analyzing Jenkins logs using AI..."
                python3 monitor_logs.py
                '''
            }
        }

        stage('Optimize Testing with AI') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                source /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

                echo "Generating test cases using AI..."
                python3 generate_tests.py
                '''
            }
        }

        stage('Run AI-Generated Tests') {
            steps {
                sh '''
                echo "Activating virtual environment..."
                source /var/lib/jenkins/workspace/open-ai-devops/venv/bin/activate

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
}
