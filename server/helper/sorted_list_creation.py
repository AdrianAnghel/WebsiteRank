def add_in_sorted_list(sorted_list, string):
    for i in range(0, len(sorted_list)):
        if string.split(':')[0] > sorted_list[i].split(':')[0]:
            sorted_list.insert(i, string)
            return sorted_list
    sorted_list.append(string)
    return sorted_list


def create_top(dict_of_domains):
    top_of_websites = []
    for element in dict_of_domains:
        add_in_sorted_list(top_of_websites, str(len(dict_of_domains[element])) + ":" + str(element))
    return top_of_websites


def create_top_from_last_minute(dict_of_domains, time):
    top_of_websites = []
    for element in dict_of_domains:
        count = 0
        for i in range(0, len(dict_of_domains[element])):
            if time.minute == dict_of_domains[element][i][1].minute:
                count += 1
        if count>0:
            add_in_sorted_list(top_of_websites, str(count) + ":" + str(element))
    return top_of_websites
