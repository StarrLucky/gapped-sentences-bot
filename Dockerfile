FROM python:3.9 

WORKDIR /wordeli/

RUN apt-get update 
RUN apt-get -y install cron nano

COPY wordeli.py ./
COPY requirements.txt ./
COPY wordeli_dict wordeli_dict/
COPY config.py ./
COPY run.py ./
COPY send.py ./
COPY git_repo.py ./

RUN pip install -r requirements.txt

RUN touch /var/log/cron.log

RUN (crontab -l ; echo "0 6,9,12,13,15 * * * cd /wordeli/ && /usr/local/bin/python run.py >> /var/log/cron.log 2>&1") | crontab

CMD cron; tail -f /var/log/cron.log