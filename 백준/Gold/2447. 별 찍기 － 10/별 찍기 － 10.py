N = int(input())

def draw_stars(num):
    if num == 1:
       return '*'

    stars = draw_stars(num//3)
    output = []

    for star in stars:
        output.append(star*3)
    for star in stars:
        output.append(star+' '*(num//3)+star)
    for star in stars:
        output.append(star*3)

    return output

print('\n'.join(draw_stars(N)))