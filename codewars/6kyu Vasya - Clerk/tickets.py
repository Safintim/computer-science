import collections


def tickets(people_money):
    ticket_price = 25
    bank = collections.Counter({25: 0, 50: 0, 100: 0})
    for money in people_money:
        delivery = money - ticket_price
        bank[money] += 1
        if delivery == 0:
            continue
        elif delivery == ticket_price and bank[delivery] != 0:
            bank[25] -= 1
        elif delivery == 75 and bank[50] != 0 and bank[25] != 0:
            bank[25] -= 1
            bank[50] -= 1
        elif delivery == 75 and bank[25] >= 3:
            bank[25] -= 3
        else:
            return 'NO'  
    
    return 'YES'