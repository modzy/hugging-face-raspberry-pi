from flask import render_template
from app import app
from app.forms import *
import time

from modzy.edge.client import EdgeClient
client = EdgeClient("localhost",55000)

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
	job = client.submit_text('uxchm260wz', '1.0.0', {'input.txt': input_text})
	time.sleep(1)
	_ = client.block_until_complete(job, timeout=None)
	results = client.get_results(job)
	return (results['results']['job']['results.json']['data']['result'])