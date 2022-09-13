def asteroid_collision(asts, index):
    #Code Here
    if asts == []:
        return []
    elif index + 1 == len(asts) :
        return asts
    else :
        if asts[index] < 0 : #left
            if index == 0 :
                return asteroid_collision(asts, index + 1)
            else :
                if asts[index - 1] < 0 :
                    return asteroid_collision(asts, index + 1)
                else :
                    if (asts[index] *  (-1)) > asts[index - 1] :
                        asts.pop(index - 1)
                        return asteroid_collision(asts, 0)
                    elif (asts[index] *  (-1)) == asts[index - 1] :
                        asts.pop(index)
                        asts.pop(index)
                        return asteroid_collision(asts, 0)
                    else :
                        asts.pop(index)
                        return asteroid_collision(asts, 0)
        elif asts[index] > 0 : #right
            if asts[index + 1] > 0 :
                return asteroid_collision(asts, index + 1)
            else :
                if (asts[index]) > asts[index + 1] * (-1) :
                        asts.pop(index + 1)
                        return asteroid_collision(asts, 0)
                elif (asts[index]) == asts[index + 1] * (-1) :
                    asts.pop(index)
                    asts.pop(index)
                    return asteroid_collision(asts, 0)
                else :
                    asts.pop(index)
                    return asteroid_collision(asts, 0)
        else :
            asts.pop(index)
            return asteroid_collision(asts, 0)
        

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x , 0))