FROM python:latest

WORKDIR /fastapi

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -U wheel setuptools
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy project
COPY . .
