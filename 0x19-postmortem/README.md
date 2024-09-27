### Postmortem: Web Stack Outage - August 18, 2024

## Issue Summary
#  Outage Duration: August 18, 2024, 01:00 AM - August 18, 2024, 03:30 AM (UTC)

* Impact: The primary web application was down for 2.5 hours. During this period, 85% of users experienced inability to access the site, resulting in approximately 50,000 users being unable to log in or access critical services.

# Root Cause: The issue stemmed from an expired SSL certificate on the load balancer, causing failed HTTPS connections.

## Timeline
    01:00 AM: The outage began. Monitoring alerts triggered as server logs indicated HTTPS handshake failures.
    01:05 AM: The DevOps engineer received an automated alert from Datadog regarding the downtime.
    01:10 AM: Initial investigation began, focusing on web servers, assuming a misconfiguration or service crash.
    01:30 AM: Misleading investigation led the team to restart Nginx services across all servers, assuming a proxy-related issue.
    02:00 AM: The escalation to the network team occurred when previous fixes failed.
    02:20 AM: Upon closer inspection, the SSL certificate on the load balancer was found to have expired.
    02:30 AM: Immediate resolution by renewing and applying a new SSL certificate.
    03:00 AM: Services restored, and further tests confirmed system stability.
    03:30 AM: Postmortem discussion initiated to prevent future occurrences.

## Root Cause and Resolution

# Root Cause: The SSL certificate on the load balancer expired without being automatically renewed. This caused all HTTPS traffic to be blocked since the web browsers could not verify the site’s security. The monitoring system did not have alerts for certificate expiration.

# Resolution: The certificate was manually renewed, and re-applied to the load balancer configuration. This immediately restored secure communication between users and the web servers.

## Corrective and Preventative Measures

# Improve SSL Monitoring:

    Implement automated monitoring for SSL certificate expiration using a service like Certbot, which sends alerts well before expiry.
    Add certificate expiration checks to daily system reports.

# Task List:
    Configure auto-renewal for SSL certificates on all load balancers.
    Ensure SSL expiration alerts are integrated into Datadog or another monitoring platform.
    Perform regular load balancer configuration checks during routine maintenance.

## Conclusion
    This outage highlighted the need for better SSL certificate management and monitoring. Moving forward, proactive measures will be implemented to ensure no such issue recurs, impacting uptime and customer experience.

