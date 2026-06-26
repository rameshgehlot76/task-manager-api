# ⚡ Task Manager REST API.  

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-00C853?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-00C853?style=for-the-badge)
![Postman](https://img.shields.io/badge/Postman-Tested-FF6C37?style=for-the-badge&logo=postman&logoColor=white)  

A clean, production-ready RESTful API for task management built with Flask and SQLAlchemy. Supports full CRUD operations — Create, Read, Update, and Delete tasks — with proper HTTP status codes, error handling, and JSON responses.  

---

## ✨ Features

- ✅ **Full CRUD** — Create, Read, Update, Delete tasks
- 🛡️ **Input Validation** — clean error messages for invalid requests
- 📦 **JSON Responses** — industry standard API format
- 🗄️ **SQLite Database** — persistent storage with SQLAlchemy ORM
- 🔢 **HTTP Status Codes** — 200, 201, 400, 404, 405, 500
- 🧩 **Blueprint Architecture** — clean, modular code structure
- 🧪 **Postman Tested** — all endpoints verified

---

## 🛠️ Tech Stack 

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Framework | Flask |
| Database | SQLite |
| ORM | Flask-SQLAlchemy |
| Architecture | REST API with Blueprints |
| Testing | Postman |

---

## 📋 API Endpoints 

| Method | Endpoint | Description | Status Code |
|---|---|---|---|
| GET | `/tasks` | Get all tasks | 200 |
| GET | `/tasks/<id>` | Get single task | 200 / 404 |
| POST | `/tasks` | Create new task | 201 |
| PUT | `/tasks/<id>` | Update task | 200 / 404 |
| DELETE | `/tasks/<id>` | Delete task | 200 / 404 |

---

## 🚀 Run Locally 

### 1. Clone the repo
```bash
git clone https://github.com/rameshgehlot76/task-manager-api.git
cd task-manager-api
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

### 5. Test with Postman or curl
```
http://127.0.0.1:5000
```

---

## 📬 API Usage Examples

### Create a Task
```http
POST /tasks
Content-Type: application/json

{
    "title": "Buy groceries"
}
```
**Response (201):**
```json
{
    "id": 1,
    "title": "Buy groceries",
    "done": false
}
```

### Get All Tasks
```http
GET /tasks
```
**Response (200):**
```json
[
    {
        "id": 1,
        "title": "Buy groceries",
        "done": false
    }
]
```

### Update a Task
```http
PUT /tasks/1
Content-Type: application/json

{
    "title": "Buy groceries and cook",
    "done": true
}
```
**Response (200):**
```json
{
    "id": 1,
    "title": "Buy groceries and cook",
    "done": true
}
```

### Delete a Task
```http
DELETE /tasks/1
```
**Response (200):**
```json
{
    "message": "Task 1 deleted successfully"
}
```

---

## 📦 Project Structure

```
task-manager-api/
│
├── app.py              # Flask app — registers blueprints & error handlers
├── routes.py           # All API endpoints (CRUD operations)
├── models.py           # Task database model
├── database.py         # SQLAlchemy setup & initialization
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🔍 Error Handling

| Scenario | Status Code | Response |
|---|---|---|
| Task not found | 404 | `{"error": "Task X not found"}` |
| Missing title | 400 | `{"error": "Title is required"}` |
| Empty title | 400 | `{"error": "Title cannot be empty"}` |
| No data sent | 400 | `{"error": "No data provided"}` |
| Wrong method | 405 | `{"error": "Method not allowed"}` |
| Server error | 500 | `{"error": "Internal server error"}` |

---

## 📚 What I Learned

- Designing and building a **RESTful API** from scratch
- **CRUD operations** with Flask and SQLAlchemy ORM
- **HTTP methods** — GET, POST, PUT, DELETE and when to use each
- **HTTP status codes** — 200, 201, 400, 404, 405, 500
- **Blueprint architecture** for clean, modular Flask apps
- **Input validation** and proper error handling in APIs
- Testing APIs with **Postman**
- Database modeling with **SQLAlchemy**

---

## 👨‍💻 Author

**Ramesh**
[![GitHub](https://img.shields.io/badge/GitHub-rameshgehlot76-181717?style=flat&logo=github)](https://github.com/rameshgehlot76)

---

Built with dedication 🚀

> ⭐ If you found this useful, consider starring the repo!
