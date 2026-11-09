FROM debian:bookworm-slim@sha256:7ff6ba31527b9e336162fa061746c366c4b2032f4d2cff2078bea43f78efe3f8

ARG DEBIAN_SNAPSHOT=20261021T000000Z

RUN rm -f /etc/apt/sources.list.d/debian.sources && \
    printf '%s\n' \
      "deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/${DEBIAN_SNAPSHOT} bookworm main" \
      "deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/${DEBIAN_SNAPSHOT} bookworm-updates main" \
      "deb [check-valid-until=no] http://snapshot.debian.org/archive/debian-security/${DEBIAN_SNAPSHOT} bookworm-security main" \
      > /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
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
