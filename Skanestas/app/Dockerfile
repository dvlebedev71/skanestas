FROM python:latest
WORKDIR /code
RUN pip install psycopg2
RUN pip install python-dotenv
COPY app.py app.py
CMD ["python", "-u", "app.py"]

