from tkinter import*
from ctypes import*
import queue_lib
import queue_module
# Загружаем DLL
lib = CDLL("./DLL1.dll")

# Определяем структуры
class Node(Structure):
    pass
    
Node._fields_ = [
    ("data", c_char * 11),
    ("priority", c_int),
    ("next", POINTER(Node))
]

class elem_queue(Structure):
    _fields_ = [
        ("head", POINTER(Node)),
        ("tail", POINTER(Node))
    ]

class basic_queue(Structure):
    _fields_ = [
        ("queues", POINTER(elem_queue) * 5)
    ]


lib.create_queue.restype = POINTER(basic_queue)

lib.add_node.restype = c_bool
lib.add_node.argtypes = [POINTER(POINTER(basic_queue)), c_int, c_char_p]

lib.del_queue.restype = c_bool
lib.del_queue.argtypes = [POINTER(POINTER(basic_queue))]

lib.length.restype = c_int
lib.length.argtypes = [POINTER(POINTER(basic_queue))]

lib.check_void.restype = c_int
lib.check_void.argtypes = [POINTER(POINTER(basic_queue))]

def error():
    listbox.delete(0, END)
    listbox.insert(END, f"ОШИБКА!!!\nСначала нужно создать структуру")

q = None
m = None
l = None

def c_lib():


    listbox.delete(0, END)
    listbox.insert(END, "Используется библиотека c++")

def python_lib():


    listbox.delete(0, END)
    listbox.insert(END, "Используется библиотека python")

def create_queue():
    global q, m, l
    if selected_var.get() == "C++":
        print("c++")

        q = lib.create_queue()
        listbox.delete(0, END)
        listbox.insert(END, "Очередь создана")
    elif selected_var.get() == "Stl":
        print("очередь создана")
        l = queue_module.PriorityQueue()
        print("очередь создана")
        listbox.delete(0, END)
        listbox.insert(END, "Очередь создана")
    else:
        print("python")

        m = queue_lib.create_queue()
        listbox.delete(0, END)
        listbox.insert(END, "Очередь создана")

def write_queue():
    global q, m, l
    if selected_var.get() == "C++":
        print("c++")


        if not(q):
            listbox.delete(0, END)
            listbox.insert(END, "ОШИБКА!!!\nСначала нужно создать структуру")
        else:
            queues_array = q.contents.queues
            result = []
            for i in range(5):
                cur_queue = queues_array[i]
                queue = f"Очередь {i + 1}:"
                if cur_queue.contents.head:
                    cur_element = cur_queue.contents.head
                    while cur_element:
                        print(cur_element.contents.priority, cur_element.contents.data)
                        queue += f"({cur_element.contents.priority}, {cur_element.contents.data.decode("utf-8")}) "
                        cur_element =  cur_element.contents.next
                        
                else:
                    queue += "---"
                queue += "\n"
                result.append(queue)

            listbox.delete(0, END)

            for i in range(len(result)):
                listbox.insert(END, result[i])
    elif selected_var.get() == "Stl":
        listbox.delete(0, END)
        if l is not None:
            if l.is_empty():
                listbox.insert(END, "Очередь пуста")
            else:
                items = l.queue_list()
                for i, val in enumerate(items):
                    listbox.insert(END, f"Приоритет: {i + 1}. Данные: {val}")
        else:
            error()

    else:
        print("python")

        if m:
            result = queue_lib.watch_queue(m)
            listbox.delete(0, END)
            for x in result:
                listbox.insert(END, x)
        else:
            error()




def length_queue():
    global q, m, l
    if selected_var.get() == "C++":
        print("c++")
        result = lib.length(pointer(q))
        if result != -1:
            listbox.delete(0, END)
            listbox.insert(END, f"В очереди {result}")
        else:
            error()
    elif selected_var.get() == "Stl":
        if l is None:
            error()
        else:
            result = l.get_size()
            print("Stl")
            listbox.delete(0, END)
            listbox.insert(END, f"В очереди {result}")


    else:

        if m:
            count = queue_lib.length(m)
            print("python")
            if count != -1:
                listbox.delete(0, END)
                listbox.insert(END, f"В очереди {count}")
        else:
            error()


def del_queue():
    global q, m
    if selected_var.get() == "C++":
        print("c++")
        lib.del_queue(q)
        listbox.delete(0, END)
        listbox.insert(END, f"Очередь удалена")
        flag = False
    else:

        if m:
            print("python")
            result = queue_lib.del_queue(m)
            if result:
                listbox.delete(0, END)
                listbox.insert(END, f"Очередь удалена")
        else:
            error()

def check_queue():
    global q, m, l
    if selected_var.get() == "C++":
        print("c++")
        result = lib.check_void(pointer(q))

        if result == 1:
            listbox.delete(0, END)
            listbox.insert(END, f"В очереди есть элементы")
        elif result == 0:
            listbox.delete(0, END)
            listbox.insert(END, f"В очереди нет элементов")
        else:
            error()
    elif selected_var.get() == "Stl":
        if l is None:
            error()
        else:
            result = l.is_empty()
            print("Stl")
            if result:
                listbox.delete(0, END)
                listbox.insert(END, f"В очереди нет элементов")
            else:
                listbox.delete(0, END)
                listbox.insert(END, f"В очереди есть элементы")

    else:
        if m:
            result = queue_lib.check_void(m)
            print("python")
            if result != -1:
                if result:
                    listbox.delete(0, END)
                    listbox.insert(END, f"В очереди есть элементы")
                else:
                    listbox.delete(0, END)
                    listbox.insert(END, f"В очереди нет элементов")
        else:
            error()

def get_element():
    global l
    print(selected_var.get())

    if selected_var.get() == "C++":
        print("c++")


        if not(q):
            listbox.delete(0, END)
            listbox.insert(END, "ОШИБКА!!!\nСначала нужно создать структуру")
        else:
            queues_array = q.contents.queues
            for i in range(5):
                print(i)
                if queues_array[i].contents.head:
                    cur_element = queues_array[i].contents.head

                    result = f"({cur_element.contents.priority}, {cur_element.contents.data.decode("utf-8")})"
                    listbox.delete(0, END)
                    listbox.insert(END, result)
                    queues_array[i].contents.head = cur_element.contents.next
                    cur_element = None
                    break

    elif selected_var.get() == "Stl":
        if l is None:
            error()
        else:
            result = l.peek()
            print(result)
            listbox.delete(0, END)
            if result:
                listbox.insert(END, f"Элемент: {result}")
            else:
                listbox.insert(END, "Очередь пуста")

    else:
        if m:
            result = queue_lib.get_element(m)
            if result == -1:
                error()
            else:
                listbox.delete(0, END)
                listbox.insert(END, result)
        else:
            error()

def add_queue():
    global q, m, l
    value = str(element_input.get())
    # prior = int(priority_input.get())
    if selected_var.get() == "C++":
        print("c++")
        prior = int(priority_input.get())
        if prior < 0 or prior > 5:
            listbox.delete(0, END)
            listbox.insert(END, "ОШИБКА!!!\nПриоритет принимает значения от 1 до 5")
        else:
            q_new = pointer(q)

            lib.add_node(q_new, prior, value.encode("utf-8"))

            listbox.delete(0, END)
            listbox.insert(END, "Элемент добавлен")
    elif selected_var.get() == "Stl":
        if l is None:
            error()
        else:
            prior = int(priority_input.get())
            l.push(int(value), prior - 1)
            listbox.delete(0, END)
            listbox.insert(END, "Элемент добавлен")
    else:
        if m:
            prior = int(priority_input.get())
            print("python")
            if prior < 0 or prior > 5:
                listbox.delete(0, END)
                listbox.insert(END, "ОШИБКА!!!\nПриоритет принимает значения от 1 до 5")
            else:
                result = queue_lib.add_node(m, value, prior)
                if result:
                    listbox.delete(0, END)
                    listbox.insert(END, "Элемент добавлен")
        else:
            error()

    element_input.delete(0, END)
    priority_input.delete(0, END)

root = Tk()

root.geometry("500x600")
root.title("Очередь")
root["bg"] = "#33ffe6"
root.resizable(False, False)



text1 = Label(root, text = "PQ", font = ("Arial", 40), bg = "#33ffe6", fg = "#9B30FF")

text1.place(x = 200, y = 250)


listbox = Listbox(root, height=5, width = 3, selectmode=SINGLE)
listbox.place(x=40, y=5, width=400, height=170)
listbox.insert(END, "Привет!")



selected_var = StringVar(value="")
rb1 = Radiobutton(root, text="Python", variable=selected_var, value="Python", bg = "#33ffe6", fg = "blue", command = python_lib)
rb2 = Radiobutton(root, text="C++", variable=selected_var, value="C++", bg = "#33ffe6", fg = "blue", command = c_lib)
rb3 = Radiobutton(root, text="Stl", variable=selected_var, value="Stl", bg = "#33ffe6", fg = "blue")

rb1.place(x = 220, y = 550)
rb2.place(x = 120, y = 550)
rb3.place(x = 320, y = 550)

btn1 = Button(text = "Создать очередь", command = create_queue, bg = "blue", fg = "white")

btn4 = Button(text = "Удалить очередь", bg = "blue", command = del_queue, fg = "white")
btn5 = Button(text = "Пустота очереди", bg = "blue", command = check_queue, fg = "white")
btn6 = Button(text = "Длина очереди", command = length_queue, bg = "blue", fg = "white")

btn7 =Button(text = "Считать элемент", bg = "blue", command = get_element, fg = "white")

btn8 = Button(text = "Считать очередь", command = write_queue, bg = "blue", fg = "white")



btn1.place(x = 40, y = 180, width=400, height=50)
btn8.place(x = 40, y = 235, width=140, height=40)
btn5.place(x = 300, y = 235, width=140, height=40)
btn4.place(x = 40, y = 325, width=400, height=50)
btn6.place(x = 40, y = 280, width=140, height=40)
btn7.place(x = 300, y = 280, width=140, height=40)

#
element = Label(root, text="Введите приоритет", font = ("Arial", 10), bg = "blue", fg = "white")
element.place(x = 40, y = 410)


element_input = Entry(root)
element_input.place(x = 190, y = 460, width=140, height=40)

priority = Label(root, text="Введите элемент", font = ("Arial", 10), bg = "blue", fg = "white")
priority.place(x = 40, y = 470)


priority_input = Entry(root)
priority_input.place(x = 190, y = 400, width=140, height=40)



result_btn = Button(root, text="Добавить\nэлемент", command = add_queue, bg = "#9B30FF")
result_btn.place(x = 340, y = 400, width = 100, height = 100)

root.mainloop()
