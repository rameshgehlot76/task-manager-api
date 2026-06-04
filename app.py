from flask import Flask
from database import init_db
from routes import task_bp

app = Flask(__name__) 

# Initialize the database
init_db(app)

# Register routes
app.register_blueprint(task_bp)


@app.errorhandler(404)
def not_found(e):
    return {"error": "Route not found"}, 404


@app.errorhandler(405)
def method_not_allowed(e):
    return {"error": "Method not allowed"}, 405 


@app.errorhandler(500)
def server_error(e):
    return {"error": "Internal server error"}, 500


if __name__ == '__main__':
    app.run(debug=True)
    

