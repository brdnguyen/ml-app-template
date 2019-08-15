import os
SHOULD_USE_MLFLOW='true'
PORT=8080
# CI is defined as 'true' in ci.gocd.yaml
CI=os.environ.get('CI', '')

# replace the following with the external IP of your k8s services
MLFLOW_IP='mlflow'
FLUENTD_IP='35.198.222.225'
