FROM node:16 AS frontend

WORKDIR /frontend
COPY package*.json /frontend
RUN npm install

COPY . /frontend
RUN npm run development

FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=frontend /frontend/dist /usr/share/nginx/html