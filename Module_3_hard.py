data_structure = [
[1, 2, 3,],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    sum_ = []

    for i in data_structure:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, int|float):
                    sum_.append(j)
                elif isinstance(j, str):
                    sum_.append(len(j))
                    if j.isnumeric():
                        sum_.append(int(j))

        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, int | float):
                    sum_.append(key)
                elif isinstance(key, str):
                    sum_.append(len(key))
                    if key.isnumeric():
                        sum_.append(int(key))
                if isinstance(value, int | float):
                    sum_.append(value)
                elif isinstance(value, str):
                    sum_.append(len(value))
                    if value.isnumeric():
                        sum_.append(int(value))
        elif isinstance(i, tuple):
            for f in i:
                if isinstance(f, int|float):
                    sum_.append(f)
                elif isinstance(f, str):
                    sum_.append(len(f))
                    if f.isnumeric():
                        sum_.append(int(f))
                elif isinstance(f, dict):
                    for key, value in f.items():
                        if isinstance(key, int | float):
                            sum_.append(key)
                        elif isinstance(key, str):
                            sum_.append(len(key))
                            if key.isnumeric():
                                sum_.append(int(key))
                        if isinstance(value, int | float):
                            sum_.append(value)
                        elif isinstance(value, str):
                            sum_.append(len(value))
                            if value.isnumeric():
                                sum_.append(int(value))
                elif isinstance(f, list):
                    for j in f:
                        if isinstance(j, int | float):
                            sum_.append(j)
                        elif isinstance(j, str):
                            sum_.append(len(j))
                            if j.isnumeric():
                                sum_.append(int(j))
                        elif isinstance(j, set):
                            for l in j:
                                if isinstance(l, tuple):
                                    for f in l:
                                        if isinstance(f, int | float):
                                            sum_.append(f)
                                        elif isinstance(f, str):
                                            sum_.append(len(f))
                                            if f.isnumeric():
                                                sum_.append(int(f))
                                        elif isinstance(f, tuple):
                                            for k in f:
                                                if isinstance(k, int | float):
                                                    sum_.append(k)
                                                elif isinstance(k, str):
                                                    sum_.append(len(k))
                                                    if k.isnumeric():
                                                        sum_.append(int(k))

        elif isinstance(i,str):
            sum_.append(len(i))
            if i.isnumeric():
                sum_.append(int(i))

    return sum(sum_)

result = calculate_structure_sum(data_structure)
print(result)