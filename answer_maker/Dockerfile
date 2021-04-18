FROM python:3.8-buster

ENV APP_HOME /app
ENV PROJECT_ID "corona-line-bot"
ENV TIMEZONE "Asia/Tokyo"
ENV LINE_ACCESS_TOKEN "***"
ENV LINE_CHANNEL_SECRET "***"
ENV DEBUG_MODE "True"
ENV GOOGLE_APPLICATION_CREDENTIALS './corona-line-bot-7e74b5375cca.json'
WORKDIR $APP_HOME

COPY . ./

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get install tk
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :8080 main:app
