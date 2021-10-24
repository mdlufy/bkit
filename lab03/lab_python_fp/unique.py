from gen_random import gen_random

class Unique(object):

    def __init__(self, items, **kwargs):

        self.items = items

        if kwargs:
            seen, result = set(), []
            for item in self.items:
                if type(item) == str:
                    if str(item.lower()) not in seen:
                        seen.add(item.lower())
                        result.append(item)
                else:
                    if item not in seen:
                        seen.add(item)
                        result.append(item)
        else:
            result = list(set(self.items))

        self.items = result



    def __next__(self):
        self.items += 1
        return (self.items)

    def __iter__(self):
        return (el for el in self.items)

'''
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
[print(*((el) for el in Unique(data)), sep = ", ")]

data = gen_random(5, 1, 3)
[print(*((el) for el in Unique(data)), sep = ", ")]

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
[print(*((el) for el in Unique(data)), sep = ", ")]
[print(*((el) for el in Unique(data, ignore_case = True)), sep = ", ")]
'''

#print(list(Unique(items, ignore_case=True).get()))
#[print(el) for el in Unique(data, ignore_case=True)]