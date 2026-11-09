FROM python:3.11-alpine@sha256:5fb4bc53dd0180955e31e5245b648bbb24a4ac4ab03a1de81513642325220bcd
WORKDIR /app
COPY . /app
RUN pip install --require-hashes -r requirements.txt
