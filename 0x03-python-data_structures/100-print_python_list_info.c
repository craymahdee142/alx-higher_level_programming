#include <Python.h>
/**
 *print_python_list_info - print basic Python info
 *@p: PythonObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyOject *obj;

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
