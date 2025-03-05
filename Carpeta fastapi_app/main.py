from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def get_info():
    return {
        "name": "Library System",
        "version": "1.0",
        "author": "diana-andres",
        "language": "Python",
        "framework": "FastAPI",
        "status": "Running"
    }