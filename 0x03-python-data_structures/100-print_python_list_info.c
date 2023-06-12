#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i = 0;
	PyObject *obj;

	/* get the size of Python list */
	size = Py_SIZE(p);
	/* get the alloacted memory of the Python list */
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Alloacted = %d\n", alloc);
	while (i < size)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
