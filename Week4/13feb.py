#Total Revenue from Active Customers
def Rev():
    customers = [
        {"name": "A", "purchases": [50, 200, 300], "active": True},
        {"name": "B", "purchases": [500, 20], "active": False},
        {"name": "C", "purchases": [150, 250], "active": True}
    ]
    f = filter(lambda c: c["active"], customers)
    total = sum(map(lambda c: sum(map(lambda p: p+(p*0.1) if p >= 100 else 0, c["purchases"])), f))
    print(total)

#Total Discounted Price of Electronics
def Elec():
    products = [
        ("Laptop", "Electronics", 1000),
        ("Shirt", "Clothing", 50),
        ("Phone", "Electronics", 500)
    ]
    f = filter(lambda p: p[1] == "Electronics", products)
    total = sum(map(lambda p: p[2] * 0.8, f ))
    print(total)

#Student Weighted Score Calculator
def marks():
    students = [
        {"name": "A", "marks": [50, 60, 70]},
        {"name": "B", "marks": [30, 40]},
        {"name": "C", "marks": [80, 90]}
    ]
    f = filter(lambda s: sum(s["marks"])/len(s["marks"]) >= 60, students)
    total = sum(map(lambda s: sum(map(lambda m: m+5, s["marks"])), f))
    print(total)
""""
Multi-Region Sales Analytics Engine
Problem Statement
You are given a list of regions. 
Each region contains multiple stores, and each store contains multiple transactions.
Each transaction has:
• amount (float)
• category (string)
• successful (boolean)
Task
• Consider only transactions that:
• Are successful
• Belong to category "Electronics"
• Have amount ≥ 100
Apply:
• 18% GST to each valid transaction
• Then apply an additional 5% regional surcharge
Compute:
• The total revenue per region
• Then return the grand total across all regions

Final output: single float (grand total)
"""
def sales():
    regions = [{"region": "North","stores": [{
                    "transactions": [
                        {"amount": 200, "category": "Electronics", "successful": True},
                        {"amount": 50, "category": "Electronics", "successful": True},
                        {"amount": 500, "category": "Clothing", "successful": True}
                    ]
                }
            ]
        },
        {"region": "South","stores": [{
                    "transactions": [
                        {"amount": 300, "category": "Electronics", "successful": True},
                        {"amount": 150, "category": "Electronics", "successful": False}
                    ]
                }
            ]
        }
    ]
    n = filter(lambda r: r["region"] == "North", regions)
    n = map(lambda x: x["stores"],n)
    n = map(lambda x: x["transactions"],n)
    print(list(n))
    """en = filter(lambda x: x["successful"] and x["category"]=="Electronics" and x["amount"]>=100,n)
    print(en)
    tn = sum(map(lambda x:x["amount"],en))
    print(tn)
    s = filter(lambda r: r["region"] == "South", regions)
    es = filter(lambda x: x["successful"] and x["category"]=="Electronics" and x["amount"]>=100,s)
    print(es)
    ts = sum(map(lambda x:x["amount"],es))
    print(ts)
    gt = tn + ts
    print(gt)"""

def main():
    sales()

if __name__ == "__main__":
    main()