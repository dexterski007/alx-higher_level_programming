#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - print list
 * @p: pyobject
 */

void print_python_list(PyObject *p)
{
	size_t sze, allocat;
	int j;
	const char *typ;

	setbuf(stdout, NULL);
	PyListObject *lst = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	sze = ((PyVarObject *)p)->ob_size;
	allocat = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", sze);
	printf("[*] Allocated = %lu\n", allocat);

	for (j = 0; j < sze; j++)
	{
		typ = lst->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, typ);
		if (!strcmp(typ, "bytes"))
			print_python_bytes(lst->ob_item[j]);
		else if (!strcmp(typ, "float"))
			print_python_float(lst->ob_item[j]);
	}
}

/**
 * print_python_bytes - print bytes
 * @p: pyobject
 */
void print_python_bytes(PyObject *p)
{
	size_t j, sze, len;
	char *str;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sze = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	if (sze + 1 > 10) 
		len = 10;
	else
		len = sze + 1;
	printf("  size: %lu\n", sze);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes: ", len);
	for (j = 0; j < len; j++)
		printf("%02hhx%s", str[j], j + 1 < len ? " " : "");
	printf("\n");
}

/**
 * print_python_float - print float
 * @p: pyobject
 */

void print_python_float(PyObject *p)

{
	double k;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	k = ((PyFloatObject *)p)->ob_fval;
		printf("  value: %s\n",
		PyOS_double_to_string(k, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

