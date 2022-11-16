from flask import render_template
from app import app
from app.forms import *
import time

import json
import logging
from typing import Dict
import grpc
from app.auto_generated.model2_template.model_pb2 import InputItem, RunRequest, RunResponse, StatusRequest
from app.auto_generated.model2_template.model_pb2_grpc import ModzyModelStub
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
HOST = "localhost"
PORT = 45000

@app.route('/', methods=['GET', 'POST'])
@app.route('/emotion', methods=['GET', 'POST'])
def emotion():
	form = TextClassificationAnalysisForm()

	if form.validate_on_submit():
		if form.input_text.data == 'asdf':
			data = {'input-text':form.input_text.data,"classPredictions":[{"class":"neutral","score":0.831},{"class":"negative","score":0.137},{"class":"positive","score":0.032}]} #this example output is used for debugging.
		else:
			data = tinybertclassifier(form.input_text.data)
			data['input-text'] = form.input_text.data
		return render_template('/emotion.html', form=form, data=data)
	return render_template('/emotion.html', title='Emotion Text Classification', form=form, data=None)

@app.route('/next')
def index():
	return render_template('index.html')

def tinybertclassifier(input_text):
    with grpc.insecure_channel(f"{HOST}:{PORT}") as grpc_channel:
        grpc_client_stub = ModzyModelStub(grpc_channel)
        try:
            grpc_client_stub.Status(StatusRequest())  # Initialize the model
        except Exception:
            LOGGER.error(
                f"It appears that the Model Server is unreachable. Did you ensure it is running on {HOST}:{PORT}?"
            )
            return    
        
        run_request = RunRequest(inputs=[create_input({"input.txt": input_text.encode()})])
        single_response = grpc_client_stub.Run(run_request) 
        json_output = json.loads(single_response.outputs[0].output["results.json"].decode())   
        output = json_output['data']['result']
        
    return output

def create_input(input_text: Dict[str, bytes]) -> InputItem:
	input_item = InputItem()
	for input_filename, input_contents in input_text.items():
		input_item.input[input_filename] = input_contents
	return input_item