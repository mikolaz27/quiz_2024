FROM python:3.11-rc-slim

RUN apt update
RUN python --version

RUN mkdir /docker_example

WORKDIR /docker_example

COPY ./hello_from_docker.py ./hello_docker.py
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip & pip install -r ./requirements.txt

CMD ["python", "hello_docker.py"]