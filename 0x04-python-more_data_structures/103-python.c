#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic python info lists.
 * @p: PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, allc, a;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allc);

	for (a = 0; a < size; a++)
	{
		type = list->ob_item[a]->ob_type->tp_name;
		printf("Element %d: %s\n", a, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[a]);
	}
}

/**
 * print_python_bytes - Prints basic Python byte objects info.
 * @p: PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char a, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (a = 0; a < size; a++)
	{
		printf("%02hhx", bytes->ob_sval[a]);
		if (a == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
