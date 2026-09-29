
import student
import bag
import time


def main():
    b = bag.bag()
    
    all_age = 0
    student_amount = 0
    start_time = time.perf_counter()
        
    #open fakenames.txt data read eachline make a studdent put in bag
    with open('FakeNames.txt', 'r') as file:
        for line in file:
            words = line.split(" ")
            new_student = student.student(words[0], words[1], words[2], words[3], words[4])
            if(b.insert(new_student) == False):
                print(f"error duplicate student {new_student}")
    
    for i in range(b.size()):
        all_age = all_age + int(b.container[i].age)
        
    

    average = all_age // b.size()
    finish_time = time.perf_counter()
    elapsed = finish_time - start_time
    print(average)
    print(elapsed)
    print(b.size)

    with open('DeleteNames.txt,' 'r') as file:
        start_time = time.perf_counter()
        for line in file:
            temp = student.student("", "", "", line.strip, "", "")
            if(b.delete(temp)== False):
                print(f"error no item found to delete {temp.ssn}")
    finish_time = time.perf_counter()
    elapsed = finished - start_time
    print(elapsed)
    print(b.size())

    with open('RetrieveNames.txt', 'r')as file:
            for line in file:
                start_time = time.perf_counter()
                temp = student.student("", "", "",line.strip, "", "")
                if(b.retrieve(temp) == false):
                    print(f"error no item found{temp.ssn}")
                    continue
                    student_retrieved = b.retrieve(temp)
                    all_age = all_age + int(student_retrieved.age)
                    student_amount = student_amount + 1
    finished_time = time.perf_counter()
    average = all_age // student_amount
    elapsed = finished_time - start_time
    print(average)
    print(elapsed)
    print(b.size)
    
                
                 
main()

    
                
