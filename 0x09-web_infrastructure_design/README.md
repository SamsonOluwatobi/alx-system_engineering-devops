### Web Infrastructure Design Project
## Project Overview
This project involves designing a secure, scalable, and monitored web infrastructure for the website www.foobar.com. The goal is to ensure high availability, load distribution, and secure communication, while also monitoring the performance and health of the infrastructure.

# Requirements
Three Servers:

# Server 1: Web Server (Nginx)
# Server 2: Application Server
# Server 3: Database Server (MySQL)

## Load Balancers:

# HAProxy 1: Primary load balancer

## Firewalls:

Each server is protected by its own firewall.
SSL Certificate:

To serve www.foobar.com over HTTPS for secure communication.

## Monitoring Clients:

Collect data and send it to a centralized monitoring service like Sumologic.
