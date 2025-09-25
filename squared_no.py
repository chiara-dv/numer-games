
original_number = 2
def square(number):
    return number**2

def solutions_perfect_squares(limit):
    solutions = []
    for z in range(1,limit+1):
        print('-----------------------------------------------')
        print('Looking for solutions for z =',z,'...')
        z_sq = z**2
        for x_sq in range(1,z_sq):
            y_sq = z_sq-x_sq
            y = y_sq**(1/2)
            x = x_sq**(1/2)
            if x%1 ==0 and y%1==0:
                print('Found a solution for z =',z,'---->',end='')
                print(' x =',x,"  ;   y =",y)
                solutions.append((x,y))
    return solutions


def main():
    limit = 20
    solutions_perfect_squares(limit)      

if __name__ == "__main__":
   main()