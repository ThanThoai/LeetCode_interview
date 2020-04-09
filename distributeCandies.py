def distributeCandies(candies : int, num_people : int) -> List[int]:
    r = []
    dem = 0
    while(candies > 0):
        dem += 1
        if candies > dem:
            r.append(dem)
            candies -= dem
        else:
            r.append(candies)
            candies = 0
    if len(r) == num_people:
        return r 
    else:
        result = [0] * num_people
        for i in range(dem):
            result[i % num_people] += r[i]
        return result