

#Remover duplicados de una lista usando un ciclo
def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

#Remover duplicados de una lista usando sets
def remover_duplicates_sets(some_list):
    return list(set(some_list))

def run():
    random_list = [1,1,2,2,4]
    rando = [1,2,3,3,4,4,5,6,6]
    print(remove_duplicates(random_list))
    print(remover_duplicates_sets(rando))

if __name__=='__main__':
    run()