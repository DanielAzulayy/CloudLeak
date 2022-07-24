FROM node:16

WORKDIR /app/src/app

COPY package*.json ./
RUN npm install

COPY . .
RUN [ "npm", "run", "hot" ]

FROM nginx:alpine
COPY --from=mix /use/src/app/dist /usr/share/nginx/html