FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/index.html
COPY ./VLAD-ma111in/. /usr/share/nginx/html/
#