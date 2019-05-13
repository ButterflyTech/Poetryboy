FROM python:3.5.6-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache ffmpeg

COPY ./src .

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r ./requirements.prod