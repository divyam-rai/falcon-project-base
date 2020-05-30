FROM pypy:3-6
RUN mkdir -p /usr/src/app/logs
WORKDIR /usr/src/app
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y --force-yes supervisor
RUN mkdir -p /var/log/supervisor
COPY supervisor.conf /etc/supervisor/conf.d/supervisord.conf
COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 811
VOLUME /usr/src/app
CMD ["/usr/bin/supervisord"]