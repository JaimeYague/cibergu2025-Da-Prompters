# /app/server.py

import uvicorn
from fastapi import FastAPI
from .routers import tools, engines

app = FastAPI(title="PysingScan API")

# mount routers
app.include_router(tools.router)
app.include_router(engines.router)


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host="0.0.0.0",
        port=5000,
        workers=4,
        reload=True  # optional
    )
