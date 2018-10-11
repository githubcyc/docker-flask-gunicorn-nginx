
from app import create_app
# https://flask-restful.readthedocs.io/en/latest/

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)