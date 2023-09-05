FROM postgres:9.5.12
LABEL CIA GenAI <cia-genai@support.org>

#ADD ./postgre-init-files /docker-entrypoint-initdb.d
ENV POSTGRES_USER=chatbot
ENV POSTGRES_PASSWORD=chatbot
ENV POSTGRES_DB=chatbot
EXPOSE 5432
CMD ["postgres"]
