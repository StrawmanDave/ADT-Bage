
import student
import bag
import time


def main():
    b = bag.bag()
    
    total_age = 0
    start_time = time.perf_counter()

    with open("FakeNames.txt", 'r') as file:
        for line in file:
            words = line.split(" ")
            new_student = student.student(words[0], words[1], words[2], words[3], words[4])
            if(b.Insert(new_student) == False):
                print(f"Error duplicate student {new_student.first}")
            total_age += int(new_student.age)

    finish_time = time.perf_counter()

    # print(total_age)
    average = total_age // b.Size()
    elapsed = finish_time - start_time

    print(f"Average age of all: {average}")
    print(f"Insert time: {elapsed}")
    print(f"Size after insert: {b.Size()}")

    start_time = time.perf_counter()

    with open("DeleteNames.txt", 'r') as file:
        for line in file:
            ssn = line.strip()
            # print(ssn)
            temp = student.student("", "", ssn, "", "")
            if(b.Delete(temp) == False):
                print(f"Error no item found to delete {temp.ssn}")

    finished_time = time.perf_counter()
    elapsed = finished_time - start_time

    print(f"Delete time: {elapsed}")
    print(f"Size after delete: {b.Size()}")

    total_age = 0
    count = 0 

    start_time = time.perf_counter()

    with open("RetrieveNames.txt", 'r')as file:
            for line in file:
                ssn = line.strip()
                temp = student.student("", "", ssn, "", "")

                found = b.Retrive(temp)

                if(found == False):
                    print(f"Error no item found {temp.ssn}")
                else:
                    total_age += int(found.age)
                    count += 1

    finished_time = time.perf_counter()

    average = total_age // count
    elapsed = finished_time - start_time

    print(f"Average age of retrieved: {average}")
    print(f"Retrieve time: {elapsed}")
    print(f"Size after Retrieve b.Size()")
         
main()