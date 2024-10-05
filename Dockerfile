FROM nginx:1.27.1-bookworm

RUN apt-get update && apt-get install -y tree vim python3 python3-pip python3-venv locales-all supervisor
RUN python3 -m venv /opt/threat_map

COPY map/ /opt/threat_map/map/
COPY post/ /opt/threat_map/post/
COPY threat_map/ /opt/threat_map/threat_map/
COPY db.sqlite3 /opt/threat_map/
COPY manage.py /opt/threat_map/
COPY requirements.txt /opt/threat_map/
COPY .env /opt/threat_map/
COPY default.conf /etc/nginx/conf.d/default.conf
COPY supervisord.conf /etc/supervisor/conf.d/

RUN cd /opt/threat_map/ && . bin/activate && pip install -r requirements.txt && python3 manage.py collectstatic && deactivate
RUN mkdir /opt/threat_map/log/ && touch /opt/threat_map/log/supervisord.log && touch /opt/threat_map/log/nginx.log && chmod 777 /opt/threat_map/log/nginx.log && touch /opt/threat_map/log/gunicorn.log && chmod 777 /opt/threat_map/log/gunicorn.log

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
