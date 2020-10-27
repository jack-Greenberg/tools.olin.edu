# Ubuntu image with poetry and some useful applications installed
FROM jackgreenberg/poetry:latest as base
MAINTAINER Jack Greenberg <jgreenberg@olin.edu>

ARG AZURE_TENANT_ID
ARG AZURE_APPLICATION_ID
ARG AZURE_CLIENT_SECRET

ENV PIP_DISABLE_PIP_VERSION=on \
    POETRY_VERSION=1.0.10 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

RUN apt update && apt-get install --no-install-recommends --no-install-suggests -y \
    postgresql-client \
    libpq-dev

FROM base as dependencies
WORKDIR /tools
COPY pyproject.toml poetry.lock ./
RUN ["poetry", "install", "--no-root"]


FROM base as final

COPY --from=dependencies /usr/local/bin /usr/local/bin
COPY --from=dependencies /usr/local/lib/python3.7/dist-packages/ /usr/local/lib/python3.7/dist-packages/

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /tools
COPY . /tools

RUN ["poetry", "install"]

CMD ["/tools/scripts/entrypoint.sh"]
