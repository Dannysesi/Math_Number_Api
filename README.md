# Math Number Classification API

## Project Overview
This project is a simple web API built using Django and Django REST Framework (DRF) to classify numbers based on input provided by users. The API processes requests and returns information about whether the given number is positive, negative, or zero, as well as whether it is odd or even.

The API is deployed on Render at the following endpoint:

**[Math Number Classification API](https://math-number-api.onrender.com/api/classify-number?number=500)**

## Features
- Classify a number as **positive**, **negative**, or **zero**.
- Determine whether a number is **odd** or **even**.
- JSON responses for easy integration.

## Endpoint Details
### **GET /api/classify-number?number=**

#### Parameters
- `number` (required): An integer to classify.

#### Example Request
```bash
GET https://math-number-api.onrender.com/api/classify-number?number=500
```

#### Example Response
```json
{
    "number": 500,
    "is_prime": false,
    "is_perfect": false,
    "properties": [
        "even"
    ],
    "digit_sum": 5,
    "fun_fact": "500 is the number of planar partitions of 10."
}
```

#### Error Handling
If the input is missing or invalid, the API responds with an appropriate error message:

Example:
```json
{
    "number": "A",
    "error": "Invalid input"
}
```

## Project Structure
```
math_api_project/
├── manage.py
├── math_api_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/
    ├── views.py
    └── urls.py
```

## Installation Instructions
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd math_api_number
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Application Locally:**
   ```bash
   python manage.py runserver
   ```
   Access the API at: `http://127.0.0.1:8000/api/classify-number?number=10`

## Deployment
The project is deployed using Gunicorn on Render:

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Run the App:**
   ```bash
   gunicorn math_api_project.wsgi:application --bind 0.0.0.0:8000
   ```


