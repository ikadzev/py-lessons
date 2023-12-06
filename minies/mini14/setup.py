from setuptools import Extension, setup

setup(
    name="foreign",
    version="1.0.0",
    ext_modules=[
        Extension(
            name="foreign",
            sources=["foreignmodule.c"],
        ),
    ]
)