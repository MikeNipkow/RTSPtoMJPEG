FROM python:3

ENV TZ=Europe/Berlin

RUN useradd -ms /bin/bash app

RUN apt-get -y update

RUN apt-get install -y --fix-missing \
    libsm6 libxext6

USER app

WORKDIR /home/app/src

COPY --chown=app:app requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "main.py" ]
