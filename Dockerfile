FROM python:2.7
MAINTAINER Adam Lavie, adam.lavie@gmail.com

WORKDIR /home
EXPOSE 8080

RUN echo cloning news-cast flask application from github.. && \
    git clone https://github.com/adamlavie/News-Cast.git && \
    echo installing news-cast flask application dependencies.. && \
    pip install News-Cast/

CMD python News-Cast/rest_service/resources.py