FROM python:3.8

WORKDIR /usr/src/app

COPY web-app-requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./model ./model
COPY ./templates ./templates
COPY ./static ./static

COPY app.py ./app.py
COPY src .

EXPOSE 5000

ENV FLASK_APP=app.py
CMD [ "python", "-m", "flask", "run" ]
