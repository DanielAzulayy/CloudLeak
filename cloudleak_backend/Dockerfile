FROM python:3.10

LABEL maintainer="Daniel Azulay <serializator@gmail.com>"

WORKDIR /backend
ENV FLASK_APP="cloudleak.app"
ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_ENV=development
COPY requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["flask", "run"]