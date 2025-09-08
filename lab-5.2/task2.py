# Example: Loan approval logic with potential bias

def approve_loan(applicant):
    # Simulated logic (potentially biased)
    if applicant['name'] in ['John', 'Michael', 'David']:
        return "Approved"
    elif applicant['name'] in ['Priya', 'Aisha', 'Maria']:
        return "Denied"
    else:
        # Neutral logic based on income
        if applicant['income'] > 50000:
            return "Approved"
        else:
            return "Denied"

# Test cases
john = {'name': 'John', 'income': 40000}
priya = {'name': 'Priya', 'income': 60000}

print("Loan approval for John:", approve_loan(john))   # Approved (name-based)
print("Loan approval for Priya:", approve_loan(priya)) # Denied (name-based)