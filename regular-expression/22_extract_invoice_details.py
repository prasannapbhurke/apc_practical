import re

invoice_text = 'Invoice INV-2026-889 issued on 15-10-2026 with total amount Rs. 45000.50 due.'

inv_no = re.findall(r'\bINV-[0-9]{4}-[0-9]+\b', invoice_text)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', invoice_text)
amounts = re.findall(r'Rs\.?\s*\d+(?:\.\d{2})?', invoice_text)

print('Invoice Text:', invoice_text)
print('Invoice Number:', inv_no)
print('Date:', dates)
print('Amount:', amounts)
