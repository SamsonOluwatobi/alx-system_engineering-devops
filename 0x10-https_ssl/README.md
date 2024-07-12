# HAproxy SSL Termination with Let's Encrypt

This project demonstrates how to configure HAproxy to handle SSL termination and redirect HTTP traffic to HTTPS. It also includes handling Let's Encrypt HTTP-01 challenges for SSL certificate issuance and renewal.

## Prerequisites

- Ubuntu server
- HAproxy 1.5 or higher
- Certbot

## HAproxy Configuration

### Configuration File

Update your HAproxy configuration file `/etc/haproxy/haproxy.cfg` with the following content:


