import os

PROJECT_NAMES = map("sub_project_{}".format, range(5))


SETUP_FILE_NAME = "setup.py"


SETUP_TEMPLATE = """
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="{name}",
        version="0.0.1"
    )
"""


def write_file(fname, content):
    with open(fname, "w") as fd:
        fd.write(content)


def create_subprojects(names=PROJECT_NAMES):
    for name in names:
        os.mkdir(name)
        write_file(
            fname=os.path.join(name, SETUP_FILE_NAME),
            content=SETUP_TEMPLATE.format(name=name))
        for req_file in ('requirements.txt', 'dev-requirements.txt'):
            write_file(fname=os.path.join(name, req_file), content='')
