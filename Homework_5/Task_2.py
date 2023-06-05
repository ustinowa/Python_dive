def premium(name: list[str], wage_rate: list[int], prem: list[str]):

    return {k: i*float(j[:-1]) for k, i, j in zip(name, wage_rate, prem)}


print(premium(['Николай', 'Юлия', 'Алексей'], [10000, 50000, 78000], ['10.25%', '9.82%', '30.25%']))
