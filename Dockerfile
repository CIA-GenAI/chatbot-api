# syntax = docker/dockerfile:1.4

FROM ubuntu:22.04 AS builder

ARG APT_FLAGS=" -q -y"

WORKDIR /chatbotapi

RUN apt update && apt install ${APT_FLAGS} python3-pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /chatbotapi

ENTRYPOINT uvicorn main:app --reload
