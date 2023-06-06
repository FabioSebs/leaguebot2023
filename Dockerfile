FROM python:3.11.0b1-alpine
WORKDIR /bot
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "./main.py" ]

