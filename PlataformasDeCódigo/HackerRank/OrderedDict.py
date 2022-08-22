from collections import OrderedDict

order = OrderedDict()
for x in range(int(input())):
    name, price = input().rsplit(sep=' ', maxsplit = 1)
    if name in order:
        order[name] += int(price)
    else:
        order[name] = int(price)
for k, v in order.items():
    print(k, v)