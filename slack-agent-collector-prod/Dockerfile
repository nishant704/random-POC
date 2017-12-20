FROM alpine:3.5
RUN apk update \
    python \
    cron \
    && apk add --update py-pip
WORKDIR /usr/src/app
COPY agent-collector-slackbot.py ./
RUN echo "0 23 * * * python /usr/src/app/agent-collector-slackbot.py >> /usr/src/app/cron.log" >> /etc/crontabs/root
RUN chmod 777 /usr/src/app/agent-collector-slackbot.py
RUN pip install requests
#CMD [ "python", "./agent-collector-slackbot.py" ]
RUN touch /usr/src/app/cron.log
CMD crond && tail -f /usr/src/app/cron.log
