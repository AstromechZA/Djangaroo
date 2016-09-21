FROM ubuntu:14.04

# === PACKAGES =====================================================================================================
RUN     apt-get update &&\
        apt-get install -y python nginx wget &&\
        apt-get clean

# === PIP ==============================================================================================================
RUN     wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate &&\
        python get-pip.py &&\
        pip install --upgrade pip

# === INSTALL PYTHON DEPENDENCIES ======================================================================================
ADD     /web_src/requirements.txt /requirements.txt
RUN     pip install --upgrade -r /requirements.txt && rm /requirements.txt
RUN     pip install supervisor gunicorn

# === SETUP NGINX ======================================================================================================
RUN      rm -vrf /etc/nginx/sites-enabled/*
COPY     /container_src/config/nginx.conf /etc/nginx/sites-enabled/django-app.conf

# === SETUP SUPERVISORD ================================================================================================
COPY     /container_src/config/supervisord.conf /etc/supervisord.conf
RUN      mkdir -p /var/log/supervisor

# === COPY IN DJANGO APP ================================================================================================
COPY     /web_src/ /django_app/
RUN      rm -rfv /django_app/live && mkdir -p /django_app/live/static /django_app/live/logs

# === SETUP WWW USER ===================================================================================================
RUN      useradd -M -d /sbin www
RUN      mkdir -p /var/log/www
RUN      chown -R www:www /django_app /var/log/www

# === COPY IN RUN TIME SCRIPTS =========================================================================================
COPY     /container_src/scripts/init-django-app.sh /init-django-app.sh
COPY     /container_src/scripts/run-django-app.sh /run-django-app.sh
COPY     /container_src/scripts/store_app_vars /store_app_vars
RUN      chmod +x /init-django-app.sh /run-django-app.sh /store_app_vars

# === ADD EMPTY ENV VARS FILE ==========================================================================================
RUN      touch /django_app/overrides.env

# === PORTS ============================================================================================================
EXPOSE 80

# === ENTRYPOINT =======================================================================================================
CMD     ["sh", "-c", "/store_app_vars && chown -R www /django_app/live && exec supervisord -c /etc/supervisord.conf"]
