# ml-app-template

An ML project template for CD4ML Workshop in Melbourne, Australia.
Credit: it is based closely on the TW Singapore's team at https://github.com/ThoughtWorksInc/ml-app-template

For infrastructure-related stuff (e.g. provisioning of CI server, deployments, etc.), please refer to https://github.com/ThoughtWorksInc/ml-cd-starter-kit.

## Getting started

1. Fork repository: https://github.com/ThoughtWorksInc/ml-app-template
2. Clone repository: `git clone https://github.com/YOUR_USERNAME/ml-app-template`
3. Install Docker ([Mac](https://docs.docker.com/docker-for-mac/install/), [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/))
4. Start Docker on your desktop
5. Build image and start container:

```shell
# build docker image [Mac/Linux users]
docker build . -t ml-app-template --build-arg user=$(whoami)

# start docker container [Mac/Linux users]
docker run -it  -v $(pwd):/home/ml-app-template \
                -p 8080:8080 \
                -p 8888:8888 \
                ml-app-template bash

You're ready to roll! Here are some common commands that you can run in your dev workflow. Run these in the container.

```shell
# add some color to your terminal
source bin/color_my_terminal.sh

# run unit tests
nosetests

# run unit tests in watch mode and color output
nosetests --with-watch --rednose --nologcapture

# train model
SHOULD_USE_MLFLOW=false python src/train.py

# start flask app in development mode
python src/app.py

# make requests to your app
# 1. In your browser, visit http://localhost:8080
# 2. Open another terminal in the running container (detailed instructions below) and run:
bin/predict.sh http://localhost:8080

# You can also use this script to test your deployed application later:
bin/predict.sh http://my-app.com
```

Here are some other commands that you may find useful
```shell
# see list of running containers
docker ps

# start a bash shell in a running container
docker exec -it <container-id> bash

# starting jupyter notebook server on http://localhost:8888
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

## What's in this repo?

We've created a project template to help you with the boilerplate code that we usually have to write in any typical project.

To reduce incidental complexity, we used a simple dataset (boston housing prices) to train a simple linear regression model. Replace the (i) data, (ii) data preprocessing code and (iii) model specification for your use case.

This is the project structure:

```sh
.
├── Dockerfile
├── README.md
├── requirements-dev.txt              # specify dev dependencies (e.g. jupyter) here
├── requirements.txt                  # specify app dependencies here
├── ci.gocd.yaml                      # specify your CI pipeline here
└── src                               # place your code here
    ├── app.py
    ├── app_with_logging.py
    ├── tests                         # place your tests here
    │   ├── test.py
    │   └── test_model_metrics.py
    └── settings.py                   # define environment variables here
    └── train.py
├── bin                               # store shell scripts here
│   ├── color_my_terminal.sh
│   ├── configure_venv_locally.sh
│   ├── predict.sh
│   ├── start_server.sh
│   ├── test.sh
│   ├── test_model_metrics.sh
│   └── train_model.sh
├── docs
│   ├── FAQs.md
│   └── mlflow.md
├── models                            # serialize stuff here
│   ├── _keep
│   ├── column_order.joblib
│   └── model.joblib

```
