FROM python:3.9.12-slim-bullseye
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD waitress-serve --port=$PORT app:app