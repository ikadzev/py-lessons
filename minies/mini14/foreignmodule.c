#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

// Копирка матриц
void copy_matrix(double** inp_matrix, size_t matrix_size, double** out_matrix) {
    for (size_t s = 0; s < matrix_size; s++) {
        out_matrix[s] = malloc(matrix_size * sizeof(double*));
        for (size_t ss = 0; ss < matrix_size; ss++) {
            out_matrix[s][ss] = inp_matrix[s][ss];
        }
    }
}

// Возведение матрицы в степень (ака перемножение одной и той же матрицы)
void matrix_power(double** matrix, long matrix_size, long* mult) {
    double** init_matrix = malloc(matrix_size * sizeof(double*));
    double** out = malloc(matrix_size * sizeof(double*));
    copy_matrix(matrix, matrix_size, init_matrix);
    copy_matrix(matrix, matrix_size, out);

    long power = *mult;
    while (power != 1) {
        for (long i = 0; i < matrix_size; i++) {
            for (long j = 0; j < matrix_size; j++) {
                double sum = 0;
                for (long r = 0; r < matrix_size; r++) {
                    sum += matrix[i][r] * init_matrix[r][j];
                }
                out[i][j] = sum;
            }
        }
        copy_matrix(out, matrix_size, matrix);
        power--;
    }
}

// Возведение матрицы в степень (на иностранном Питоне)
PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    PyObject* mult = NULL;
    PyObject* matrix = NULL;
    if (!PyArg_UnpackTuple(args, "SNAFU!", 1, 2, &matrix, &mult)) {
        return NULL;
    }
    
    long c_mult = PyLong_AsLong(mult);

    long matrix_size = PyObject_Length(matrix);
    double** c_matrix = malloc(matrix_size * sizeof(double*));

    for (long i = 0; i < matrix_size; i++) {
        c_matrix[i] = (double*) malloc(matrix_size * sizeof(double));
        PyObject* item = PyList_GetItem(matrix, i);
        for (long j = 0; j < matrix_size; j++) {
            PyObject* jtem = PyList_GetItem(item, j);
            c_matrix[i][j] = PyFloat_AsDouble(jtem);
        }
    }
    
    matrix_power(c_matrix, matrix_size, &c_mult);
    
    PyObject* out_matrix = PyList_New(matrix_size);
    for (long i = 0; i < matrix_size; i++) {
        PyObject* list = PyList_New(matrix_size);
        for (long j = 0; j < matrix_size; j++) {
            PyList_SetItem(list, j, PyFloat_FromDouble(c_matrix[i][j]));
        }
        PyList_SetItem(out_matrix, i, list);
    }
    return out_matrix;
}


static PyMethodDef ForeignMethods[] = {
    {"matrix_power",
    foreign_matrix_power, METH_VARARGS,
    "Return matrix in given power."
    },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign",  /* name of module */
    NULL,       /* module documentation, may be NULL */
    -1,         /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
    ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
}

int main() {return 0;}