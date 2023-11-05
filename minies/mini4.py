dict = {("Ivanov", 1): 97832, "Petrov": 55521,
        "Kuznecov": 97832, "Kuznebcov": 97852}

tcid = {}
u_taple = []
for value, key in dict.items():  # value = 12345
    if key in tcid:
        if key in u_taple:
            del u_taple[u_taple.index(key)]
        if type(tcid[key]) == tuple:
            lsit = list(tcid[key])
            lsit.append(value)
            tcid[key] = tuple(lsit)
        else:
            tcid[key] = (tcid[key], value)
    else:
        if type(value) != tuple:
            tcid[key] = value
        else:
            tcid[key] = (value,)
            u_taple.append(key)
for key in u_taple:
    tcid[key] = tcid[key][0]
print(tcid)
