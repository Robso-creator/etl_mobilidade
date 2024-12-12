FROM python:3.12-bookworm

RUN apt update && \
    apt install --yes locales && \
    apt clean

RUN echo "en_US.UTF-8 UTF-8\npt_BR.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen

RUN mkdir /opt/app
WORKDIR /opt/app

RUN mkdir -p /src/

COPY requirements/requirements.txt requirements/requirements.txt

RUN pip install -r requirements/requirements.txt

COPY src/ src/
CMD ["tail", "-f", "/dev/null"]
