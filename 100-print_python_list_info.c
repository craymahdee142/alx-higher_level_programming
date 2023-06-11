#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int size, i, alloc;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] size of the Python list = %d\n", size);
	printf("[*] alloacted = 5d\n" alloc);
	for (i = 0; i < size; i++)
	{
	print("element %d:", i);
`	obj = Pylist_GetItem(p, i);
	printf("%s\n", PYy_TYPES(obj)->tp->name);
	}
}
