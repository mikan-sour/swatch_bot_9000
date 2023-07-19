# Stage 1: Build the Vite app
FROM node:16-alpine AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the entire app directory to the container
COPY . .

# Build the app
RUN npm run build

# Stage 2: Create a production-ready NGINX image
FROM nginx:latest

# Copy the built app from the previous stage to the NGINX static directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose the NGINX port (default is 80)
EXPOSE 80

# Start NGINX when the container is run
CMD ["nginx", "-g", "daemon off;"]