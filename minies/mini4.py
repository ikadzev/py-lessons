dict = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
tcid = {dict[key] : key for key in dict.keys()}
if len(dict.keys()) != len(tcid.keys()):
    keys  = list(dict.keys())
    values = list(tcid.values())
    for x in values: keys.remove(x)
    for key in keys:
        tcid[dict[key]] = (tcid[dict[key]], key)
print(tcid)