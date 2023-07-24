
names = ("oladapo banjo" , "teniola shalewa" , "williams michael-charter")
first_names = []
last_names = []
hyphen = []
def names_of_people():
    print(len(names))
    for x in names:
        first_names.append(x.split(' ')[0])
        last_names.append(x.split(' ')[1])
    print(first_names)
    print(last_names)
   
names_of_people()

    
