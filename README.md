# Lab 13-3 Deploy a ML model with fastAPI and Docker

In this lab you will deploy a webserver that hosts a predictive model trained on the [wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine) using [FastApi](https://fastapi.tiangolo.com/) and [Docker](https://www.docker.com/).

In this lab we will use a trained wine-classifier that uses a [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) and a [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) with a forest of 10 trees. We use this simple classifier so that our docker image can be built quickly and the file size is small.

To run this lab, you need to have a docker engine. We will use a free cloud-based one [Play with Docker](https://labs.play-with-docker.com).

----

## Why not on your own computer

If you are to install this on your own Windows computer, you will first need to install/enable Windows Subsystem for Linux, and then download a Linux image such as Ubuntu, before you can install Docker. These steps take a long time to finish. Moreover, your system (especially its old) may not be fully compatible. Once they're in place, they take a lot of space (e.g. 20 GB) and much system resources. After all, you are trying to create/run a virtual Linux computer within your computer. 

----


## How this lab works


By the end of this lab you will have built two versions of the webserver, one that can output only one prediction per request and another one that enables batching. During this you will learn about some of FastAPI's features, how to create a `Dockerfile` and other key Docker concepts such as `image tagging`.

The best way to follow along is to read this documentation from your browser while working on a cloned version of this repo on your local machine by using a terminal.

Within the documentation, snippets of the files will be displayed with a description of what is going on. Notice that the same code can be found within the repo.

To clone this repo use the following command:

```bash
git clone https://github.com/de4liu/bigdata_lab13_2_docker_working.git
```

--------

Let's get started by jumping to the section [Part 1 - One prediction per request](./no-batch/README.md)!

Or if you have already completed part 1 you can jump straight to [Part 2 - Adding batching to the server](./with-batch/README.md)!
