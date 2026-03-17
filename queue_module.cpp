#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <queue>    
#include <vector>

namespace py = pybind11;

class PriorityQueue {
public: std::vector<std::queue<int>> queues;
      PriorityQueue() : queues(5) {}
};

std::vector<std::vector<int>> priority_queue_to_vector(PriorityQueue& pq) { 
    std::vector<std::vector<int>> result(5);

    for (int i = 0; i < 5; ++i) {
        std::queue<int> temp = pq.queues[i];

        while (!temp.empty()) {
            result[i].push_back(temp.front());
            temp.pop();
        }
    }
    return result;
};

int priority_queue_size(PriorityQueue& pq) {
    int result = 0;
    for (int i = 0; i <= 4; i++) {
        result += pq.queues[i].size();

    }
    return result;
}

bool priority_queue_is_empty(PriorityQueue& pq) {
    for (int i = 0; i <= 4; i++) {
        if (!pq.queues[i].empty()) {
            return false;
        }
    }
    return true;
}


void priority_queue_push(PriorityQueue& pq, int val, int prior) { 
    if (prior >= 0 && prior < 5) {
        pq.queues[prior].push(val);
    }
}



std::vector<int> priority_queue_top(PriorityQueue& pq) {
    for (int i = 4; i >= 0; --i) {
        if (!pq.queues[i].empty()) {
            int elem = pq.queues[i].front();
            pq.queues[i].pop();  
            return {i, elem};    
        }
    }
    return {}; 
}

PYBIND11_MODULE(queue_module, m) {
    py::class_<PriorityQueue>(m, "PriorityQueue")
        .def(py::init<>())
        .def("push", &priority_queue_push)
        .def("peek", &priority_queue_top)
        .def("is_empty", &priority_queue_is_empty)
        .def("get_size", &priority_queue_size)
        .def("queue_list", &priority_queue_to_vector);
};
