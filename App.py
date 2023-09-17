from flask import Flask, render_template, request
from ctransformers import AutoModelForCausalLM
import os
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	response_text = ""
	local_path = os.getcwd() + "\\llama-2-7b-chat.ggmlv3.q4_K_S.bin"
	url = 'https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_K_S.bin'
	#url = 'https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/README.md'
	# Check if the file exists locally
	if not os.path.isfile(local_path):
		try:
			# Send an HTTP GET request to the URL
			response = requests.get(url)
			
			# Check if the request was successful (status code 200)
			if response.status_code == 200:
				# Save the content to the local file
				with open(local_path, 'wb') as file:
					file.write(response.content)
				print(f"File downloaded from {url} and saved as {local_path}.")
			else:
				print(f"Error downloading the file. Status code: {response.status_code}")
		except requests.exceptions.RequestException as e:
			print(f"Error downloading the file: {e}")
	else:
		print(f"file in location {local_path}")

	llm = AutoModelForCausalLM.from_pretrained(model_path_or_repo_id = local_path, model_type="llama")
	
	
	if request.method == 'POST':
		user_input = request.form['user_input']
		#return f'Hello, World!\n\nYou entered:\n{user_input}'
		response_text = llm(user_input)
		#response_text = f'Hello, World!\n\nYou entered:\n{user_input}'
	return render_template('index.html', response_text=response_text)

if __name__ == '__main__':
	app.run(debug=True)
