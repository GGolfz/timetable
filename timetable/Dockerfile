FROM node:lts-alpine as step01
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN npm install
RUN npm run build

FROM nginx:1.13.6
WORKDIR /usr/share/nginx/html
COPY --from=step01 /app/dist .
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]