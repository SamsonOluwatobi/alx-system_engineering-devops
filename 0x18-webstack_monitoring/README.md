# Datadog Monitoring Setup

## Project Overview
This project involves setting up monitors within Datadog to track system metrics, specifically the number of read and write requests issued to a device per second. These monitors help in assessing the system's performance and determining when scaling is necessary.

## Features
- **Read Requests Per Second Monitor**: Tracks the number of read requests issued to the device per second and triggers an alert if it exceeds the defined threshold.
- **Write Requests Per Second Monitor**: Monitors the number of write requests per second and alerts when the count surpasses the set threshold.
- **Customizable Alerts**: Alerts can be customized to meet the specific needs of your infrastructure.

## Prerequisites
- **Datadog Account**: Ensure you have a Datadog account with the necessary permissions to create monitors and dashboards.
- **Datadog Agent**: The Datadog Agent must be installed and running on the devices you want to monitor. Refer to the [Datadog Agent Installation Guide](https://docs.datadoghq.com/agent/) for setup instructions.

## Setup Instructions

### Step 1: Install Datadog Agent
1. Follow the official [Datadog Agent installation guide](https://docs.datadoghq.com/agent/) to install the agent on your devices.

### Step 2: Set Up Monitors in Datadog
1. Log in to your Datadog account.
2. Navigate to **Monitors** > **New Monitor**.
3. Set up the following monitors:
   - **Read Requests Per Second**: Use the `system.io.r_s` metric to track read requests.
   - **Write Requests Per Second**: Use the `system.io.w_s` metric to monitor write requests.
4. Customize the alert conditions and notifications according to your needs.
5. Save the monitors.

### Step 3: Create a Dashboard (Optional)
1. Navigate to **Dashboards** > **New Dashboard**.
2. Add relevant widgets to visualize the `system.io.r_s` and `system.io.w_s` metrics.
3. Save the dashboard and note the **Dashboard ID** for future reference.

## Usage
- **Monitoring**: The configured monitors will automatically track read and write requests per second. Alerts will be triggered based on the defined thresholds.
- **Notifications**: Notifications will be sent to the specified channels (e.g., email, Slack) when an alert condition is met.

## Example Monitor Messages
Here are the monitor messages used in this project:

### Read Requests Per Second Monitor Message
```plaintext
Alert: High Number of Read Requests Per Second Detected

Description: This monitor tracks the number of read requests issued to the device per second. 

Threshold: The monitor will trigger when the number of read requests exceeds 100 requests/second.

Impact: A high number of read requests might indicate heavy I/O operations, which could lead to increased latency or potential bottlenecks in the system.

Next Steps: Investigate the processes causing the high read requests. Consider scaling your resources or optimizing the read operations if necessary.

For more details, view the associated dashboard here: [Link to Dashboard](https://app.datadoghq.com/dashboard/pm7-wsk-xn2)
