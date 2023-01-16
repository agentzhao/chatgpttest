FROM python:3.11.1-slim-bullseye

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y git
RUN pip3 install -r requirements.txt
RUN playwright install firefox

# CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
CMD ["python3", "app.py"]
