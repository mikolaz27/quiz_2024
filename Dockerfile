FROM python:3.12.2-slim

RUN apt update
RUN mkdir /quiz

WORKDIR /quiz

COPY ./src ./src
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip & pip install -r ./requirements.txt

CMD ["bash"]