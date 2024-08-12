N = int(input())

def draw_stars(N):
    if N == 3:
        return ['  *  ', ' * * ', '*****']

    stars = draw_stars(N//2)
    L = []
    for star in stars:
        L.append(' '*(N//2)+star+' '*(N//2))
    for star in stars:
        L.append(star+' '+star)
    return L

print('\n'.join(draw_stars(N)))