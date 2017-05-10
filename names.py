#PART 1 Create program from dictionary that outputs first name last name

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def full_name (arr):
    for i in arr:
        print i['first_name'], i['last_name']

full_name(students)

#PART II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def org_names(dict):
    for i in dict:
        print i
        # for j in dict[i]:
        for j,d in enumerate( dict[i]):
            print j+1, "-",d['first_name'].upper(), d['last_name'].upper(), "-",len(d['first_name'])+len(d['last_name'])

org_names(users)
