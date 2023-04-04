# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = []
    time = 0
    for i in range(len(cities)):
        a = cities[i].lower()
        if a in cache:
            cache.remove(a)
            time += 1
            cache.append(a)
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(a)
            time += 5
    return time


cs = 2
ct = ["Jeju", "Pangyo", "NewYork", "newyork"]
r = solution(cs, ct)
print(r)