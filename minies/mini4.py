dict = {("Ivanov", 1): 97832, "Petrov": 55521, "Kuznecov": 97832, "Kuznebcov": 97832}

tcid = {}
for value, key in dict.items():
    if key in tcid:
        if type(tcid[key]) == tuple:
            lsit = list(tcid[key])
            lsit.append(value)
            tcid[key] = tuple(lsit)
        else:
            tcid[key] = (tcid[key], value)
    else:
        tcid[key] = value if type(value) != tuple else (value,)
print(tcid)
