import math
import random
import copy


def tsp(data123):
    point = random.choice(data123)
    data = copy.deepcopy(data123)
    return_distance = 0
    path=[]
    next_point = None
    while len(data123) != 0:
        distance = 0
        path.append(data.index(point))
        data123.remove(point)
        for i in range(len(data123)):
            if i == 0 and data123[i] != point:
                distance = int(math.hypot(data123[i][0] - point[0], data123[i][1] - point[1]))
                next_point = data123[i]
            elif int(math.hypot(data123[i][0] - point[0], data123[i][1] - point[1])) < distance and data123[i] != point:
                distance = int(math.hypot(data123[i][0] - point[0], data123[i][1] - point[1]))
                next_point = data123[i]
        point = next_point
        return_distance+=distance
    return_distance += int(math.hypot(data[path[0]][0]-data[path[len(path)-1]][0], data[path[0]][1]-data[path[len(path)-1]][1]))
    path.append(path[0])
    return return_distance, path