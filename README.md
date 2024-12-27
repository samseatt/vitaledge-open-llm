# VitalEdge Open LLM

VitalEdge Open LLM is a microservice designed to interface with external language models, such as OpenAI's GPT models. It provides a robust and flexible API for generating text and managing backend configurations, making it an essential part of the VitalEdge ecosystem. This service is particularly useful for handling tasks where external LLMs are preferred, while maintaining a modular and extensible design.

---

## Features

- **Text Generation**: Generate coherent and context-aware text based on user prompts.
- **Dynamic Backend Switching**: Switch between external LLM backends (e.g., OpenAI) without restarting the service.
- **Admin Endpoints**: Manage backend configurations and monitor the service.
- **Scalable Design**: Built using FastAPI for high performance and ease of integration.

---

## Requirements

- Python 3.11 or higher
- `pip` and `pip-tools` for dependency management

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/samseatt/vitaledge-open-llm.git
   cd vitaledge-open-llm
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following content:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

---

## Running the Service

1. Start the service using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The service will be available at:
   ```
   http://127.0.0.1:8000
   ```

---

## API Endpoints

### Text Generation
- **Route**: `/generate`
- **Method**: `POST`
- **Input**:
  ```json
  {
    "text": "What are the symptoms of diabetes?"
  }
  ```
- **Output**:
  ```json
  {
    "response": "The symptoms of diabetes include increased thirst, frequent urination, and fatigue."
  }
  ```

### Admin: Set Backend
- **Route**: `/admin/set_model`
- **Method**: `POST`
- **Input**:
  ```json
  {
    "backend": "openai"
  }
  ```
- **Output**:
  ```json
  {
    "status": "success",
    "message": "Backend switched to openai."
  }
  ```

### Admin: Get Backend
- **Route**: `/admin/get_model`
- **Method**: `GET`
- **Output**:
  ```json
  {
    "backend": "openai"
  }
  ```

---

## Development and Contribution

### Testing

To run tests:
```bash
pytest
```

### Dependency Management

Use `pip-tools` to manage dependencies:
1. Modify `requirements.in` for new dependencies.
2. Compile the `requirements.txt` file:
   ```bash
   pip-compile requirements.in
   ```

### Contributing

Contributions are welcome! Please follow the guidelines below:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes and open a pull request.

---

## Future Enhancements

1. **Streaming Responses**: Add support for streamed outputs.
2. **De-Identification**: Enable preprocessing of sensitive inputs before sending them to external APIs.
3. **Advanced Security**: Implement access control for admin routes.
4. **Integration with Other VitalEdge Services**: Seamlessly integrate with `vitaledge-analytics` for enhanced workflows.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For inquiries or support, contact the VitalEdge team at:
**Email**: samseatt@gmail.com 
**Website**: [xmed.ai](https://xmed.ai)
