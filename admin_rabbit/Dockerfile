FROM rabbitmq:3.7-management

COPY rabbitmq.config /etc/rabbitmq/

COPY definitions-admin.json /etc/rabbitmq/

RUN chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.config /etc/rabbitmq/definitions-admin.json

CMD ["rabbitmq-server"]