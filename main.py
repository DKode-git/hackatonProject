from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ALLOW ALL ORIGINS (Crucial for Hackathons)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows Netlify to call this API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is Live!"}