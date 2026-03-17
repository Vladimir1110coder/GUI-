#include "pch.h"
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <windows.h>

#define _CRT_SECURE_NO_WARNINGS


BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
struct Node {
    char data[11];
    int priority;
    Node* next;
};

struct elem_queue {
    Node* head;
    Node* tail;
};

struct basic_queue {
    elem_queue* queues[5];
};

bool flag = false;

Node* create_node(char data_values[10], int priority_values) {
    Node* elem = (Node*)malloc(sizeof(Node));
    if (elem == NULL) return NULL;

    elem->priority = priority_values;
    strncpy_s(elem->data, 11, data_values, 10);
    elem->data[10] = '\0';
    elem->next = NULL;

    return elem;
}


__declspec(dllexport) basic_queue* create_queue() {
    basic_queue* queue = NULL;

    queue = (basic_queue*)malloc(sizeof(basic_queue));
    if (queue == NULL) return NULL;

    // Создаем 5 очередей
    for (int i = 0; i < 5; i++) {
        queue->queues[i] = (elem_queue*)malloc(sizeof(elem_queue));
        queue->queues[i]->head = NULL;
        queue->queues[i]->tail = NULL;
    }

    flag = true;

    return queue;
}

__declspec(dllexport) bool add_node(basic_queue** Queue, int prior, char data[10]) {
    if (!flag || Queue == NULL || *Queue == NULL) return false;
    if (prior < 1 || prior > 5) return false;

    Node* element = create_node(data, prior);
    if (element == NULL) return false;

    elem_queue* q = (*Queue)->queues[prior - 1];

    if (q->head == NULL) {
        q->head = element;
        q->tail = element;
    }
    else {
        q->tail->next = element;
        q->tail = element;
    }
    return true;
}

__declspec(dllexport) bool del_queue(basic_queue** struct_ptr) {
    if (!flag || struct_ptr == NULL || *struct_ptr == NULL) return false;

    for (int i = 0; i < 5; i++) {
        elem_queue* curr_queue = (*struct_ptr)->queues[i];

        Node* curr = curr_queue->head;
        while (curr != NULL) {
            Node* next = curr->next;
            free(curr);
            curr = next;
        }

        free(curr_queue);
    }

    free(*struct_ptr);
    *struct_ptr = NULL;
    flag = false;

    return true;
}

__declspec(dllexport) int length(basic_queue** struct_ptr) {
    if (!flag || struct_ptr == NULL || *struct_ptr == NULL) return -1;

    int cnt = 0;
    for (int i = 0; i < 5; i++) {
        Node* cur_element = (*struct_ptr)->queues[i]->head;
        while (cur_element != NULL) {
            cnt++;
            cur_element = cur_element->next;
        }
    }
    return cnt;
}

__declspec(dllexport) int check_void(basic_queue** struct_ptr) {
    int i;
    elem_queue* curr_queue;
    bool flag_check;

    flag_check = true;
    if (flag == true) {
        for (i = 0; i < 5; i++) {

            curr_queue = (*struct_ptr)->queues[i];
            if (curr_queue->head != NULL)
                flag_check = false;
        }
        if (flag_check) {
            return 0;
        }
        else {
            return 1;
        }
    }
    else {

        return -1;
    }

}
