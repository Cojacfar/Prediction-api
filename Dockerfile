FROM ubuntu:latest
LABEL Author="Cody Farmer"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]