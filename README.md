# P6-API_for_ML_model

## Develop a Machine Learning classification model (Application Programming Interface) using FastAPI.
![sepsis](https://github.com/sethsot/P6-API_for_ML_model/assets/137343449/937e7b88-79f2-4c55-9b3a-a3ad40204f15)


Introduction
In this project, we aim to discover how to create an API that might be requested to interact with our classification ML model. This is an interesting solution when you want to keep your model architecture secret or to make your model available to users already having an API. By creating an API, and deploying it, your model can receive request using the internet protocol. 

![api depiction](https://github.com/sethsot/P6-API_for_ML_model/assets/137343449/f59b4f22-e6ac-4505-9460-466c2123136b)


Description
You will have a minimal API demo with FastAPI, this will just serve you to make sure that everything works correctly. Then, you will have to make your own API, this allowing you to interact with a Machine Learning model, that is to say:

Pass data through a request;
Get the data in using the API;
Apply the necessary processing;
Submit the processed data to the ML model to make the predictions;
Process the predictions obtained and return them as the API's response ot the input request.
Setup
Install the required packages to be able to run the evaluation locally.

You need to have Python 3 on your system (a Python version lower than 3.10). Then you can clone this repo and being at the repo's root :: repository_name> ... follow the steps below:

Windows:

  python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  
Linux & MacOs:

  python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  
The both long command-lines have a same structure, they pipe multiple commands using the symbol ; but you may manually execute them one after another.

Create the Python's virtual environment that isolates the required libraries of the project to avoid conflicts;
Activate the Python's virtual environment so that the Python kernel & libraries will be those of the isolated environment;
Upgrade Pip, the installed libraries/packages manager to have the up-to-date version that will work correctly;
Install the required libraries/packages listed in the requirements.txt file so that it will be allow to import them into the python's scripts and notebooks without any issue.
NB: For MacOs users, please install Xcode if you have an issue.

Run FastAPI
Run the demo apps (being at the repository root):

FastAPI:

