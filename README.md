# Riley
CPU compatible local LLM

This repository contains a Q4 quantized local Language Model (LLM) model that is compatible for CPU usage. This system is designed to provide efficient and fast text generation and processing on CPU-based systems through a browser interface.

This repository uses Llama-2-7B-Chat-GGLM base model published by "TheBloke" on HuggingFace.
Images used in the webpage are generated through [Leonardo.AI](https://leonardo.ai/)


## Requirements
You need to have python installed on your system.
you need to be able to connect to the internet to download the model (and nessessary packages) ONLY THE FIRST TIME. once the model is downloaded the system will run compleetly offline.

## Getting Started

To use this CPU-compatible Q4 quantized local LLM model, follow these steps:

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/akshaykadidal/Riley.git
   
  If you don't have git installed just download the resposity in to your system (keep the folder structure intact)
  
  ```python
  pip install -r requirements.txt --user
```

## Features

- **Quantized Model**: The model has been quantized to use only 4 bits for representing weights, reducing memory and computational requirements while maintaining reasonable performance. 

- **Local Context**: The model is optimized for local context processing, making it suitable for various natural language processing tasks, including text completion, sentiment analysis, and more.

- **CPU Compatibility**: This model is designed to run efficiently on CPU-based systems, making it accessible to a wide range of devices and platforms.

- **Can be used through a Browser locally 
