# ml-app-template-workshop

An ML project template for CD4ML Workshop in Melbourne, Australia.

<br/>
Credit: it is based closely on the TW Singapore's team at https://github.com/ThoughtWorksInc/ml-app-template


# Getting started

1. Clone repository: `git clone https://github.com/brdnguyen/ml-app-template-workshop`
3. Install Docker ([Mac](https://docs.docker.com/docker-for-mac/install/), [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/))
4. Start Docker host (Docker Desktop) on your desktop
5. Build Docker images and start containers:

```shell
# build docker images
docker-compose build

# start docker containers
docker-compose up

```

At this point, you should see 2 running containers, which expose 2 http endpoints via ports 5000 (MLFlow) and 8080 (Flask app for making). visit:

http://localhost:5000  (this is where MLFlow is hosted)
http://localhost:8080  (This is where the main Flask app is )


<br/>
You are ready to roll! Here are some common commands that you can run in your dev workflow. Run these in the container.


```shell
# View list of running containers
docker ps


# Log into the main app container
docker exec -it <container-id> /bin/bash


# add some color to your terminal
source bin/color_my_terminal.sh

# to tear down containers:
docker-compose stop
```


## Task 1: Run tests, and fix failing tests

In your container (`ml-app-template-workshop`), run:
```
nosetests
```

To fix this failing test, in your code editor, edit

`test_model_metrics.py, line 16`

Follow the instruction around the TODO comment. Once you fix the tests, build the model again with
```
python src/train.py
```

Then, test again with `nosetests` . The test should now pass.


## Task 2: Train and version model with MLFlow

In your container, run:

```
python src/train.py
```

In your web browser (on local laptop), visit http://localhost:5000 . You shoud see MLFlow has captured the change.

## Task 3: Let's change the Model

Let's keep the training data the same, but change the model logic. We want to see the change captured and versioned by MLFlow.

In `src\train.py`, look for "TODO for Task 3" change it to:
```
N_ESTIMATORS = 100
```

then, run:

```
python src/train.py
```

See the change in MLFlow UI (localhost:5000)

## Task 4: Make a change to the training data, and version that with MLFlow

Go to `src/train.py`, find "TODO for Task 4", and make the change (uncomment the code) as in the suggestion.

Run
```
    python src/train.py
```

Then check Mlflow again at localhost:5000 . You should see the change (look for param n_columns_training_data) captured and versioned by MLFlow.


## Task 5: (Optional) Fix bugs with changing training data

In Task 4, when we change the training data (adding one column), you we introduced a bug
in the consumer app (that makes use of the model to predict).

It is a common bug in ML pipelines when there are changes in feature processing in "Training"
phase, but the same changes did not propagate property to the "Prediction" phase.

Hint on fixing: The model is trained on 14 columns, while the prediction (`bin/predict.sh` only passes in 13 columns as parameters, thus being in compatible).

# Consume the model

It is not the focus of this workshop, but we'll walk you through the bit to make live prediction (from an API), from the model we have trained.

## make requests to your app
1. In your browser, visit http://localhost:8080 to verify the end point is ready.
2. Open another terminal and run:
```
bin/predict.sh http://localhost:8080
```
# References

https://github.com/ThoughtWorksInc/ml-app-template
https://www.thoughtworks.com/insights/articles/intelligent-enterprise-series-cd4ml

