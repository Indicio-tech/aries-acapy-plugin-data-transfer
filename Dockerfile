FROM bcgovimages/von-image:py36-1.16-1 AS base

# Install and configure poetry
USER root

ENV POETRY_VERSION=1.1.11
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH="/opt/poetry/bin:$PATH"
RUN poetry config virtualenvs.in-project true

# Setup project
RUN mkdir acapy_plugin_data_transfer && touch acapy_plugin_data_transfer/__init__.py
COPY pyproject.toml poetry.lock README.md ./
ARG install_flags=--no-dev
RUN poetry install ${install_flags}
USER $user

FROM bcgovimages/von-image:py36-1.16-1
COPY --from=base /home/indy/.venv /home/indy/.venv
ENV PATH="/home/indy/.venv/bin:$PATH"
EXPOSE 80

COPY acapy_plugin_data_transfer/ acapy_plugin_data_transfer/

ENTRYPOINT ["/bin/bash", "-c", "aca-py \"$@\"", "--"]
