# syntax=docker/dockerfile:1
FROM node:16

WORKDIR /app

# installs dependencies for frontend
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install

COPY . .

CMD [ "npm", "run", "hot" ]