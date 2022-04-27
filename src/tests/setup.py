from distutils.core import setup, Extension

module1 = Extension(
    'data_table',  # module name in interpreter
    sources=['../module/py_module.c', '../module/column.c', '../module/vector.c']
)

setup(
    name='data_table',
    version='1.1',
    description='',
    ext_modules=[module1]
)
# python setup.py build
# python setup.py install