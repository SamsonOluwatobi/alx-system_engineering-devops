# Web Stack Debugging - Project 0

This project focuses on debugging a Docker container running Apache to serve a simple web page.

## Task Description

The goal is to ensure that Apache within the Docker container serves a page that contains "Hello Holberton" when queried at the root.

## Steps to Solve the Issue

1. *Run Docker Container:*

   Start the Docker container using the provided image and map port 80 inside the container to port 8080 on the host.

   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0

