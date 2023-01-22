FROM python:3.10

WORKDIR /domaingen

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./domaingen ./domaingen

CMD ["python", "./domaingen/main.py"]