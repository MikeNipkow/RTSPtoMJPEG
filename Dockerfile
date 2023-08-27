FROM python:3

ENV TZ=Europe/Berlin

RUN useradd -ms /bin/bash app

RUN apt-get -y update

USER app

WORKDIR /home/app/src

COPY --chown=app:app requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "main.py" ]
