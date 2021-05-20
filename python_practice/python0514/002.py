sanadwich_orders = ['apple','banana','apple','candy','duck','apple']
print(sanadwich_orders)
print('不好意思，apple_sandwich卖完了')

while 'apple' in sanadwich_orders:
    sanadwich_orders.remove('apple')
print(sanadwich_orders)


# finished_sandwiches = []
# while sanadwich_orders:
#     finished= sanadwich_orders.pop()
#     print('I meet your ' + finished + ' sanadwich')
#     finished_sandwiches.append(finished)
# # for finished in finished_sandwiches:
# print(finished_sandwiches)
#
