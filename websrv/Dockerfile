FROM delssajri/tornado
MAINTAINER Tatiana Drozdova <delssajri@gmail.com>
LABEL version="1.0" description="payserver websocket back"
COPY ./app /usr/src/app/
WORKDIR /usr/src/app
EXPOSE 8888
ENTRYPOINT ["python", "app.py"]

