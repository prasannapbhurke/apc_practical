def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks, max_per_subject=100):
    return (sum(marks) / (len(marks) * max_per_subject)) * 100

def calculate_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 60:
        return "C"
    elif pct >= 50:
        return "D"
    return "F"
