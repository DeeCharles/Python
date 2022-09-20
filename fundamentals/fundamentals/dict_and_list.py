# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
#Change the value 10 in x to 15
x[1][0]=15
#print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"]="Bryant"
#print(students)

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]="Andres"
#print(sports_directory)

#Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
#print(z)

#2. Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    #for i in range (0,len(students)):
    for el in students:
        #print(el)
        # for key, val in students[i].items():
        #     print(key, " = ", val)
        print("first_name - " + el["first_name"],", last_name -" + el["last_name"])
        # if i == len(students):
        #     return i

iterateDictionary(students)

# 3. Get Values From a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(some_key,some_list):
    for el in some_list:
        for key, val in el.items():
            if key == some_key:
                print(val)
iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)

# 4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for each_key in some_dict:
        
        print(len(some_dict[each_key]),each_key.upper())
        for i in range(0,len(some_dict[each_key])):
            value=some_dict[each_key][i]
            print(value)

    
printInfo(dojo)
