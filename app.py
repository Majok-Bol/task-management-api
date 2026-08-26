from flask import Flask,request,jsonify
app=Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Flask",
        "description": "Study Flask fundamentals and routing",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 2,
        "title": "Build REST API",
        "description": "Create a basic REST API with Flask",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 3,
        "title": "Learn HTTP Methods",
        "description": "Understand GET, POST, PUT, PATCH and DELETE",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 4,
        "title": "Practice Postman",
        "description": "Test API endpoints using Postman",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 5,
        "title": "Learn JSON",
        "description": "Understand JSON objects, arrays and data types",
        "priority": "low",
        "status": "completed"
    },
    {
        "id": 6,
        "title": "Build Task API",
        "description": "Create CRUD endpoints for tasks",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 7,
        "title": "Learn SQL",
        "description": "Study SQL queries and database fundamentals",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 8,
        "title": "Create Database",
        "description": "Create a database for the task management system",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 9,
        "title": "Practice SELECT Queries",
        "description": "Practice retrieving records using SQL",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 10,
        "title": "Practice UPDATE Queries",
        "description": "Learn how to update database records",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 11,
        "title": "Learn Python Functions",
        "description": "Practice defining and calling Python functions",
        "priority": "low",
        "status": "completed"
    },
    {
        "id": 12,
        "title": "Practice Python Lists",
        "description": "Work with lists and list comprehensions",
        "priority": "low",
        "status": "completed"
    },
    {
        "id": 13,
        "title": "Learn Dictionaries",
        "description": "Practice Python dictionaries and nested data",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 14,
        "title": "Study Flask Request",
        "description": "Learn how Flask handles incoming requests",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 15,
        "title": "Study Flask Response",
        "description": "Learn how Flask sends API responses",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 16,
        "title": "Learn jsonify",
        "description": "Understand how jsonify creates JSON responses",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 17,
        "title": "Handle API Errors",
        "description": "Create proper error responses for API clients",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 18,
        "title": "Learn Status Codes",
        "description": "Study common HTTP status codes",
        "priority": "high",
        "status": "completed"
    },
    {
        "id": 19,
        "title": "Test GET Endpoint",
        "description": "Test retrieving all tasks",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 20,
        "title": "Test POST Endpoint",
        "description": "Test creating a new task",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 21,
        "title": "Test PATCH Endpoint",
        "description": "Test partially updating a task",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 22,
        "title": "Test DELETE Endpoint",
        "description": "Test deleting an existing task",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 23,
        "title": "Implement Search",
        "description": "Allow users to search tasks by title",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 24,
        "title": "Filter by Priority",
        "description": "Allow filtering tasks by priority",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 25,
        "title": "Filter by Status",
        "description": "Allow filtering tasks by task status",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 26,
        "title": "Sort Tasks",
        "description": "Implement ascending and descending task sorting",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 27,
        "title": "Implement Pagination",
        "description": "Split task results into multiple pages",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 28,
        "title": "Validate Task Data",
        "description": "Validate required fields when creating tasks",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 29,
        "title": "Validate Priority",
        "description": "Only allow low, medium and high priorities",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 30,
        "title": "Validate Status",
        "description": "Only allow valid task statuses",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 31,
        "title": "Learn API Security",
        "description": "Study common API security vulnerabilities",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 32,
        "title": "Study Authentication",
        "description": "Learn how API authentication works",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 33,
        "title": "Learn JWT",
        "description": "Study JSON Web Tokens for authentication",
        "priority": "high",
        "status": "in_progress"
    },
    {
        "id": 34,
        "title": "Implement Login",
        "description": "Create a login endpoint for users",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 35,
        "title": "Implement Registration",
        "description": "Create a user registration endpoint",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 36,
        "title": "Hash Passwords",
        "description": "Secure user passwords using password hashing",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 37,
        "title": "Learn Authorization",
        "description": "Understand permissions and access control",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 38,
        "title": "Protect API Routes",
        "description": "Require authentication for protected endpoints",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 39,
        "title": "Learn SQLAlchemy",
        "description": "Study ORM concepts using SQLAlchemy",
        "priority": "medium",
        "status": "in_progress"
    },
    {
        "id": 40,
        "title": "Create Task Model",
        "description": "Create a database model for tasks",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 41,
        "title": "Create User Model",
        "description": "Create a database model for users",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 42,
        "title": "Create Relationships",
        "description": "Connect users with their tasks",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 43,
        "title": "Test Authentication",
        "description": "Test login and protected API endpoints",
        "priority": "medium",
        "status": "pending"
    },
    {
        "id": 44,
        "title": "Test Authorization",
        "description": "Verify users can only access permitted tasks",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 45,
        "title": "Document API",
        "description": "Write documentation for API endpoints",
        "priority": "low",
        "status": "in_progress"
    },
    {
        "id": 46,
        "title": "Write API Tests",
        "description": "Create automated tests for API endpoints",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 47,
        "title": "Handle Invalid IDs",
        "description": "Return proper errors for nonexistent task IDs",
        "priority": "medium",
        "status": "completed"
    },
    {
        "id": 48,
        "title": "Improve Error Handling",
        "description": "Create consistent API error responses",
        "priority": "medium",
        "status": "in_progress"
    },
    {
        "id": 49,
        "title": "Deploy API",
        "description": "Deploy the task management API to a server",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 50,
        "title": "Review Project",
        "description": "Review the complete task management API",
        "priority": "low",
        "status": "pending"
    }
]
#fetch task by id
#using dynamic route
# @app.get("/api/v1/tasks/<int:id>")
# def get_task(id):
#     if id>len(tasks):
#         return jsonify({
#             "error":"Task not found"
#         }),404
#     for task in tasks:
#         if task["id"]==id:
#             return jsonify(task),200


#get task by query
if __name__=="__main__":
    app.run(debug=True)