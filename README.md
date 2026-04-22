# GlobalTech-Solutions-Customer-Management-System

This Python program simulates a basic customer management system for a company called **GlobalTech Solutions**. It uses **dictionaries**, **lists**, **loops**, **functions**, and **dictionary comprehensions** to organize customer and project data, perform lookups, calculate totals, and generate reports.

## Purpose

The purpose of this project is to demonstrate how Python dictionaries can be used to:

- Store and organize customer information
- Track services and project data
- Perform data lookups
- Update records
- Calculate project costs and financial summaries
- Analyze service usage
- Generate reports with aggregated data

## Features

### Service Management
The program stores service categories and hourly rates in a dictionary, including:

- Web Development
- Data Analysis
- Cybersecurity
- Cloud Consulting
- IT Support

### Customer Records
The program keeps customer details such as:

- Company name
- Contact person
- Email
- Phone number

Each customer is stored in a master dictionary using a customer ID.

### Customer Lookups
The program shows how to:

- Access a full customer record by ID
- Retrieve a single field from a customer record
- Safely search for a missing customer using `.get()`

### Updating Information
The program updates customer data by:

- Changing an existing phone number
- Adding a new field to a customer record

### Project Tracking
Each customer can have one or more projects.  
Each project includes:

- Project name
- Service type
- Hours worked
- Budget

Projects are stored in a dictionary organized by customer ID.

### Cost Calculations
The program calculates the total project cost by multiplying:

hourly service rate × project hours

### Statistics and Analysis
The system also performs several summaries, including:

- Total number of customers
- List of company names
- Service usage counts
- Total project hours
- Total budget
- Average budget
- Highest and lowest project budgets

### Reports
The program prints a customer summary report showing:

- Customer ID
- Company name
- Number of projects
- Total hours
- Total budget

### Dictionary Comprehensions
The code uses dictionary comprehensions to create:

- Adjusted service rates with a 10% increase
- Active customers
- Customer budget totals
- Service pricing tiers

### Functions
The program includes custom functions for:

- **Customer validation**  
  Checks whether each customer has all required fields.

- **Budget analysis**  
  Calculates total, average, and project count for each customer.

- **Service recommendations**  
  Recommends services a customer has not used yet.

## Concepts Used

This project practices the following Python concepts:

- Dictionaries
- Nested dictionaries
- Lists
- Loops
- Conditional expressions
- Dictionary methods like `.keys()`, `.values()`, and `.get()`
- Functions
- List comprehensions
- Dictionary comprehensions
- Aggregation with `sum()`, `len()`, `max()`, and `min()`

## How to Run

1. Open the program in Python.
2. Run the script in your IDE or terminal.
3. Review the printed output for customer information, project summaries, financial analysis, and service recommendations.

## Example Output Sections

When run, the program displays sections such as:

- All Customers
- Customer Lookups
- Updating Customer Information
- Project Information
- Project Cost Calculations
- Customer Statistics
- Service Usage Analysis
- Financial Summary
- Customer Summary Report
- Adjusted Service Rates
- Active Customers
- Customer Budget Totals
- Service Pricing Tiers
- Customer Validation
- Project Status Summary
- Detailed Budget Analysis
- Service Recommendations

## File Name Suggestion

You can save this program with a name like:

```python
globaltech_customer_management.py
