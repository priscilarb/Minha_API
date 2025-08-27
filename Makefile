<<<<<<< HEAD
run:
	@uvicorn dio_fastapi_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
=======
run:
	@uvicorn dio_fastapi_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
>>>>>>> 275c1638309bad2a7978f205f40b4ec50f66f75b
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head