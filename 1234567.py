def pizza_rewards(customers, min_orders, min_price):
    res=set()
    for i,j in customers.items():
        if sum(1 for price in j if price>=min_price)>=min_orders:
            res.add(i)
    return res