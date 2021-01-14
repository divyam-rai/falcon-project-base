FROM python:3.6
RUN mkdir -p /usr/src/app/logs
WORKDIR /usr/src/app
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y --force-yes supervisor
RUN curl -L https://github.com/edenhill/librdkafka/archive/v0.11.6.tar.gz | tar xzf -
RUN cd librdkafka-0.11.6/ && ./configure --prefix=/usr && make -j && make install
RUN mkdir -p /var/log/supervisor
COPY supervisor.conf /etc/supervisor/conf.d/supervisord.conf
COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install confluent-kafka==1.4.1
EXPOSE 811
VOLUME /usr/src/app
CMD ["/usr/bin/supervisord"]