FROM eclipse-temurin:17
RUN apt-get update && apt-get install -y \
    python3 python3-venv \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /hapi-run
COPY ./copy /
CMD ["hapi-run"]

