---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Overall project checklist

The checklist is *exhaustic* which means that it includes everything that you could possible do on the project in
relation the curricilum in this course. Therefore, we do not expect at all that you have checked of all boxes at the
end of the project.

### Week 1

* [x] Create a git repository
* [x] Make sure that all team members have write access to the github repository
* [x] Create a dedicated environment for you project to keep track of your packages
* [x] Create the initial file structure using cookiecutter
* [x] Fill out the `make_dataset.py` file such that it downloads whatever data you need and
* [x] Add a model file and a training script and get that running
* [x] Remember to fill out the `requirements.txt` file with whatever dependencies that you are using
* [x] Remember to comply with good coding practices (`pep8`) while doing the project
* [x] Do a bit of code typing and remember to document essential parts of your code
* [ ] Setup version control for your data or part of your data
* [x] Construct one or multiple docker files for your code
* [x] Build the docker files locally and make sure they work as intended
* [x] Write one or multiple configurations files for your experiments
* [x] Used Hydra to load the configurations and manage your hyperparameters
* [x] When you have something that works somewhat, remember at some point to to some profiling and see if
      you can optimize your code
* [x] Use Weights & Biases to log training progress and other important metrics/artifacts in your code. Additionally,
      consider running a hyperparameter optimization sweep.
* [ ] Use Pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### Week 2

* [x] Write unit tests related to the data part of your code
* [x] Write unit tests related to model construction and or model training
* [x] Calculate the coverage.
* [x] Get some continuous integration running on the github repository
* [ ] Create a data storage in GCP Bucket for you data and preferable link this with your data version control setup
* [x] Create a trigger workflow for automatically building your docker images
* [x] Get your model training in GCP using either the Engine or Vertex AI
* [x] Create a FastAPI application that can do inference using your model
* [ ] If applicable, consider deploying the model locally using torchserve
* [x] Deploy your model in GCP using either Functions or Run as the backend

### Week 3

* [ ] Check how robust your model is towards data drifting
* [ ] Setup monitoring for the system telemetry of your deployed model
* [ ] Setup monitoring for the performance of your deployed model
* [ ] If applicable, play around with distributed data loading
* [ ] If applicable, play around with distributed model training
* [ ] Play around with quantization, compilation and pruning for you trained models to increase inference speed

### Additional

* [ ] Revisit your initial project description. Did the project turn out as you wanted?
* [ ] Make sure all group members have a understanding about all parts of the project
* [ ] Uploaded all your code to github

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

27

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sXXXXXX, sXXXXXX, sXXXXXX*
>
> Answer:

s183951, s173853, s212804

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

We choose to work with the pytorch geometric framework, from where we got both the dataset and the model framework. The framework itself actually complicated the project a bit as a lot of the time was used on dependency issues and installation requirements that did not work (most torch-sparse and torch-scatter). However the framework itself worked just fine once installed and we were able to create, train and predict using a model from the framework. We got the data from the Dataset class of pytorch-geometric. We used many of the frameworks taught in the course such as wandb, docker, github actions and gcp. We did not use any frameworks not taught in the course. 

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development enviroment, one would have to run the following commands*
>
> Answer:

We used conda for managing our dependencies. The list of dependencies was auto-generated using pipreqs. To get a complete copy of your development environment, one would have to run the following command: `conda env create -f environment.yml`. 

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

The vast majority of the code is found in the src_2 folder, the rests of the folders should be self explanatory which is one of the benefits of cookiecutter. We removed the folders notebooks, models and src, and added the src_2 folder instead. This was done because when building an image, installing all the packages with pip would create a src folder that would interfere with the import statements within the source folder. Even when we interacted with our docker images we were unable to uninstall the faulty 'src' module and thus settled upon just giving our module a different name to avoid this conflict. We added a tests folder containing a few unit tests. The yml files and the dockerfile(s) was added directly to the root of the project. The models are created in the outputs folder by default using hydra. 

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

We added documentation to the code using docstrings for the functions that were more difficult to understand, to explain their purpose. In terms of styling, we used black to format the code in order to be pep8 compliant, and isort to sort the import statements. We also added typing to most of our functions as a good coding practice, despite their simplicity.
This makes it easier when multiple people are contributing to a project as the code should be more readable. Also when complying to a standard there is less probability for errors (https://standards.ieee.org/beyond-standards/what-are-standards-why-are-they-important/).

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement and what are they testing in your code?**
>
> Answer length: 50-100 words.
>
> Example:
> *In total we have implemented X tests. Primarily we are testing ... and ... as these the most critical parts of our*
> *application but also ... .*
>
> Answer:

We implemented data and training testing. We test whether the dataset is valid, and check for parameter update during training by training a model for one epoch on a random dataset and then looking at the gradients of the model parameters. 

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> Answer length: 100-200 words.
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:

The total code coverage of our source code is 8%. To include all the source scripts, we had to use the command: `coverage run --source='src_2' -m pytest tests/`. We are far from 100% of our code and even if we were, that doesn't mean that it would be error free: 100% coverage only means that all the code would run when the tests are executed. 

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

We made use of branches in the project, primarily so that each person could work on their own branch as to not interfere with the work of the others. A new branch was typically also created while prototyping a new feature (e.g. a branch for Docker, Github Actions etc.). Pull requests were then used to merge the branches to the main branch. 

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

We did not make use of dvc as the dataset was a part of the package that was also used to create the network. Thus the data never changed and nothing new was added to the data. Therefore data version control did not make sense in this project. However if the project was using data that might change and it could be useful to capture which version of the data that was used in a given commit to github. 

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our CI into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:

We are running unittesting. We test two operating systems, Ubuntu and Windows and python version 3.10 which is compatible with pytorch geometric. We also make use of caching to avoid redownloading all the packages every time the workflow gets triggered. An example of a triggered workflow can be seen here: https://github.com/Fuedyolo/mlops_final_project/actions/runs/3965723650. 

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:
      
We configured training experiments with Hydra, with the default configuration being the optimal hyperaparameters obtained after a hyperparameter sweep. Therefore, training a model is as simple as: `python src/models/train_model.py`. The inference script uses click which takes the model and data paths as arguments: `python src/models/predict_model.py MODEL_FILEPATH DATA_FILEPATH`. 

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

We used config files such that each training of a model would create a hydra folder in the outputs folder with a config.yaml file which indicates the settings used for that training, eg. epochs, learning rate etc. To reproduce an experiment exp.yml located in the experiment folder, one would have to use the command: `python src/models/train_model.py experiment=exp`. 


### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

![screenshot](figures/sweep.png)
The first 5 charts track the train and test loss and accuracy for 4 runs of a hyperparameter sweep. The last chart tracks the loss of 4 experiments with the default configuration, e.g. using the hyperparameters of the best model found during the hyperparameter sweep. These metrics are important because they reflect how well our model is learning and is able to generalize to unseen data. 

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

We used docker mostly to get the different part of the project to work with gcp. We used the docker image to both train the model on gcp but also to deploy a function with cloud run. The first docker image is run by simply `docker run <name> trainer:latest`. The second docker image is run by the same command and by specifying which port the user wants to be able to run the application on. 

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

The code for training and predicting was provided in the documentation of pytorch geometric as an introduction using the example of the Cora dataset, which is similar to ours, so we didn't have bugs related to this. However, we ran into an error with the hyperparameter sweep using wandb. By comparing with the example provided by the documentation, and inserting it into our code, we figured out that click was responsible for the error, and removing it solved the issue. Although the code is probably already optimized because it comes from the documentation, we profiled the main code and found that Hydra had the longest runtime in our training script.

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:

We used the following services: Compute Engine, cloud trigger, cloud run, vertex ai and container registry. Compute Engine was used to create a VM, the specifications of the VM was similar to the ones used in the course. The container registry was used to store the image that was created from the dockerfile. Cloud triggers was used to automatically create the new container image when the main branch of the github repo was updated (this was disabled most of the time as new docker images were not needed). Cloud run was used to deploy a simple app that let the user input a datapoint and then predict the output. Vertex ai was used to do model training. 

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

We used the compute engine to create the instance we used for almost all other gcp features in this project. The following hardware was used: 
* Machine type: n1-standard-1
* CPU platform: Intel Haswell
* Architecture: x86/64

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

We did not use GCP buckets as the dataset was stored within the torch-geometric package and therefore available to everyone with the package.

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

Below is the image of the containers in the registry, however they are in the same project as the ones used during the exercises in the course.
![container registry](figures/registry.png)

### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:
The following figure shows the cloud builds, the trigger was disabled as it was not necessary to upload a new image to gcp each time we pushed to main, but the latest successfull one was also the imaged used for training with vertex ai
![cloud build](figures/build.png)

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer:

Using a fastapi application the model was attempted deployed to google cloud run and can be invoked by giving a valid dataset (the used dataset) and returning the accuracy for the model that we trained. 

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

No, monitoring our application wouldn't make sense because our data is fixed, so there can be no data drift. 

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

The billing pane did not show any costs used at all during the month of january however one group member used up all the credits and another used around half of the credits up until the day before the exam. Most of the credits were spend in cloud engine, cloud logging, cloud storage and cloud build.

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:
The starting point of the diagram is out local setup on our computers. In this step the code is being developed and structured using the cookiecutter template. Hydra is responsible for the local logging of experiments while wandb is used to log and visualize the results as well as doing the hyperparameter sweep.
Whenever the code is committed and pushed to GitHub (typically to a new development branch) this activates a sequence of processes. 1) unittests on the data and the main ML model are carried out via GitHub actions. Caching of dependencies was used to speed up this process. 2) A cloud build of the model is made via GCL and the dockerfile (which makes use of the requirements file to install the required libraries). The build concludes with a new model being trained on the data and the results being logged by Hydra/wandb. 3) As an alternative to 2) local docker images were also being generated throughout the development process.
In order to use our model a user can either clone the github repo or pull the latest docker image. The app is not deployed 100% yet but it is possible to upload a dataset to a locally deployed fastapi app and use the model there.
![overview](figures/Overview.jpg)

### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

The main difficulty of running the experiments was understanding how to configure them, and run a hyperparameter sweep, using hydra and wandb. A minor setback was the issues with the required dependencies and the installation of those. A big challenge was getting the fastAPI app to work with correct and to work with cloud run - the problem was mostly with figuring out how to push datafiles to the app. Furthermore, the specific formulation of the docker files was also a big challenge and definently something that requires a lot of practice to master. As with all data science/software development a lot of time was spend on minor bugs, in this case path related bugs especially. 

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:

* s173853 : was in charge of building the docker images, setting up local deployment and the unit tests/github actions
* s212804 : was in charge of setting up the project structure, configuring and logging the experiments, as well as profiling.
* s183951 : was in charge of the things done with gcp and the deployement of the model

Further all team members contributed to the writing of the report.
