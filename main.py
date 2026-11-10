from fastapi import FastAPI  # type: ignore[import-not-found]

app = FastAPI(title="Chai",
              description = "Read only menu API")

@app.get("/")
def root():
    return {"message":"Welcome to Chai Point Menu API"}