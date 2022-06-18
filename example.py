students = {'john':["django","c","c+++"],'jim':["java","c#"],'dwight':["sales","nodejs"]}
keys1 = students.keys()
for eachkey in keys1:
    print("this course is taken by",eachkey)
    for eachcourse in students[eachkey]: #here value will be call
        print(eachcourse)