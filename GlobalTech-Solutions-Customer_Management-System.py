# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)


# Service categories dictionary
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "IT Support": 90
}


# Customer dictionaries
customer1 = {
    "company_name": "Alpha Tech",
    "contact_person": "John Smith",
    "email": "john@alphatech.com",
    "phone": "813-555-1111"
}

customer2 = {
    "company_name": "Beta Industries",
    "contact_person": "Sarah Lee",
    "email": "sarah@betaind.com",
    "phone": "813-555-2222"
}

customer3 = {
    "company_name": "Gamma Solutions",
    "contact_person": "David Chen",
    "email": "david@gammasol.com",
    "phone": "813-555-3333"
}

customer4 = {
    "company_name": "Delta Systems",
    "contact_person": "Maria Lopez",
    "email": "maria@deltasys.com",
    "phone": "813-555-4444"
}


# Master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}


# Display all customers
print("\nAll Customers:")
print("-" * 60)

for cid, info in customers.items():
    print(f"Customer ID: {cid}")
    for key, value in info.items():
        print(f"{key}: {value}")
    print()


# Customer lookups
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\nCustomer Lookups:")
print("-" * 60)

print("C002 Info:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Lookup:", c999_info)


# Updating customer information
customers["C001"]["phone"] = "813-555-9999"
customers["C002"]["industry"] = "Manufacturing"

print("\nUpdating Customer Information:")
print("-" * 60)

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])


# Project dictionaries
project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 13200}
project3 = {"name": "Sales Data Dashboard", "service": "Data Analysis", "hours": 80, "budget": 14000}
project4 = {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 90, "budget": 18000}
project5 = {"name": "Network Maintenance", "service": "IT Support", "hours": 40, "budget": 3600}


# Projects dictionary organized by customer
projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

print("\nProject Information:")
print("-" * 60)

for cid, plist in projects.items():
    print(f"Customer {cid} Projects:")
    for p in plist:
        print(p)
    print()


# Project cost calculations
print("\nProject Cost Calculations:")
print("-" * 60)

for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print("Project:", p["name"], "Cost:", cost)


# Customer statistics using dictionary methods
print("\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", list(customers.keys()))

company_names = [c["company_name"] for c in customers.values()]
print("Companies:", company_names)

print("Total Customers:", len(customers))


# Service usage analysis
service_counts = {}

for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("\nService Usage Analysis:")
print("-" * 60)
print(service_counts)


# Financial calculations across projects
hours_list = []
budget_list = []

for plist in projects.values():
    for p in plist:
        hours_list.append(p["hours"])
        budget_list.append(p["budget"])

total_hours = sum(hours_list)
total_budget = sum(budget_list)
avg_budget = total_budget / len(budget_list)

max_budget = max(budget_list)
min_budget = min(budget_list)

print("\nFinancial Summary:")
print("-" * 60)

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Highest Budget:", max_budget)
print("Lowest Budget:", min_budget)


# Customer summary report
print("\nCustomer Summary Report:")
print("-" * 60)

for cid, info in customers.items():
    plist = projects.get(cid, [])
    hours = sum(p["hours"] for p in plist)
    budget = sum(p["budget"] for p in plist)

    print("\nCustomer ID:", cid)
    print("Company:", info["company_name"])
    print("Projects:", len(plist))
    print("Total Hours:", hours)
    print("Total Budget:", budget)


# Adjusted service rates using dictionary comprehension
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)


# Active customers dictionary
active_customers = {cid: customers[cid] for cid in customers if cid in projects}

print("\nActive Customers:")
print("-" * 60)
print(active_customers)


# Customer budget totals dictionary
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

print("\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)


# Service pricing tiers
service_tiers = {
    service: ("Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic")
    for service, rate in services.items()
}

print("\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)


# Customer validation function
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]

    for field in required:
        if field not in customer_dict.keys():
            return False

    return True


print("\nCustomer Validation:")
print("-" * 60)

for cid, cust in customers.items():
    print(cid, validate_customer(cust))


# Project status tracking
status_counts = {"active": 0, "completed": 0, "pending": 0}
statuses = ["active", "completed", "pending"]

i = 0
for plist in projects.values():
    for p in plist:
        p["status"] = statuses[i % 3]
        status_counts[p["status"]] += 1
        i += 1

print("\nProject Status Summary:")
print("-" * 60)
print(status_counts)


# Budget analysis function
def analyze_customer_budgets(projects_dict):

    results = {}

    for cid, plist in projects_dict.items():
        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count else 0

        results[cid] = {
            "total": total,
            "average": avg,
            "count": count
        }

    return results


budget_analysis = analyze_customer_budgets(projects)

print("\nDetailed Budget Analysis:")
print("-" * 60)
print(budget_analysis)


# Service recommendation function
def recommend_services(customer_id, customers, projects, services):

    used_services = set()

    for p in projects.get(customer_id, []):
        used_services.add(p["service"])

    recommendations = []

    for service in services:
        if service not in used_services:
            recommendations.append(service)

    return recommendations


print("\nService Recommendations:")
print("-" * 60)

for cid in customers:
    rec = recommend_services(cid, customers, projects, services)
    print(cid, "recommendations:", rec)