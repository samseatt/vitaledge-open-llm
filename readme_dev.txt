
# conda create -n vitaledge-open-llm python=3.11 -y
conda activate vitaledge-open-llm



### How to Use
## Setup Environment:
# Add OPENAI_API_KEY to your .env file.
export OPENAI_API_KEY=sk-proj-...

# Run docker-compose up to build and start the service.

##Endpoints:
# /openai/generate POST: Takes prompt and model as input.

uvicorn app.main:app --host 0.0.0.0 --port 8005 --reload

curl -X POST http://127.0.0.1:8005/openai/generate      -H "Content-Type: application/json"      -d '{
           "model": "gpt-4o",
           "prompt": "Explain Loop Quantum Gravity in an essay."
         }'


