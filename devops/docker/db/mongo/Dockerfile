FROM postgres:9.5.12
LABEL CIA GenAI <cia-genai@support.org>

#ADD ./postgre-init-files /docker-entrypoint-initdb.d
ENV POSTGRES_USER=chatbot
ENV POSTGRES_PASSWORD=chatbot
ENV POSTGRES_DB=chatbot
EXPOSE 5432
CMD ["postgres"]


#  postgresdb:
#    container_name: chatbotdb_postgresql
#    image: "postgres:9.5.12"
#    restart: always
#    environment:
#      - POSTGRES_USER=chatbot
#      - POSTGRES_PASSWORD=loop hams less curd vest tilt
#      - POSTGRES_DB=chatbot
#    ports:
#      - 5432:5432
#    networks:
#      - markai-net