customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

latest=lambda dis:{
        'name':dis['name'],
        'age':dis['age'],
        'total_purchase':dis['total_purchase']*(0.9 if dis['age']>=18 and dis['age']<=25 else 0.95 if dis['age']>=26 and dis['age']<=40
         else 1.0)
    }
updated=list(map(latest, customers))
print(updated)