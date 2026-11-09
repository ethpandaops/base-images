FROM ethpandaops/debian-slim:latest@sha256:a197a83e7c74ad4bb137d5a9cd3ed9305fa12ff835e7e433d3f23dba46c6dfc1

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

ARG DEBIAN_SNAPSHOT=20261021T000000Z
ARG CLICKHOUSE_KEY_SHA256=74c1dfd89393b27c5739ee579a5af661ebe628cef9c33222c6fb29d0b8d42ad0
ARG CLICKHOUSE_VERSION=26.10.3.7

# Install clickhouse-client and aws-cli (s3 binary)
RUN rm -f /etc/apt/sources.list.d/debian.sources && \
    printf '%s\n' \
      "deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/${DEBIAN_SNAPSHOT} bookworm main" \
      "deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/${DEBIAN_SNAPSHOT} bookworm-updates main" \
      "deb [check-valid-until=no] http://snapshot.debian.org/archive/debian-security/${DEBIAN_SNAPSHOT} bookworm-security main" \
      > /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends curl unzip gnupg2 software-properties-common build-essential pkg-config libssl-dev && \
    curl -fsSLo /tmp/clickhouse-key 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' && \
    echo "${CLICKHOUSE_KEY_SHA256}  /tmp/clickhouse-key" | sha256sum -c - && \
    gpg --dearmor -o /usr/share/keyrings/clickhouse-keyring.gpg /tmp/clickhouse-key && \
    rm /tmp/clickhouse-key && \
    echo "deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg] https://packages.clickhouse.com/deb stable main" | tee \
        /etc/apt/sources.list.d/clickhouse.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends "clickhouse-client=${CLICKHOUSE_VERSION}" awscli jq python3 python3-pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --require-hashes --break-system-packages -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Rust, Cargo and cryo_cli
ARG TARGETARCH
ARG RUSTUP_VERSION=1.29.2
ARG RUST_VERSION=1.92.0
ARG RUSTUP_SHA256_AMD64=5be191e8c70a5007074254cb74d78dbfdd25cd5a61c27de7b8e5410122ec24f4
ARG RUSTUP_SHA256_ARM64=a9c168dbea81a84671c6b7a5c1795cb0eb699020110d107ddfca427bd797e697
ARG CRYO_REVISION=80eedf5355ca7b141d48123126515e6c9dd7d290
RUN case "$TARGETARCH" in \
      amd64) rust_arch=x86_64; rustup_sha256="$RUSTUP_SHA256_AMD64" ;; \
      arm64) rust_arch=aarch64; rustup_sha256="$RUSTUP_SHA256_ARM64" ;; \
      *) echo "Unsupported architecture: $TARGETARCH" >&2; exit 1 ;; \
    esac && \
    curl --proto '=https' --tlsv1.2 -fsSLo /tmp/rustup-init \
      "https://static.rust-lang.org/rustup/archive/${RUSTUP_VERSION}/${rust_arch}-unknown-linux-gnu/rustup-init" && \
    echo "${rustup_sha256}  /tmp/rustup-init" | sha256sum -c - && \
    chmod +x /tmp/rustup-init && \
    /tmp/rustup-init -y --profile minimal --default-toolchain "$RUST_VERSION" && \
    rm /tmp/rustup-init
ENV PATH="/root/.cargo/bin:$PATH"
RUN cargo install --git https://github.com/paradigmxyz/cryo \
    --rev "$CRYO_REVISION" --locked cryo_cli
