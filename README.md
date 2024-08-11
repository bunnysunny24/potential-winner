# Household Manager API

This is a simple Flask-based API for managing household tasks, expenses, and family members.

## Features

- **Manage Tasks**: Add and mark tasks as completed.
- **Track Expenses**: Add expenses and check if they exceed the available budget.
- **Manage Family Members**: Add family members and view their details.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/household-manager-api.git
    cd household-manager-api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the API

1. **Run the Flask server:**

    ```bash
    python app.py
    ```

2. **Access the API:**

   The API will be available at `http://127.0.0.1:5000/`.

### API Endpoints

- **Get all tasks:**

    ```http
    GET /tasks
    ```

- **Add a new task:**

    ```http
    POST /add_task
    {
        "name": "Clean the house",
        "description": "Vacuum and dust all rooms",
        "price": 50.0
    }
    ```

- **Mark a task as completed:**

    ```http
    POST /complete_task
    {
        "task_name": "Clean the house"
    }
    ```

- **Get all expenses:**

    ```http
    GET /expenses
    ```

- **Add a new expense:**

    ```http
    POST /add_expense
    {
        "name": "Groceries",
        "amount": 100.0,
        "date": "2024-08-10"
    }
    ```

- **Get all family members:**

    ```http
    GET /family_members
    ```

- **Add a new family member:**

    ```http
    POST /add_family_member
    {
        "name": "John",
        "age": 35
    }
    ```

### Project Structure

```plaintext
household-manager-api/
│
├── app.py                   # Main application file
├── requirements.txt         # Python packages required
├── README.md                # Project documentation
└── venv/                    # Virtual environment
