FROM python:3

WORKDIR /usr/src/app
COPY ./ /usr/src/app
RUN apt-get update ##[edited]
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'tesseract-ocr'\ 
    'libtesseract-dev'\ 
    'libxext6'  -y
RUN pip install --no-cache-dir -r requirements.txt