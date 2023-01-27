FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install python-dotenv
COPY app.py app.py
CMD ["python", "-u", "app.py"]

