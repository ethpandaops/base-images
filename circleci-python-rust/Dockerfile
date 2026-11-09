FROM cimg/python:3.12.4@sha256:7ae98e2a116140aa9e3d8f736a485cce0895b662d35683af768c21619ba201dc

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

LABEL maintainer="EthPandaOps <ethpandaops@ethereum.org>"

ENV PYENV_ROOT=/home/circleci/.pyenv \
	PATH=/home/circleci/.pyenv/shims:/home/circleci/.pyenv/bin:/home/circleci/.poetry/bin:$PATH \
	PYTHON_VERSION=3.12.4 \
	PIPENV_DEFAULT_PYTHON_VERSION=3.12.4

# Install Rust and Cargo
ARG TARGETARCH
ARG RUSTUP_VERSION=1.29.2
ARG RUST_VERSION=1.92.0
ARG RUSTUP_SHA256_AMD64=5be191e8c70a5007074254cb74d78dbfdd25cd5a61c27de7b8e5410122ec24f4
ARG RUSTUP_SHA256_ARM64=a9c168dbea81a84671c6b7a5c1795cb0eb699020110d107ddfca427bd797e697
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
ENV PATH="/home/circleci/.cargo/bin:$PATH"
