# FinAuditSystem

FinAuditSystem is a web application designed to streamline auditing processes for financial institutions. It offers a personalized dashboard with various charts based on audit logs, internal controls, and risk assessments. This README provides instructions for installation, usage, system details, and expectations.
![Sample](./images/risk_assessment_chart.png)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [System Overview](#system-overview)
- [System Details and Expectations](#system-details-and-expectations)
  - [Automated Auditing and Classification](#1-automated-auditing-and-classification)
  - [Data Security and Privacy](#2-data-security-and-privacy)
  - [Third-Party Auditor (TPA) Functions](#3-third-party-auditor-tpa-functions)
  - [Risk Assessment and Management](#4-risk-assessment-and-management)
  - [User Collaboration and Discussion](#5-user-collaboration-and-discussion)
  - [Organizational Information Management](#6-organizational-information-management)
  - [System Efficiency and Reliability](#7-system-efficiency-and-reliability)
  - [User-Friendly Interface](#8-user-friendly-interface)
  - [Compliance and Accuracy](#9-compliance-and-accuracy)
- [Charts](#charts)
- [Sample Output Images](#sample-output-images)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/FinAuditSystem.git

   ```
2. Change into the project directory:

   ```bash
   cd FinAuditSystem
   ```
3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
7. Run the development server:

   ```bash
   python manage.py runserver
   ```
8. Open the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. Sign up for a new account or log in if you already have one.
2. Access the personalized dashboard by clicking on the "Dashboard" link in the navigation menu.
3. Explore various charts, including audit log counts, internal controls distribution, risk assessment timeline, and an impact vs. likelihood scatter plot.

## System Overview

The "FinAuditSystem" is designed to achieve the following objectives:

### 1. Automated Auditing and Classification:

- **Objective:**

  - Implement a robust system for automated auditing and classification processes tailored for financial institutions.
- **Expected Results:**

  - Streamlined and efficient auditing procedures that minimize manual intervention.
  - Accurate classification of data and transactions for improved financial management.

### 2. Data Security and Privacy:

- **Objective:**

  - Ensure the security and privacy of sensitive financial data stored and processed by the system.
- **Expected Results:**

  - Implementation of secure authentication mechanisms to control access to the system.
  - Encryption of sensitive data to prevent unauthorized access or tampering.

### 3. Third-Party Auditor (TPA) Functions:

- **Objective:**

  - Leverage the TPA to conduct regular checks on the integrity and availability of delegated data.
- **Expected Results:**

  - Periodic sampling audits conducted by TPA to verify the integrity and availability of outsourced data.
  - Support for dynamic data operations for authorized applications, ensuring consistency and reliability.

### 4. Risk Assessment and Management:

- **Objective:**

  - Implement a risk assessment mechanism to identify and manage risks associated with the financial environment.
- **Expected Results:**

  - Identification and analysis of relevant risks to the achievement of objectives.
  - Mechanisms in place for managing and mitigating risks associated with economic, industry, regulatory, and operating conditions.

### 5. User Collaboration and Discussion:

- **Objective:**

  - Facilitate collaboration and communication among users through a discussion forum.
- **Expected Results:**

  - A platform for users to engage in discussions on audit reviews, key control activities, and system-related topics.
  - Enhanced communication and information exchange within the system.

### 6. Organizational Information Management:

- **Objective:**

  - Manage and store information related to the organizational/company's internal controls, corporate governance, and accounting processes.
- **Expected Results:**

  - Availability of comprehensive organizational information for auditing purposes.
  - Efficient storage and retrieval of data related to corporate governance practices and accounting processes.

### 7. System Efficiency and Reliability:

- **Objective:**

  - Develop a system that is reliable, efficient, and capable of handling the auditing needs of a financial institution.
- **Expected Results:**

  - Reliable and consistent audit results.
  - Efficient handling of data operations and verification processes.

### 8. User-Friendly Interface:

- **Objective:**

  - Provide a user-friendly interface for ease of use and accessibility.
- **Expected Results:**

  - Intuitive user interface design that allows users to navigate the system with ease.
  - Clear presentation of audit results and relevant information.

### 9. Compliance and Accuracy:

- **Objective:**

  - Ensure compliance with industry standards and regulations.
- **Expected Results:**

  - Accuracy in audit results and adherence to relevant financial regulations.
  - Systematic compliance checks and reporting mechanisms.

By meeting these expectations, the "FinAuditSystem" aims to be a comprehensive and effective tool for auditing and classifying financial data in a secure and efficient manner.

## Charts

### 1. Audit Log Chart

Displays the number of audit logs for each action.

### 2. Internal Control Chart

Visualizes the distribution of internal controls.

### 3. Risk Assessment Chart

Shows the timeline of risk assessments with random data.

### 4. Scatter Plot

Presents an impact vs. likelihood scatter plot with randomly generated data.

## Sample Output Images

### Audit Log Chart and Internal Control Chart

![Audit Log Chart](./images/audit_log_chart.png)

### Risk Assessment Chart

![Risk Assessment Chart](./images/risk_assessment_chart.png)

### Scatter Plot

![Scatter Plot](./images/scatter_plot.png)


