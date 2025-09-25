original_number = 2
def square(number):
    return number**2


# def solutions_perfect_squares(limit: int) -> list(list[int])
from typing import List
import time

def square_list(int_list:List[int]) -> List[int]:
   return [x**2 for x in int_list]


def add_list(list1:list[int],list2:list[int]) ->dict[tuple,int]:
    #return [x1+x2 for x1,x2 in zip(list1,list)]
    dictionary = {}
    for x1 in list1:
        for x2 in list2:
            dictionary[tuple((x1,x2))] =x1 + x2
    return dictionary



def solutions_perfect_squares(limit: int) -> List[List[int]]:
    solutions = []
    """
    A very nice function
    """

    # OLD STRATEGY
    # for z in range(1,limit+1):
    #     print('-----------------------------------------------')
    #     print('Looking for solutions for z =',z,'...')
    #     z_sq = z**2
    #     for x_sq in range(1,z_sq):   # STORE AND RESUSE THIS CODE !!!
    #         y_sq = z_sq-x_sq
    #         y = y_sq**(1/2)
    #         x = x_sq**(1/2)
    #         if x%1 ==0 and y%1==0:
    #             print('Found a solution for z =',z,'---->',end='')
    #             print(' x =',x,"  ;   y =",y)
    #             solutions.append((x,y))
    results =[]
    # NEW STRATEGY
    nums = list(range(1,limit+1))
    squares = square_list(nums)
    added_squares = add_list(squares,squares)
    for key,value in added_squares.items():
        if value in squares:
            print(value)
            results.append([key[0] ** 0.5, key[1] ** 0.5, value ** 0.5]). #see this function agaun
    return results


def main():
    start_time = time.time()
    limit = 20
    solutions_perfect_squares(limit)  
    end_time = time.time()    
    print(end_time-start_time)
if __name__ == "__main__":
   main()