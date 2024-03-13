# Stori Challenge: Transaction Processing System

## Introduction
This document provides an overview of the Stori Challenge, a sample exercise aimed at demonstrating the design and implementation of a transaction processing system. The challenge involves processing transaction data from a CSV file, performing analysis, and sending summary reports via email.

## Architecture Overview

### The architecture of the Stori Challenge consists of several components:

Main Script (main.py): This script serves as the entry point of the application. It orchestrates the processing of transaction data, generates summary reports, and sends them via email.

Transaction Processing Module: Responsible for reading transaction data from a CSV file, processing it, and storing it in a database. This module includes functions for parsing CSV data, calculating transaction statistics, and saving data to a database.

Database (SQLite): A lightweight relational database used for storing transaction data. SQLite was chosen for its simplicity and ease of use, making it suitable for small-scale applications like this one.

Email Sending Module: Handles the sending of summary reports via email. This module uses the Simple Mail Transfer Protocol (SMTP) to send emails and includes functions for composing and sending emails.

### Selection of SQLite for Database Storage
SQLite was chosen as the database management system due to its simplicity, portability, and low overhead. SQLite stores the entire database in a single file, making it easy to manage and deploy. Additionally, SQLite is well-supported in Python and requires no separate server process, making it suitable for embedding in small applications.

### Dockerization for Containerization
The application is containerized using Docker to ensure consistency and portability across different environments. Docker allows the application and its dependencies to be packaged into a single container, making it easy to deploy and run on any platform that supports Docker.

Step-by-Step Guide
Follow these steps to set up and run the Stori Challenge:

Clone the Repository: Clone the Stori Challenge repository to your local machine:
```
git clone https://github.com/dederico/stori.git
cd stori_challenge
```
Create Directories: Create the necessary directories for the project:
```
mkdir src
cd src
```

Create Transaction Data File: Create a transactions.csv file inside the src directory and populate it with transaction data:
```
touch transactions.csv
```

Write Transaction Data: Open the transactions.csv file in a text editor and write transaction data in the following format:
```
Id,Date,Transaction
0,7/15,+60.5
1,7/28,-10.3
2,8/2,-20.46
3,8/13,+10
```

Create Python Scripts: Create the following Python scripts inside the src directory:

main.py: This script serves as the entry point of the application. It orchestrates the processing of transaction data, generates summary reports, and sends them via email.

create_db.py: This script contains functions to create the SQLite database schema and tables for storing transaction data.

save_transaction_to_db.py: This script contains functions to save transaction data to the SQLite database.

email_utils.py: This script contains functions for composing and sending emails.

Write Python Scripts: Open each Python script in a text editor and write the necessary code. You can refer to the provided sample code or implement your own logic.

Build Docker Image: Build the Docker image using the provided Dockerfile:
```
docker build -t stori .
```

Run the Docker Container: Run the Docker container to execute the main.py script:
```
docker run stori
```

View Output: Check the console output for summary reports and any error messages.
Email: change the email address that responds to the summary_email attribute on the main.py file, to your email address, and expect the output message to be sent as long as you add a gmail account.

By following these steps, you can set up and run the Stori Challenge application to process transaction data, generate summary reports, and send them via email.