from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from allocation import allocate_resources_claude

app = FastAPI(title="NHAI Resource Allocation API")

# Enable CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ProjectRequest(BaseModel):
    project: dict

@app.post("/allocate_resources")
async def allocate_resources_endpoint(request: ProjectRequest):
    result = allocate_resources_claude(request.dict())
    return result
