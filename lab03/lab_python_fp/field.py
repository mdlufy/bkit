def field(items, *args):
    assert len(args) > 0

    for item in items:
        dict = {arg: item.get(arg) for arg in args if item.get(arg)}
        
        if len(dict) == 0: continue

        if len(args) == 1: yield dict[args[0]]
        else: yield dict


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Стул', 'color': 'black', 'price': None}
]

'''
print(list(field(goods, 'title')))
print(list(field(goods, 'title', 'price')))

'''
