FROM python
RUN pip3 install flask
RUN pip3 install requests

CMD python consumer.py runserver 0.0.0.0:${CONSUMER_PORT}