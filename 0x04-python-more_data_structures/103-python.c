#include <stdio.h>
#include <Python.h>

void display_python_bytes(PyObject *object) {
    char *bytes_string;
    long int size, i, limit;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(object)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)object)->ob_size;
    bytes_string = ((PyBytesObject *)object)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  bytes: %s\n", bytes_string);

    limit = (size >= 10) ? 10 : size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++) {
        printf(" %02x", (unsigned char)bytes_string[i]);
    }

    printf("\n");
}

void display_python_list(PyObject *object) {
    long int size, i;
    PyListObject *list;

    size = ((PyVarObject *)object)->ob_size;
    list = (PyListObject *)object;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        PyObject *element = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

        if (PyBytes_Check(element)) {
            display_python_bytes(element);
        }
    }
}
