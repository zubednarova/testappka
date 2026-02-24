from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.api_route("/", methods=["GET", "POST"])  # POST required for Keboola startup check
async def index():
    html = """
    <!DOCTYPE html>
    <html>
      <head><title>Hello App</title></head>
      <body style="font-family: sans-serif; padding: 2rem;">
        <h1>👋 Hello from Keboola Data Apps!</h1>
        <p>FastAPI is running successfully.</p>
      </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.get("/api/health")
async def health():
    return {"status": "ok"}
