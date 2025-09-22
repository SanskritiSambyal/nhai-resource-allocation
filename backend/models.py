from pydantic import BaseModel
from typing import List, Optional

class Project(BaseModel):
    project_name: str
    project_id: str
    location: str
    project_type: str
    start_date: str
    duration_days: int
    priority: Optional[str] = None
    budget: Optional[float] = None

class SiteConditions(BaseModel):
    terrain: Optional[str] = None
    soil_type: Optional[str] = None
    climate: Optional[str] = None
    expected_rainfall: Optional[float] = None
    extreme_weather: Optional[List[str]] = None
    seismic_zone: Optional[str] = None
    drainage_conditions: Optional[str] = None

class Manpower(BaseModel):
    role: str
    count: int
    shift_hours: Optional[int] = 8

class Machinery(BaseModel):
    type: str
    quantity: int
    maintenance_schedule: Optional[str] = None
    rental_cost: Optional[float] = None

class Material(BaseModel):
    type: str
    quantity: float
    unit: Optional[str] = None
    lead_time_days: Optional[int] = None
    storage_capacity: Optional[float] = None

class ResourceAllocationRequest(BaseModel):
    project: Project
    site_conditions: Optional[SiteConditions] = None
    manpower: Optional[List[Manpower]] = None
    machinery: Optional[List[Machinery]] = None
    materials: Optional[List[Material]] = None
