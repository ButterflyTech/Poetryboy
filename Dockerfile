FROM python:3.5.6-alpine

WORKDIR /usr/src/app

COPY ./src .

RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r ./requirements.prod

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]