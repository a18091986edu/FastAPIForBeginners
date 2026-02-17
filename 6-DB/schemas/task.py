from pydantic import BaseModel, ConfigDict

class STaskBase(BaseModel):
    name: str
    description: str | None = None
    is_completed: bool = False

class STaskAdd(STaskBase):
    pass

class STask(STaskBase):
    id: int

    model_config = ConfigDict(from_attributes=True) # говорим pydantic, что мы хотим читать не только словари, но и объекты через точку task.id




