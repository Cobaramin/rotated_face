FROM python:3.6-slim

RUN apt-get update && apt-get install -y gcc build-essential wget libglib2.0-0 libsm6 libxext6 libgtk2.0-dev

COPY . /code
WORKDIR /code

RUN pip install --upgrade pip
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-linux_x86_64.whl \
 && pip install torchvision
