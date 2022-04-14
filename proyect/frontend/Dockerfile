FROM node:12

RUN mkdir /frontend
WORKDIR /frontend
ADD . /frontend/

COPY package*.json ./

USER node

RUN npm install

COPY --chown=node:node . .

EXPOSE 8080

CMD [ "npm", "serve" ]