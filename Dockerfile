FROM python:3.10-slim

# RUN apt install gcc libpq (no longer needed bc we use psycopg2-binary)
RUN apt update

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt
#
#
#
RUN mkdir -p /src
COPY src/ /src/
# RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src