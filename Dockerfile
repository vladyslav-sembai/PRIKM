FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/index.html
COPY ./VLAD-main/. /usr/share/nginx/html/
