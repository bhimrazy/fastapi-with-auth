FROM python:3.11-alpine

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -U wheel setuptools
RUN pip install --no-cache-dir -r requirements.txt


# copy project
COPY . .
