#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, i;
	PyObject *obj;

	/* get the size of Python list */
	size = Py_SIZE(p);
	/* get the alloacted memory of the Python list */
	PyListObject *list = (PyListObject *)p;
	int allocated = list->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Alloacted = %d\n", alloc);

	while (i < size)
	printf("[*] Alloacted = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: ", i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
