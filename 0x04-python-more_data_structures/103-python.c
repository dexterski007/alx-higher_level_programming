#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list - print list
 * @p: pyobject
 */
#include <Python.h>

void print_python_list(PyObject *p) {
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < PyList_Size(p); i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}
/**
 * print_python_bytes - print bytes
 * @p: pyobject
 */
void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    printf("  [.] Size: %ld\n", PyBytes_GET_SIZE(p));
    printf("  [.] Address of the first byte: %p\n", (void *)((PyBytesObject *)p)->ob_sval);
    printf("  [.] First 10 bytes: ");
    for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p) && i < 10; i++) {
        printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
        if (i + 1 < PyBytes_GET_SIZE(p) && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}
