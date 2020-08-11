# Ubuntu image with poetry and some useful applications installed
FROM jackgreenberg/poetry:latest as dependencies
MAINTAINER Jack Greenberg <jgreenberg@olin.edu>

ENV PIP_DISABLE_PIP_VERSION=on \
    POETRY_VERSION=1.0.10 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

RUN apt-get install --no-install-recommends --no-install-suggests -y \
    postgresql-client \
    libpq-dev

WORKDIR /tools
COPY pyproject.toml poetry.lock ./
RUN ["poetry", "install", "--no-root"]


FROM jackgreenberg/poetry:latest as final

COPY --from=dependencies /usr/local/bin /usr/local/bin
COPY --from=dependencies /usr/local/lib/python3.7/dist-packages/ /usr/local/lib/python3.7/dist-packages/

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /tools
COPY . /tools

RUN ["poetry", "install"]

CMD ["/tools/scripts/entrypoint.sh"]
