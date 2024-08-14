FROM cimg/python:3.12.4

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

LABEL maintainer="EthPandaOps <ethpandaops@ethereum.org>"

ENV PYENV_ROOT=/home/circleci/.pyenv \
	PATH=/home/circleci/.pyenv/shims:/home/circleci/.pyenv/bin:/home/circleci/.poetry/bin:$PATH \
	PYTHON_VERSION=3.12.4 \
	PIPENV_DEFAULT_PYTHON_VERSION=3.12.4

# Update apt sources
RUN sudo apt-get update && sudo apt upgrade -y

RUN sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

# Install Rust, Cargo and cryo_cli
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN echo "export PATH=/root/.cargo/bin:$PATH" >> /root/.bashrc


