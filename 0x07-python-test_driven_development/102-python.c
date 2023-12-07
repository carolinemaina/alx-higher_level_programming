#include <Python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    long int length;

    if (p == NULL || !PyUnicode_Check(p)) {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");

    length = PyUnicode_GET_LENGTH(p);

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    printf("  length: %ld\n", length);

    wchar_t *wide_string = PyUnicode_AsWideCharString(p, &length);
    if (wide_string == NULL) {
        printf("[ERROR] Unable to retrieve string value\n");
        return;
    }

    printf("  value: %ls\n", wide_string);
    PyMem_Free(wide_string);
}
