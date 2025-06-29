FROM python:3.12-slim

RUN apt-get update

# Install NMap
RUN apt-get install -y nmap

# Install Hashcat
RUN apt-get install -y hashcat

# Install WHOIS
RUN apt-get install -y whois

# Install CookTheFlag
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run CookTheFlag
ENV DOCKER=1
EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]