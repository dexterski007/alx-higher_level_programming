#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print list
 * @p: pyobject
 */
#include <Python.h>

void print_python_list(PyObject *p)
{
	int sze, allocat, j;
	const char *typ;
	PyListObject *lst = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	sze = var->ob_size;
	allocat = lst->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", sze);
	printf("[*] Allocated = %d\n", allocat);

	for (j = 0; j < sze; j++)
	{
		typ = lst->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, typ);
		if (strcmp(typ, "bytes") == 0)
			print_python_bytes(lst->ob_item[j]);
	}
}

/**
 * print_python_bytes - print bytes
 * @p: pyobject
 */
void print_python_bytes(PyObject *p)
{
	unsigned char j, sze;
	PyBytesObject *byte = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byte->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		sze = 10;
	else
		sze = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", sze);
	for (j = 0; j < sze; j++)
	{
		printf("%02hhx", byte->ob_sval[j]);
		if (j == (sze - 1))
			printf("\n");
		else
			printf(" ");
	}
}

