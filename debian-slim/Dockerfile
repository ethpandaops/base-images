FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y \
    awscli \
    curl \
    wget \
    net-tools \
    git \
    nano \
    vim \
    unzip \
    zip \
    ca-certificates \
    gnupg \
    software-properties-common && \
    rm -rf /var/lib/apt/lists/*