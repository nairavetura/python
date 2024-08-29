for i in range(1, 301):

    if i % 5 == 0 and i % 7 == 0:
        print(f"{i} (Múltiplo de 5 y 7)")
    elif i % 5 == 0:
        print(f"{i} (Múltiplo de 5)")
    elif i % 7 == 0:
        print(f"{i} (Múltiplo de 7)")
    else:
        print(i)
    
    if i % 6 == 0:
        print("-" * 20)
