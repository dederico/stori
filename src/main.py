import csv
from datetime import datetime
from collections import defaultdict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from save_transaction_to_db import save_transaction_to_database
from email_utils import send_email
import os


def process_transactions(file_path):
    total_balance = 0
    num_transactions_by_month = defaultdict(int)
    total_debit_by_month = defaultdict(float)
    total_credit_by_month = defaultdict(float)

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transaction_date = datetime.strptime(row['Date'], '%m/%d')
            month_year = transaction_date.strftime('%B %Y')
            amount = float(row['Transaction'])
            if amount > 0:
                total_credit_by_month[month_year] += amount
            else:
                total_debit_by_month[month_year] += amount
            total_balance += amount
            num_transactions_by_month[month_year] += 1
            save_transaction_to_database(row['Id'], row['Date'], row['Transaction'])

    return total_balance, num_transactions_by_month, total_debit_by_month, total_credit_by_month

def generate_summary_email(total_balance, num_transactions_by_month, total_debit_by_month, total_credit_by_month):
    summary_email = f"Total balance is {total_balance}\n"
    for month, count in num_transactions_by_month.items():
        summary_email += f"Number of transactions in {month}: {count}\n"
    average_debit = sum(total_debit_by_month.values()) / len(total_debit_by_month)
    average_credit = sum(total_credit_by_month.values()) / len(total_credit_by_month)
    summary_email += f"Average debit amount: {average_debit}\n"
    summary_email += f"Average credit amount: {average_credit}\n"
    return summary_email

def main():
    file_path = 'transactions.csv'  # Update the file path here

    total_balance, num_transactions_by_month, total_debit_by_month, total_credit_by_month = process_transactions(file_path)
    summary_email = generate_summary_email(total_balance, num_transactions_by_month, total_debit_by_month, total_credit_by_month)
    send_email("Summary of Transactions", summary_email, "dederico@gmail.com")

if __name__ == "__main__":
    main()
