FROM python:3.12-alpine


WORKDIR /app

COPY requirements.txt /app/
RUN pip install --require-hashes --no-deps -r requirements.txt --upgrade pip 
COPY src/ /app/src/

WORKDIR /app/src

CMD ["sh" , "-c", "alembic upgrade head && python -m uvicorn main:app --host=0.0.0.0 --port=8000"]
