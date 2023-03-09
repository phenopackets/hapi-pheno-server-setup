FROM eclipse-temurin:17-jammy
RUN apt-get update && apt-get install -y \
    python3 python3-venv \
    unzip \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /hapi
COPY ./copy /
CMD ["hapisetup-hapi-run"]

