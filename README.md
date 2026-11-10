# Chai Menu API

A small read-only REST API for a chai menu, built with [FastAPI](https://fastapi.tiangolo.com/).

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

The API runs at http://127.0.0.1:8000. Interactive docs (Swagger UI) are at http://127.0.0.1:8000/docs.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Welcome message |
| GET | `/menu` | List all menu items. Optional `?category=chai` filter (case-insensitive) |
| GET | `/menu/{item_id}` | Get a single menu item by ID |

Unknown categories or IDs return `404`.

### Example

```bash
curl http://127.0.0.1:8000/menu/1
```

```json
{
  "id": 1,
  "name": "Masala Chai",
  "description": "Classic Indian spiced tea",
  "price": 30.0,
  "category": "chai",
  "available": true
}
```

`GET /menu` returns:

```json
{ "status": "success", "count": 10, "items": [ ... ] }
```

## Project structure

- `main.py` - FastAPI app and routes
- `models.py` - Pydantic models (`MenuItem`, `MenuResponse`)
- `data.py` - in-memory menu data
- `requirements.txt` - dependencies

## Note

Prices are in ₹ and are currently placeholder values.
