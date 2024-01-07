#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - print info
 * @p: pyobject
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t i = 0;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", PyList_GET_SIZE(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < PyList_GET_SIZE(p); i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
