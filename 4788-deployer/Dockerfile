FROM python:3.9.18-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT ["python", "send_tx.py"]