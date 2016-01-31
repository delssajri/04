animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
order_names = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'sevens']

for i, animal in enumerate(animals):
    print "The %s animal is %s, it stays at %d" % (order_names[i], animals[i], i)
