sanadwich_orders = ['apple','banana','candy']
finished_sandwiches = []
while sanadwich_orders:
    finished= sanadwich_orders.pop()
    print('I meet your ' + finished + ' sanadwich')
    finished_sandwiches.append(finished)
# for finished in finished_sandwiches:
print(finished_sandwiches)