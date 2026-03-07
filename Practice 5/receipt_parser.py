import re
import json
with open("raw.txt", "r") as f:
    text = f.read()
price_pattern = r"\d{1,3}(?:\s\d{3})*,\d{2}"
prices_raw = re.findall(price_pattern, text)
prices = []
for p in prices_raw:
    clean = p.replace(" ", "").replace(",", ".")
    prices.append(float(clean))
product_pattern = r"\d+\.\s*\n([^\n]+)"
products = re.findall(product_pattern, text)
total_calculated = sum(prices)
datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)
date = None
time = None
if datetime_match:
    date, time = datetime_match.group().split()
payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group() if payment_match else None
data = {
    "products": products,
    "prices": prices,
    "calculated_total": total_calculated,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))