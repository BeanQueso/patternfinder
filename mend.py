def mend(x,y):
    string = ""
    x_len_ind = len(x)-1
    for i in x:
        ind_of_i = x.index(i)
        if ind_of_i < x_len_ind:
            string+=i
            string+=" "
        else:
            string+=i
    #print(string)
    new_str_list = string.split(" ")

    arg = input("enter your arg: ")
    new_str_list.insert(y,arg)
    #print(new_str_list)

    string = ""
    x_len_ind = len(new_str_list)-1
    for i in new_str_list:
        ind_of_i = new_str_list.index(i)
        if ind_of_i < x_len_ind:
            string+=i
            string+=" "
        else:
            string+=i
    print(string)
    new_str_list = string.split(" ")