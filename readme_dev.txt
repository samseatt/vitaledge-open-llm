
# conda create -n vitaledge-open-llm python=3.11 -y
conda activate vitaledge-open-llm



### How to Use
## Setup Environment:
# Add OPENAI_API_KEY to your .env file.
# Run docker-compose up to build and start the service.

##Endpoints:
# /openai/generate POST: Takes prompt and model as input.

uvicorn app.main:app --host 0.0.0.0 --port 8005 --reload

