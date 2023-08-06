def numRescueBoats(people: [int], limit: int) -> int:
    people = sorted(people)
    boats = 0
    x,y = 0,len(people)-1
    while x <= y:
        if x == y:
            boats+=1
            break
        elif people[x] + people[y] <= limit:
            boats += 1
            x += 1
            y -= 1
        else:
            y -= 1
            boats += 1
    return boats

print(numRescueBoats([3,2,2,1], 3))
s = ""
for x in range(100):
    s += str(x*x) + ", "
print(s)