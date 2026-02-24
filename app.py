from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.api_route("/", methods=["GET", "POST"])
async def index():
    return PlainTextResponse("Hello World")
