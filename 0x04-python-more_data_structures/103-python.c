#include <stdio.h>
#include <Python.h>

void display_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Error: Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void display_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Error: Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *bytes_string = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_string);

    Py_ssize_t limit = (size >= 10) ? 10 : size + 1;

    printf("  first %ld bytes:", limit);

    for (Py_ssize_t i = 0; i < limit; i++) {
        printf(" %02x", (unsigned char)bytes_string[i]);
    }

    printf("\n");
}
