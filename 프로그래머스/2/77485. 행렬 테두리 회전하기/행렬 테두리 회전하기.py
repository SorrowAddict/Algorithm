# from pprint import pprint

def solution(rows, columns, queries):
    answer = []
    arr = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    # pprint(arr)
    
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        tmp = arr[x1][y1]
        min_v = 1e9
        
        for y in range(y1 + 1, y2 + 1):
            arr[x1][y], tmp = tmp, arr[x1][y]
            min_v = min(min_v, tmp)
        
        for x in range(x1 + 1, x2 + 1):
            arr[x][y2], tmp = tmp, arr[x][y2]
            min_v = min(min_v, tmp)
            
        for y in range(y2 - 1, y1 - 1, -1):
            arr[x2][y], tmp = tmp, arr[x2][y]
            min_v = min(min_v, tmp)
            
        for x in range(x2 - 1, x1 - 1, -1):
            arr[x][y1], tmp = tmp, arr[x][y1]
            min_v = min(min_v, tmp)
        
        answer.append(min_v)
    return answer