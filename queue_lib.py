from typing import List, Optional


class Node:


    def __init__(self, data : str, priority : int):
        self.priority = priority
        self.data = data
        self.next = None

class elem_queue:

    def __init__(self):
        self.head = None
        self.tail = None

class basic_queue:

    def __init__(self):
        self.queues : List[Optional[elem_queue]] = [None] * 5



def create_queue():
    queue_priority = basic_queue()
    for i in range(5):
        queue_priority.queues[i] = elem_queue()

    print("Очередь создана")
    return queue_priority

def create_node(data : str, priority : int):
    elem = Node(data, priority)
    return elem



def add_node(queue : basic_queue, data : str, priority : int):

    if queue:
        element = create_node(data, priority)
        q = queue.queues[priority - 1]

        if not(q.head):
            q.head = element
            q.tail = element
        else:
            q.tail.next = element
            q.tail = element
        return True

    else:
        return False



def watch_queue(struct : basic_queue):
    res = []
    if struct:
        for i in range(5):
            queue = f"Очередь {i + 1}: "
            curr_queue = struct.queues[i]
            if curr_queue.head is None:
                queue += "--- "
            else:
                cur_element = curr_queue.head
                while cur_element:
                    queue += f"({cur_element.priority}, {cur_element.data}) "
                    cur_element = cur_element.next
                queue += "\n"
            res.append(queue)


    return res

def del_queue(struct : basic_queue):
    if struct:
        for i in range(5):
            curr_queue = struct.queues[i]
            if curr_queue.head:
                curr_queue.head = None
                curr_queue.tail = None

        return True
    else:
        return False

def length(struct : basic_queue):
    cnt = 0
    if struct:
        for i in range(5):
            if struct.queues[i].head:
                cur_element = struct.queues[i].head
                while not(cur_element == None):
                    cnt = cnt + 1
                    cur_element = cur_element.next
        return cnt
    else:
        return -1

def check_void(struct : basic_queue):
    flag = False
    if struct:
        for i in range(5):
            curr_queue = struct.queues[i]
            if curr_queue.head:
                flag = True
                break
        return flag
    else:
        return -1

def get_element(struct : basic_queue):
    if struct:
        for i in range(5):
            if struct.queues[i].head:
                cur_element = struct.queues[i].head
                res = f"({cur_element.priority}, {cur_element.data})"
                struct.queues[i].head = cur_element.next
                cur_element = None
                return res
                break
    else:
        return -1
