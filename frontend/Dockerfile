FROM node:15.14-alpine3.10

WORKDIR /frontend

COPY package.json package-lock.json ./

RUN npm i

COPY . .
