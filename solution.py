
def direction(facing, turn):

    numb = turn / 45
    dicts = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    a = []
    for key in dicts:
        if facing == key:
            place_in = dicts.index(key)
            new_place = round(numb + place_in)
            print(new_place)
            t = 0
            while new_place >= t:
                dicts = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
                for item in reversed(dicts):
                    a = [item]
                    t += 1
                    print(t)
                    print(a)


direction("W", 495)
# direction("S", 180)
# "S",  180  -->  "N"
# "SE", -45  -->  "E"
# "W",  495  -->  "NE"


# dictss = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
# for item in dictss[::-1]:
#     print(item)
# dicts = {'N': 0 | 8, 'NE': 1, 'E': 2, 'SE': 3, 'S': 4, 'SW': 5, 'W': 6, 'NW': 7}

# [1,2,3].index(2) # => 1
# [1,2,3].index(4) # => ValueError
# a = direction("S", 0)
# print(a.values)



