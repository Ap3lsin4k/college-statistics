FROM python:3.10-slim

# RUN apt install gcc libpq (no longer needed bc we use psycopg2-binary)
RUN apt update

COPY requirements.txt /tmp/
RUN apt-get update && apt-get install -y --no-install-recommends \
    jq \
    python3-pip \
    python3-setuptools \
    netcat
#    python3.10 \

RUN pip3 install ipython ipykernel

COPY entrypoint.sh entrypoint.sh

# At runtime, mount the connection file to /tmp/connection_file.json
RUN pip install -r /tmp/requirements.txt
#
#
#
RUN mkdir -p /src
COPY src/ /src/
# RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src

ENTRYPOINT [ "./entrypoint.sh"]

