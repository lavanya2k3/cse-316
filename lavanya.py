from queue import Queue

teacher_queue = Queue()
student_queue = Queue()

books = [["Book1", 5], ["Book2", 3], ["Book3", 2]]

teacher_waiting_time = []
student_waiting_time = []

while True:
    print("Enter your name:")
    name = input()
    status = ""
    while status not in ["teacher", "student"]:
        print("Enter your status (teacher/student):")
        status = input()
        if status not in ["teacher", "student"]:
            print("Invalid status entered. Please enter either 'teacher' or 'student'.")

    x= True
    while(x):
        print("Please Enter the book you want that exist's in Libary :")
        book_name = input()
        for i in range(len(books)):
            if books[i][0] == book_name:
                if books[i][1] > 0:
                    x = False
                    books[i][1] -= 1
                    if status == "teacher":
                        teacher_queue.put((name,book_name))
                        teacher_waiting_time.append(teacher_queue.qsize() - 1)
                    else:
                        student_queue.put((name,book_name))
                        student_waiting_time.append(student_queue.qsize() - 1)
                else:
                    print("Book not available")

    print("Do you want to continue (y/n)?")
    choice = input()
    if choice == "n":
        break

while not teacher_queue.empty():
    print(teacher_queue.get())

while not student_queue.empty():
    print(student_queue.get())

if len(teacher_waiting_time) > 0:
    avg_teacher_waiting_time = sum(teacher_waiting_time) / len(teacher_waiting_time)
else:
    avg_teacher_waiting_time = 0

if len(student_waiting_time) > 0:
    avg_student_waiting_time = sum(student_waiting_time) / len(student_waiting_time)
else:
    avg_student_waiting_time = 0

print(f"Average waiting time for teachers: {avg_teacher_waiting_time}")
print(f"Average waiting time for students: {avg_student_waiting_time}")