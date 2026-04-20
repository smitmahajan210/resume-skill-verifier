FROM node:20
WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build
CMD ["npm", "run", "start", "--", "-H", "0.0.0.0", "-p", "3000"]
