# DO NOT EDIT!!! built with `python _building/build_setup.py`
import setuptools
setuptools.setup(
    name="k3dictutil",
    packages=["k3dictutil"],
    version="0.1.0",
    license='MIT',
    description='It provides with several dict operation functions.',
    long_description='# k3dictutil\n\n[![Action-CI](https://github.com/pykit3/k3dictutil/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3dictutil/actions/workflows/python-package.yml)\n[![Build Status](https://travis-ci.com/pykit3/k3dictutil.svg?branch=master)](https://travis-ci.com/pykit3/k3dictutil)\n[![Documentation Status](https://readthedocs.org/projects/k3dictutil/badge/?version=stable)](https://k3dictutil.readthedocs.io/en/stable/?badge=stable)\n[![Package](https://img.shields.io/pypi/pyversions/k3dictutil)](https://pypi.org/project/k3dictutil)\n\nIt provides with several dict operation functions.\n\nk3dictutil is a component of [pykit3] project: a python3 toolkit set.\n\n\nk3dictutil\n\nIt provides with several dict operation functions.\n\n#   Status\n\nThis library is considered production ready.\n\n\n\n\n# Install\n\n```\npip install k3dictutil\n```\n\n# Synopsis\n\n```python\n\nimport k3dictutil\n\nmydict = {\'a\':\n              {\'a.a\': \'v-a.a\',\n               \'a.b\': {\'a.b.a\': \'v-a.b.a\'},\n               \'a.c\': {\'a.c.a\': {\'a.c.a.a\': \'v-a.c.a.a\'}}\n               }\n          }\n\n# depth-first iterative the dict\nfor rst in k3dictutil.depth_iter(mydict):\n    print(rst)\n\n# output:\n#     ([\'a\', \'a.c\', \'a.c.a\', \'a.c.a.a\'], \'v-a.c.a.a\')\n#     ([\'a\', \'a.b\', \'a.b.a\'], \'v-a.b.a\')\n#     ([\'a\', \'a.a\'], \'v-a.a\')\n\nfor rst in k3dictutil.breadth_iter(mydict):\n    print(rst)\n\n# output:\n#     ([\'a\'],                            {\'a.c\': {\'a.c.a\': {\'a.c.a.a\': \'v-a.c.a.a\'}}, \'a.b\': {\'a.b.a\': \'v-a.b.a\'}\n#                                           , \'a.a\': \'v-a.a\'})\n#     ([\'a\', \'a.a\'],                     \'v-a.a\')\n#     ([\'a\', \'a.b\'],                     {\'a.b.a\': \'v-a.b.a\'})\n#     ([\'a\', \'a.b\', \'a.b.a\'],            \'v-a.b.a\')\n#     ([\'a\', \'a.c\'],                     {\'a.c.a\': {\'a.c.a.a\': \'v-a.c.a.a\'}})\n#     ([\'a\', \'a.c\', \'a.c.a\'],            {\'a.c.a.a\': \'v-a.c.a.a\'})\n#     ([\'a\', \'a.c\', \'a.c.a\', \'a.c.a.a\'], \'v-a.c.a.a\')\n#\n\nrecords = [\n    {"event": \'log in\',\n     "time": {"hour": 10, "minute": 30, }, },\n\n    {"event": \'post a blog\',\n     "time": {"hour": 10, "minute": 40, }, },\n\n    {"time": {"hour": 11, "minute": 20, }, },\n\n    {"event": \'log out\',\n     "time": {"hour": 11, "minute": 20, }, },\n]\n\nget_event = k3dictutil.make_getter(\'event\', default="NOTHING DONE")\nget_time = k3dictutil.make_getter(\'time.$field\')\n\nfor record in records:\n\n    ev = get_event(record)\n\n    tm = "%d:%d" % (get_time(record, {"field": "hour"}),\n                    get_time(record, {"field": "minute"}))\n\n    print("{ev:<12}   at {tm}".format(ev=ev, tm=tm))\n\n# output:\n# log in         at 10:30\n# post a blog    at 10:40\n# NOTHING DONE   at 11:20\n# log out        at 11:20\n\n```\n\n#   Author\n\nZhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n#   Copyright and License\n\nThe MIT License (MIT)\n\nCopyright (c) 2015 Zhang Yanpo (张炎泼) <drdr.xp@gmail.com>\n\n\n[pykit3]: https://github.com/pykit3',
    long_description_content_type="text/markdown",
    author='Zhang Yanpo',
    author_email='drdr.xp@gmail.com',
    url='https://github.com/pykit3/k3dictutil',
    keywords=['python', 'dictionary', 'util'],
    python_requires='>=3.0',

    install_requires=['k3ut>=0.1.15,<0.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ] + ['Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: Implementation :: PyPy'],
)
