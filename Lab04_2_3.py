print 'Question 2'
##2a.     They will use the dictionary Data Structure cause they will need a key and value
##       where stock is the key and price is the value

shopStock ={'Apples      ' : '7.3' , 'Bananas     ' : '5.5' , 'Bread       ' : '1.0' , 'Carrots     ':'10.0','Champagne   ':'20.90','Strawberries':'32.6'}
print 'The Initial Items in the store'
for i in shopStock:
    print i +'                      '+ shopStock[i]
print''

##Changing the value of straberries
shopStock['Strawberries']='63.43'


##Adding another item to dictionary
shopStock['Chicken     ']='6.5'

print 'The Final Items in the store'
for i in shopStock:
    print i +'                      '+ shopStock[i]
print''

print''
print''
print 'Question 3'
##3a.    The list should be used
##


##3b.
print 'The List for advertisement'
in_stock = shopStock.keys()

##3c.
always_in_stock=()

##convertion from list to tuple
always_in_stock+=tuple(in_stock)
    



##3d.
print ''

print 'Come to shoprite! We always sell:'
for i in always_in_stock :
    print i
 







