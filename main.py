from fastapi import FastAPI, HTTPException, Query
from models import MenuItem, MenuResponse
from data import menu_items


app = FastAPI(title="Chai", description="Read only menu API")


@app.get("/")
def root():
    return {"message": "Welcome to Chai Point Menu API"}


@app.get("/menu", response_model=MenuResponse)
def get_menu(
    category: str | None = Query(None, description="Filter menu items by category"),
):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]
        if not filtered:
            raise HTTPException(
                status_code=404, detail=f"No item found in this category:{category}"
            )
        return MenuResponse(count=len(filtered), items=filtered)

    return MenuResponse(count=len(menu_items), items=menu_items)


@app.get("/menu/{item_id}", response_model=MenuItem)
def get_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404, detail=f"Menu item not found with this ID:{item_id}"
    )
