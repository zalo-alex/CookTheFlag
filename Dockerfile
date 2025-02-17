FROM python:3.10-slim

RUN apt-get update

# Install NMap
RUN apt-get install -y nmap

# Install NMap
RUN apt-get install -y hashcat

# Install CookTheFlag
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV DOCKER=1

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]