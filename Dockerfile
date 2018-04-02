FROM            petershan1119/eb-docker-practice-1:base
MAINTAINER      petershan0315@gmail.com

ENV             BUILD_MODE              production
ENV             DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

# source 폴더를 통째로 복사
COPY            . /srv/project

# nginx 설정파일을 복사 및 링크
RUN             cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf       /etc/nginx/nginx.conf &&\
                cp -f   /srv/project/.config/${BUILD_MODE}/nginx-app.conf   /etc/nginx/sites-available/ &&\
                rm -f   /etc/nginx/sites-enabled/* &&\
                ln -sf  /etc/nginx/sites-available/nginx-app.conf   /etc/nginx/sites-enabled/

# supervisor설정파일을 복사
RUN             cp -f   /srv/project/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/

# pkill nginx후 supervisor -n실행
CMD             pkill nginx; supervisord -n

# EB에서 프록시로 연결될 port를 열어줌
EXPOSE          80