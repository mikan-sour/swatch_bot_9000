FROM python:3.7

ENV PYTHONPATH=.

COPY . .

EXPOSE 8080

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install toolz
RUN pip install psycopg2
RUN pip install boto3

CMD ["python", "src/main.py"]
