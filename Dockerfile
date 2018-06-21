FROM ubuntu:latest
LABEL Author="Cody Farmer"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /Prediction-api
WORKDIR /Prediction-api
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]