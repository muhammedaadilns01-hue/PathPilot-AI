from fastapi import FastAPI

app = FastAPI( title="PathPilot AI",
              description="AI-powered career opportunity discovery platform",
              version="0.1.0")

@app.get("/health")
def health_check():
    return{
        "status":"healthy",
        "project":"PathPilot AI",
        "message":"Backend is running correctly and successfully!!!"
          }