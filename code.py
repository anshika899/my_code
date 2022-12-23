import math


start = 11111111
end = 99999999

count_second_small = 0
count_second_largest=0

second_smallest=0
second_largest = 0

def findprime(num):
    end_num= int(math.sqrt(end+1))
    for i in range(2,end_num):
        if i!=num and num%i==0:
            return False

    return True


for i in range(start,end+1):
    if findprime(i)==True:
        count_second_small+=1

    if count_second_small==2:
        second_smallest=i
        break

for i in range(end, start-1,-1):
    if findprime(i) == True:
        count_second_largest += 1

    if count_second_largest == 2:
        second_largest = i
        break



def find_pos(word):

    n=len(word)

    char_1_rem = count_second_small%(n)
    char_2_rem= count_second_largest%(n)

    print(word[char_1_rem]," ",word[char_2_rem])

find_pos("GREYBIANSROCK")
