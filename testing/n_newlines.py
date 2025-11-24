'''
def create_line(n):
    print(n*"*")

    
create_line(5)
'''

def create_line(n):
    for i in range(n):
        print("*", end="")


# while
def kreiere_zeilen(n):
    i = 1
    while i < n + 1:
        print("*", end="", sep="")
        i += 1

# create_line(5)
# kreiere_zeilen(7)
'''
def vielseitige_zeilen(n):
    some_list = ["*-" for i in range(n)]
    some_str = "".join(some_list)
    print(some_str[:n])
'''

def vielseitige_zeilen(n1):
    print("".join(["*-" for i in range(n1)])[:n1])

def dreieck(n2):
    for i in range(n2):
        ## Pyramide
        # print(" "*(n-i-1)+"*"*(2*i-1))
        print("*"*(i))

# dreieck(7)
def create_array(arr_length: int)->list:
    # return [" "*(n-i)+(2*i-1)*"*" for i in range(n)]
    # return [i*"*" for i in range(1, arr_length)]
    my_array = []
    for i in range(1, arr_length):
        my_line = i*"*"
        my_array.append(my_line)
    return my_array

def print_array(some_array: list)->str:
    for i in some_array:
        print(i)


def reverse_array(array: list)->list:
    return array[::-1]


# vielseitige_zeilen(8)
print_array(create_array(6))
# forward_array = create_array(6)
# backward_array = reverse_array(forward_array)

# backward_triangle
# print_array(backward_array)

def create_array(arr_length: int)->list:
    # return [" "*(n-i)+(2*i-1)*"*" for i in range(n)]
    # return [i*"*" for i in range(1, arr_length)]
    my_array = []
    for i in range(1, arr_length):
        my_line = arr_length-i*"*"
        my_array.append(my_line)
    return my_array