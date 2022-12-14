# Hugging Face & Raspbery Pi Flask App

This example Flask app provides an interface for any user to submit text to a field in a browser and see the model predictions rendered in a table. The code to run this app *as is* requires connection to a running, OMI-compliant Docker container on `localhost:45000`.

## Setting up SSH Tunnel

If you followed these [instructions](../README.md#run-model-on-pi-with-docker--grpc) for running a Docker container on your Raspberry Pi, all you have to do is set up a simple SSH tunnel to connect your local server to the port serving the container on the Pi.

```bash
ssh -L 45000:localhost:45000 <user@ip-address-of-pi>
```

Replace `<user@ip-address-of-pi>` with the username and IP address of your device. In doing so, your SSH tunnel will connect. Now, follow the below instructions to spin up your Flask App with a connection to your edge device. 

## Flask App Instructions

The following instructions will generate a simple Python Flask web application that makes inference calls to a Hugging Face Text Classification model running on a Raspberry Pi.

- Download or clone this project from github: `git clone https://github.com/modzy/hugging-face-raspberry-pi.git`
- In your terminal, navigate to the project directory: `cd hugging-face-raspberry-pi/flask-app`
- Install Python
    - If you already have Python installed, you may skip this step.
    - If you don't have Python installed, install it now. You can download an installer from the [Python official website](http://python.org/download/) or on a Mac you can [install with Homebrew](https://docs.brew.sh/Homebrew-and-Python). 
- Create and Activate Virtual Environment
    - Create virtual environment: `python -m venv venv`
    - Activate environment `source venv/bin/activate` (Linux & MacOS) or `.\venv\Scripts\activate` (Windows)
- Install Requirements & Set Environment Variables
    - Install Python packages by running `pip install -r requirements.txt`
    - Now start flask with the command `flask run`
- Open your new Web server!
    - Using a web browser of your choice, navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    - Type any text into the 'My Text' box and hit Analyze.
    
## Table of contents

- [Flask Application code](app.py)
- [config.py](config.py): Flask configuration details
- [routes.py](app/routes.py): Flask App API Endpoints
- [HTML Code](app/templates/emotion.html): Folder containing HTML code