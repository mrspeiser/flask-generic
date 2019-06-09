FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y software-properties-common python3-pip python3.7
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]
