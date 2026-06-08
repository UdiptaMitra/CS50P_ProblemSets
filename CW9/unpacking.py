def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
print(total(*coins), "Knuts")  # total(100,50,25)
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "Knuts")  # total(galleons=100, sickles=50, knuts=25)
