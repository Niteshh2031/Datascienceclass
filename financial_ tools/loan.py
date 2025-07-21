def calculate_emi(principal, rate, time):
    monthly_rate = rate / (12 * 100)
    emi = principal * monthly_rate * ((1 + monthly_rate)**(time * 12)) / ((1 + monthly_rate)**(time * 12) - 1)
    return round(emi, 2)
