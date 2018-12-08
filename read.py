
file_object = open("testmatrix2.txt", "r")
line_list, int_list, sum_col_list = [], [], []

for line in file_object:
    line_list.append(line.split())
    
    #convert int elements of list
    for i in line_list:
        new_list = []
        for j in i:
            a = int(j)
            new_list.append(a)
    int_list.append(new_list)
    
#sum of row
def sum_row(list1):
    sum_row_list = []
    for i in list1:
        sum_row_list.append(sum(i))
    return sum_row_list

#sum of coloumn
def sum_col(list1):
    sum_collist = []
    for i in range(len(list1)):
        for j in range(len(list1)):
            sum_col_list.append(list1[j][i])
        sum_collist.append(sum(sum_col_list))   
    return sum_collist

def sort_row(list1):
    sum_row_list =[]
    sort_list = sum_row(list1)
    for i,j in range(len(sort_list) - 1):
        if sort_list[i] ==  sort_list[i+1]:
            print("esit")
        elif sum_row_list[i] <  sum_row_list[i+1]:
            print("kucuk")
        else:
            print("buyuk")
           

print(int_list)
print(sum_row(int_list))
print(sum_col(int_list))
sort_row(int_list)
