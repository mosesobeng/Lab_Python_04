
groceries = ['bananas    ','strawberies','apples     ','bread    ']
groceries.append('champagne  ')

groceries.remove('bread    ')



groceries.sort()
for i in groceries:
    s=list(i)
    print i + '     --->'+ (str(s[0:1]))[2:3]


