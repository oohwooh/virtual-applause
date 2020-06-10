FROM python:3.7-slim-buster

RUN apt-get update && apt-get install ffmpeg -y

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY claps /app/claps
COPY crabs /app/crabs
COPY bot.py /app/bot.py
WORKDIR /app
CMD ["python3", "bot.py"]
