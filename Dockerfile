FROM python:3.12-slim

LABEL maintainer="Bilal Asim"
LABEL description="taskcli - a tiny command-line task tracker"

WORKDIR /app

COPY taskcli.py .

# Store the data file at a fixed path we can mount a volume onto
RUN mkdir /data
ENV TASKS_FILE=/data/tasks.json

# ENTRYPOINT makes the container behave like the tool itself:
# args after `docker run <image>` become args to taskcli
ENTRYPOINT ["python3", "/app/taskcli.py"]
