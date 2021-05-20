#生成一个1到1000000的列表，找出最大和最小值并计算他们的和
value_list = []
for value in range(1,1000001):
    value_list.append(value)

print(min(value_list))
print(max(value_list))
print(sum(value_list))

