# Dockerfile
# Dockerfile
FROM node:13.12.0-alpine

WORKDIR /app/frontend
COPY package.json /app/frontend
RUN npm install
COPY . /app/frontend
RUN npm run build
CMD ["npm", "start"]