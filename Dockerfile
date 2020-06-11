FROM python:3.7-slim-buster

RUN apt-get update && apt-get install ffmpeg -y

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY cogs /app/cogs
COPY templates /app/templates
COPY audio /app/audio
COPY bot.py /app/bot.py
COPY audio.py /app/audio.py
WORKDIR /app
CMD ["python3", "bot.py"]
