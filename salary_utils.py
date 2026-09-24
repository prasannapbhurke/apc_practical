def calculate_gross(basic, hra, da):
    return basic + hra + da

def calculate_deductions(pf, tax):
    return pf + tax

def calculate_net(gross, deductions):
    return gross - deductions
