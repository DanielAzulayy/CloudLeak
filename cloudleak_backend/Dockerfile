FROM python:3.9-slim-buster as app
LABEL maintainer="Daniel Azulay <serializator@gmail.com>"

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY . /app

RUN pip3 install -r requirements.txt

ENV FLASK_DEBUG=1 \
    FLASK_APP="cloudleak.app" \
    FLASK_SKIP_DOTENV="true" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    USER="python"

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]