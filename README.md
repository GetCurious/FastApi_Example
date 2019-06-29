## Python - FastApi FrameWork

- ORM: <b>SQLAlchemy</b>
- Server: <b>Uvicorn</b>
- Migration Tool: <b>Alembic</b>
- <b>Swagger UI & ReDoc</b>

#### Setup:
1. Install Python
2. `pip install -r requirements`
3. Create a postgres database
4. Change db route in `/alembic.ini` and `/app/database.py`


##### How to run:
1. `export PYTHONPATH=.`

2. `uvicorn app.main:app --reload`

3. "Hibernate" & "Seed" using `alembic upgrade head`

4. Browser `http://127.0.0.1:8000/docs/`

## Documentations 
https://fastapi.tiangolo.com/

## Full Example
https://github.com/tiangolo/full-stack-fastapi-postgresql
