objetivo_X = 7
objetivo_Y = 8

caballo_x = 0
caballo_y = 0
print(f'({caballo_x}, {caballo_y})', end=' ')

flow = True

while caballo_x != objetivo_X and caballo_y != objetivo_Y:
    if flow:
        caballo_x += 1
        caballo_y += 2
    else:
        caballo_x += 2
        caballo_y += 1
    print(f'({caballo_x}, {caballo_y})', end=' ')
    flow = not flow
