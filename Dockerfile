FROM python:3.9

COPY . /code
RUN python -m pip install --upgrade pip && pip install -r /code/config/requirements.txt