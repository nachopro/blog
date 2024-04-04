FROM python:3.11-alpine

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && apk add --no-cache \
    bash \
    curl

RUN python -m venv $VIRTUAL_ENV && pip install --upgrade pip

COPY requirements/* ./
RUN pip install --no-cache-dir -r prod.txt

WORKDIR /opt/app
COPY blog/ ./
COPY entrypoint.sh ./

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
