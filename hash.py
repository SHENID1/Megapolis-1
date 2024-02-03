import string

with open('game.txt', "r") as f:
    sp = list(map(lambda x: x.split("$"), f.readlines()))


def get_hash(s):
    d = {}
    i = 1
    for el in string.ascii_letters:
        d.update({el: i})
        i += 1
    for el in "1234567890:-":
        d.update({el: i})
        i += 1
    st = 0
    p = 65
    m = 10 ** 9 + 9
    i = -1
    for el in s:
        i += 1
        st += d[el] * p ** i
    return st % m


del sp[0]
i = 0
with open('game_with_hash.csv', "w+") as f:
    while i < len(sp):
        name = sp[i][0].replace(" ", "") + sp[i][1].replace(" ", "")
        i += 1
        f.writelines(str(get_hash(name)) + "$" + sp[i][0] + "$" + sp[i][1] + "$" + sp[i][2] + "$" + sp[i][3])
        print(name)
print(get_hash("aaaaavg"))
