Below is a GitHub-ready `README.md` for the **current version** of your project. I’ve documented what the code actually implements, while keeping Users, Authentication, Authorization, SQLAlchemy, and JWT as **future improvements** rather than claiming they already exist.

# Task Management REST API

A beginner-friendly **Task Management REST API** built with **Python and Flask**.

This project is designed to practice REST API development concepts including CRUD operations, HTTP methods, JSON requests/responses, query parameters, searching, filtering, sorting, pagination, input validation, and HTTP status codes.

> **Project status:** Currently uses an in-memory Python list as the data store. Database persistence, users, authentication, and authorization are planned for later versions.

---

## Features

### Task Management

* Create a task
* Retrieve all tasks
* Retrieve a single task by ID
* Update a task using PATCH
* Delete a task
* Search tasks by title
* Filter tasks by:

  * Title
  * Description
  * Priority
  * Status
* Sort tasks
* Sort in ascending or descending order
* Paginate task results
* Validate task IDs
* Validate pagination parameters
* Validate sorting parameters
* Return appropriate HTTP status codes
* JSON API responses

---

## Technologies Used

* **Python**
* **Flask**
* **REST API**
* **JSON**
* **HTTP**
* **Postman** for API testing

---

## Project Structure

```text
task-management-api/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd task-management-api
```

---

### 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
```

Windows:

```bash
python -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install Flask

```bash
pip install flask
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
Flask
```

---

## Running the API

Start the Flask development server:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

# API Endpoints

## Get All Tasks

```http
GET /api/v1/tasks
```

Returns a paginated list of tasks.

### Example

```text
http://127.0.0.1:5000/api/v1/tasks
```

### Default pagination

If no pagination parameters are provided:

```text
page = 1
per_page = 5
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?page=1&per_page=5
```

---

# Search Tasks

Search tasks by title using the `search` query parameter.

```http
GET /api/v1/tasks?search=flask
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?search=flask
```

The search is case-insensitive.

For example:

```text
search=flask
```

can match:

```text
Learn Flask
Study Flask Request
```

---

# Filter Tasks

## Filter by Title

```http
GET /api/v1/tasks?title=flask
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?title=flask
```

---

## Filter by Description

```http
GET /api/v1/tasks?description=database
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?description=database
```

---

## Filter by Priority

Available priorities:

```text
low
medium
high
```

Example:

```http
GET /api/v1/tasks?priority=high
```

---

## Filter by Status

Available statuses:

```text
pending
in_progress
completed
```

Example:

```http
GET /api/v1/tasks?status=completed
```

---

# Combine Search and Filters

Multiple query parameters can be used together.

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?search=api&priority=high&status=in_progress
```

This allows the API to:

1. Search for `api`
2. Filter by high priority
3. Filter by `in_progress` status

---

# Sorting

Tasks can be sorted using:

```text
sort_by
```

and:

```text
sort_order
```

### Supported sort fields

```text
id
priority
status
```

### Sort ascending

```http
GET /api/v1/tasks?sort_by=priority&sort_order=asc
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?sort_by=priority&sort_order=asc
```

### Sort descending

```http
GET /api/v1/tasks?sort_by=priority&sort_order=desc
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?sort_by=status&sort_order=desc
```

If `sort_by` is not provided, the API defaults to:

```text
id
```

If `sort_order` is not provided, the API defaults to:

```text
asc
```

---

# Pagination

Pagination uses:

```text
page
per_page
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?page=2&per_page=10
```

The API calculates:

```python
start = (page - 1) * per_page
```

and:

```python
end = start + per_page
```

This determines which tasks are returned.

### Pagination Response

Example:

```json
{
    "tasks": [
        {
            "id": 6,
            "title": "Build Task API",
            "description": "Create CRUD endpoints for tasks",
            "priority": "high",
            "status": "in_progress"
        }
    ],
    "pagination": {
        "page": 2,
        "per_page": 5,
        "total": 50,
        "pages": 10
    }
}
```

---

# Get Task by ID

```http
GET /api/v1/tasks/<id>
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks/10
```

Returns the task with the specified ID.

### Successful response

```json
{
    "id": 10,
    "title": "Practice UPDATE Queries",
    "description": "Learn how to update database records",
    "priority": "medium",
    "status": "pending"
}
```

---

# Create a Task

```http
POST /api/v1/tasks
```

### Request body

Set Postman to:

```text
Body
→ raw
→ JSON
```

Example:

```json
{
    "title": "Learn Flask Authentication",
    "description": "Study authentication in Flask APIs",
    "priority": "high",
    "status": "pending"
}
```

### Response

```json
{
    "id": 51,
    "title": "Learn Flask Authentication",
    "description": "Study authentication in Flask APIs",
    "priority": "high",
    "status": "pending"
}
```

HTTP status:

```text
201 Created
```

---

# Update a Task

The current implementation uses the task ID as a query parameter.

```http
PATCH /api/v1/tasks?id=<id>
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?id=10
```

### Request body

You can update individual fields.

For example:

```json
{
    "status": "completed"
}
```

Or multiple fields:

```json
{
    "title": "Practice SQL UPDATE",
    "priority": "high",
    "status": "completed"
}
```

The API uses PATCH because only the supplied fields are changed.

---

# Delete a Task

The current implementation uses the task ID as a query parameter.

```http
DELETE /api/v1/tasks?id=<id>
```

Example:

```text
http://127.0.0.1:5000/api/v1/tasks?id=10
```

If the task exists, it is removed from the in-memory list.

Successful response:

```text
204 No Content
```

---

# HTTP Status Codes Used

| Status Code | Meaning     | Example                       |
| ----------- | ----------- | ----------------------------- |
| `200`       | OK          | Successful GET/PATCH          |
| `201`       | Created     | Task successfully created     |
| `204`       | No Content  | Task successfully deleted     |
| `400`       | Bad Request | Invalid ID or query parameter |
| `404`       | Not Found   | Task does not exist           |

---

# Error Handling

### Invalid Task ID

Request:

```text
GET /api/v1/tasks/abc
```

Response:

```json
{
    "error": "Id must be an integer"
}
```

Status:

```text
400 Bad Request
```

---

### Invalid ID Value

Request:

```text
GET /api/v1/tasks/0
```

Response:

```json
{
    "error": "Id must be greater than or equal to 1"
}
```

Status:

```text
400 Bad Request
```

---

### Task Not Found

Request:

```text
GET /api/v1/tasks/999
```

Response:

```json
{
    "error": "Task not found"
}
```

Status:

```text
404 Not Found
```

---

### Invalid Sort Field

Example:

```text
GET /api/v1/tasks?sort_by=invalid
```

Response:

```json
{
    "error": "Invalid sort field",
    "allowed": [
        "id",
        "priority",
        "status"
    ]
}
```

---

### Invalid Sort Order

Example:

```text
GET /api/v1/tasks?sort_order=random
```

Response:

```json
{
    "error": "Sort order must be asc or desc"
}
```

---

# Query Parameter Reference

| Parameter     | Purpose               | Example                |
| ------------- | --------------------- | ---------------------- |
| `search`      | Search task titles    | `search=flask`         |
| `title`       | Filter by title       | `title=api`            |
| `description` | Filter by description | `description=database` |
| `priority`    | Filter by priority    | `priority=high`        |
| `status`      | Filter by status      | `status=pending`       |
| `sort_by`     | Sort field            | `sort_by=priority`     |
| `sort_order`  | Sort direction        | `sort_order=desc`      |
| `page`        | Page number           | `page=2`               |
| `per_page`    | Tasks per page        | `per_page=10`          |

---

# Example API Requests

### Get first page

```text
GET /api/v1/tasks?page=1&per_page=5
```

### Search

```text
GET /api/v1/tasks?search=api
```

### Filter

```text
GET /api/v1/tasks?priority=high
```

### Sort

```text
GET /api/v1/tasks?sort_by=priority&sort_order=desc
```

### Search + filter + sorting

```text
GET /api/v1/tasks?search=api&priority=high&sort_by=status&sort_order=asc
```

### Pagination + filtering

```text
GET /api/v1/tasks?status=pending&page=2&per_page=5
```

### Get individual task

```text
GET /api/v1/tasks/10
```

### Create task

```text
POST /api/v1/tasks
```

### Update task

```text
PATCH /api/v1/tasks?id=10
```

### Delete task

```text
DELETE /api/v1/tasks?id=10
```

---

# Testing with Postman

This API can be tested using Postman.

Recommended testing sequence:

### 1. GET all tasks

```text
GET /api/v1/tasks
```

### 2. GET a single task

```text
GET /api/v1/tasks/1
```

### 3. POST a new task

```text
POST /api/v1/tasks
```

### 4. PATCH a task

```text
PATCH /api/v1/tasks?id=1
```

### 5. DELETE a task

```text
DELETE /api/v1/tasks?id=1
```

### 6. Test query parameters

Test:

```text
search
title
description
priority
status
sort_by
sort_order
page
per_page
```

### 7. Test invalid input

Test:

```text
Invalid IDs
Invalid page numbers
Invalid per_page values
Invalid sort fields
Invalid sort orders
Nonexistent task IDs
```

---

# Current Limitations

This is currently a learning-focused API and has several limitations.

### In-memory data

Tasks are stored in:

```python
tasks = [...]
```

Therefore, data is lost when the Flask application restarts.

### No database

The project currently does not use:

```text
SQLite
PostgreSQL
MySQL/MariaDB
SQLAlchemy
```

### No users

There is currently no user system.

### No authentication

The API does not currently use:

```text
JWT
Sessions
API keys
OAuth
```

### No authorization

Any client that can access the API can currently access the available task endpoints.

### No task ownership

Tasks do not currently belong to individual users.

---


# Learning Objectives

This project is intended to develop practical understanding of:

* Flask routing
* HTTP methods
* REST API design
* JSON
* Query parameters
* Path parameters
* CRUD operations
* List comprehensions
* Lambda functions
* `sorted()`
* Filtering
* Searching
* Pagination
* Input validation
* HTTP status codes
* API testing with Postman

Future versions will extend these skills into:

* SQL
* SQLAlchemy
* Database design
* Authentication
* Authorization
* JWT
* API security
* BOLA/IDOR
* RBAC
* API testing

---
