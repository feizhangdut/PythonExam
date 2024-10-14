"""
Have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, 
and return an integer output that will specify the least number of coins, that when added, equal the input integer. 
Coins are based on a system as follows: there are coins representing the integers 1, 5, 7, 9, and 11. 
So for example: if num is 1…
"""
coin = [11, 9, 7, 5 , 1]
num = 16
res =[]

for i in coin:
    if num >= i:
        res.append(num//i)
        num = num% i
print (sum(res))
