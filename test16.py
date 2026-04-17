# Given a list of transactions [{"from": "A", "to": "B", "amount": 50}, ...], compute the net balance of each person. 

transactions = [
    {"from": "A", "to": "B", "amount": 50},
    {"from": "B", "to": "C", "amount": 30},
    {"from": "C", "to": "A", "amount": 20},

    {"from": "A", "to": "D", "amount": 40},
    {"from": "D", "to": "B", "amount": 25},

    {"from": "E", "to": "A", "amount": 60},
    {"from": "B", "to": "E", "amount": 10},

    {"from": "C", "to": "D", "amount": 35},
    {"from": "D", "to": "C", "amount": 15},

    {"from": "E", "to": "B", "amount": 20}
]




net_Bal = {}

for action in transactions:

    sender = action["from"]
    receiver = action["to"]
    
    if sender in net_Bal:
        net_Bal[sender] -= action["amount"]
    else:
        net_Bal[sender] = 0 - action["amount"]

    if receiver in net_Bal:
        net_Bal[receiver] += action["amount"]
    else:
        net_Bal[receiver] = 0 + action["amount"]

print(net_Bal)