# 1. Use a lightweight web server image
FROM nginx:alpine

# 2. Remove default nginx static files
RUN rm -rf /usr/share/nginx/html/*

# 3. Copy our static site into nginx's serving directory
COPY . /usr/share/nginx/html

# 4. Expose port 80 inside the container
EXPOSE 80
