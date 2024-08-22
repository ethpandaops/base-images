FROM ethpandaops/debian-slim:latest

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install clickhouse-client and aws-cli (s3 binary)
RUN apt-get update && \
    apt-get install -y curl unzip gnupg2 software-properties-common build-essential && \
    curl -fsSL 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' | gpg --dearmor -o /usr/share/keyrings/clickhouse-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg] https://packages.clickhouse.com/deb stable main" | tee \
        /etc/apt/sources.list.d/clickhouse.list && \
    apt-get update && \
    apt-get install -y clickhouse-client awscli jq python3 python3-pip

RUN pip3 install pandas pyarrow --break-system-packages

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Rust, Cargo and cryo_cli
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN echo "export PATH=/root/.cargo/bin:$PATH" >> /root/.bashrc
RUN /root/.cargo/bin/cargo install cryo_cli
