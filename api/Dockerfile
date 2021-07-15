FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

EXPOSE 80

WORKDIR /

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
