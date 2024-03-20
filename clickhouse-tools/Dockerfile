FROM ethpandaops/debian-slim:latest

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install clickhouse-client and aws-cli (s3 binary)
RUN apt-get update && \
    apt-get install -y curl unzip gnupg2 software-properties-common && \
    curl -fsSL 'https://packages.clickhouse.com/rpm/lts/repodata/repomd.xml.key' | gpg --dearmor -o /usr/share/keyrings/clickhouse-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/clickhouse-keyring.gpg] https://packages.clickhouse.com/deb stable main" | tee \
        /etc/apt/sources.list.d/clickhouse.list && \
    apt-get update && \
    apt-get install -y clickhouse-client awscli jq

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*