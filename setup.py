from setuptools import setup, find_packages

setup(
    name="MedCare Plus",
    version="0.1",
    description="A Doctor-Patient Management System with Authentication and Dashboards",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Subhadeep Ghorai",
    author_email="subhadeepghorai23@gmail.com",
    packages=find_packages(),
    install_requires=[
        "tkinter",          # List other dependencies here
        "sqlite3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
