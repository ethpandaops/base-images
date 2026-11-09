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

ARG TARGETARCH
ARG DOCKER_VERSION=29.9.2
ARG DOCKER_SHA256_AMD64=9ac225999fd5e863f7694c728ef23d480616b1e5639328fa309befd4243d69eb
ARG DOCKER_SHA256_ARM64=873b3e0207857c3b2f28392fb922f3ea6efe37620c16d4d4aaf2fef409c90b73
RUN case "$TARGETARCH" in \
      amd64) docker_arch=x86_64; docker_sha256="$DOCKER_SHA256_AMD64" ;; \
      arm64) docker_arch=aarch64; docker_sha256="$DOCKER_SHA256_ARM64" ;; \
      *) echo "Unsupported architecture: $TARGETARCH" >&2; exit 1 ;; \
    esac && \
    curl -fsSLo /tmp/docker.tgz \
      "https://download.docker.com/linux/static/stable/${docker_arch}/docker-${DOCKER_VERSION}.tgz" && \
    echo "${docker_sha256}  /tmp/docker.tgz" | sha256sum -c - && \
    tar -xzf /tmp/docker.tgz --strip-components=1 -C /usr/local/bin docker/docker && \
    rm /tmp/docker.tgz && \
    docker --version
