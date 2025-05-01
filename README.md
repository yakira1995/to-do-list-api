# To-Do List RESTful API

A lightweight and functional backend system for managing tasks, built using Python and Flask. This project demonstrates core backend development skills, including designing RESTful APIs, database integration, and implementing CRUD (Create, Read, Update, Delete) functionality.

---

## Features
- **CRUD Operations**: Add, view, update, and delete tasks.
- **Database Integration**: SQLite used for persistent task storage.
- **RESTful API Design**: Adheres to REST principles for scalable and maintainable APIs.
- **Error Handling**: Robust error handling with meaningful HTTP responses.
- **Testing**: Thoroughly tested endpoints using Postman.

---

## Technologies
- **Programming Language**: Python
- **Framework**: Flask
- **Database**: SQLite
- **ORM**: Flask-SQLAlchemy
- **Tools**: Postman (API testing), Git (version control)

---

## Installation

### Prerequisites
- Python 3.9+
- Flask and Flask-SQLAlchemy (install via `pip`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yakira1995/to-do-list-api.git
   cd to-do-list-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the API at `http://127.0.0.1:5000`.

---

## API Endpoints

| HTTP Method | Endpoint           | Description                  | Example Request Body          |
|-------------|--------------------|------------------------------|-------------------------------|
| `GET`       | `/tasks`           | Retrieve all tasks           | N/A                           |
| `POST`      | `/tasks`           | Add a new task               | `{ "title": "Learn Flask" }`  |
| `PUT`       | `/tasks/<task_id>` | Mark a task as completed     | N/A                           |
| `DELETE`    | `/tasks/<task_id>` | Delete a task by ID          | N/A                           |

---

## Project Structure

```
to-do-list-api/
│
├── app.py            # Main Flask application
├── models.py         # Database models
├── requirements.txt  # Dependencies
├── .gitignore        # Ignored files for Git
└── README.md         # Project documentation
```

---

## Future Enhancements
- Add user authentication for task management.
- Integrate a frontend using React or Angular.
- Deploy the API to a cloud platform like Heroku or AWS.

---

## License
This project is licensed under the MIT License.
