def all(f, a):
    for e in filter(lambda e: not f(e), a):
        return False
    return True

def unzip(a):
    return [ e[0] for e in a ], [ e[1] for e in a ]

def numerize(c):
    return 2 + "23456789TJQKA".index(c)

def make_hands(s):
    def split(s): return (numerize(s[0]), s[1])
    a = s.split(' ')
    return (map(split, a[:5]), map(split, a[5:]))

def read_hands():
    file = open("poker.txt")
    a = map(make_hands, file.readlines())
    file.close()
    return a

def is_flush(suits):
    return all(lambda e: e == suits[0], suits[1:])

def is_straight(values):
    return all(lambda k: values[k] == values[k+1] + 1, range(4))

def add_dic(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1

def collect_same_values(values):
    dic = { }
    for n in values:
        add_dic(dic, n)
    
    a = list(dic.iteritems())
    a.sort(key = lambda e: -e[0] - e[1] * 15)
    return a

def rank(h):
    values, suits = unzip(h)
    values.sort(key = lambda a: -a)
    if is_flush(suits):
        if is_straight(values):
            if values[0] == 14:
                return [ 9 ] + values   # Royal Flush
            else:
                return [ 8 ] + values   # Straight Flush
        else:
            return [ 5 ] + values       # Flush
    else:
        a = collect_same_values(values)
        values = map(lambda e: e[0], a)
        if len(a) == 2:
            if a[0][1] == 4:
                return [ 7 ] + values   # Four of a Kind
            else:
                return [ 6 ] + values   # Full House
        elif len(a) == 3:
            if a[0][1] == 3:
                return [ 3 ] + values   # Three of a Kind
            else:
                return [ 2 ] + values   # Two Pairs
        elif len(a) == 4:
            return [ 1 ] + values       # One Pair
        else:
            if is_straight(values):
                return [ 4 ] + values   # Straight
            else:
                return [ 0 ] + values   # High Card

def greater_hand(h1, h2):
    r1 = rank(h1)
    r2 = rank(h2)
    for v1, v2 in zip(r1, r2):
        if v1 != v2:
            return v1 > v2
    return False

print(sum(map(lambda t: greater_hand(t[0], t[1]), read_hands())))