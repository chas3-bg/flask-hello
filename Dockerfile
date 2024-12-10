ARG PY_VER=3.13.0
FROM python:${PY_VER}-alpine

COPY ./requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
COPY ./app.py app.py
EXPOSE 5000
CMD python app.py

