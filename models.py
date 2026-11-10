from pydantic import BaseModel  # type: ignore[import-not-found]


class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    available: bool
    
    
class MenuResponse(BaseModel):
    status:str="success"
    count:int
    items:list[MenuItem]
        