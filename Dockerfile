FROM python:3.4-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

# ENV http_proxy 127.0.0.1:80
# ENV https_proxy 127.0.0.1:80

ENV FLASK_APP flaskr
ENV FLASK_ENV development

CMD ["flask", "init-db"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
# CMD ["python", "flaskr/__init__.py"]
