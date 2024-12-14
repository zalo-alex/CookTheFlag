FROM python:3.10-slim

RUN apt-get update

# Install NMap
RUN apt-get install -y nmap

# Install CookTheFlag
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]