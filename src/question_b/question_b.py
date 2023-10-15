#write functions here, don't add input('') statements here!
def get_sum_of_evens(num):
    sum = 0
    for i in range(0,num + 1, 2):
        sum = sum + i
    return sum

