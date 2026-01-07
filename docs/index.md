# k3dict

[![Action-CI](https://github.com/pykit3/k3dict/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3dict/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3dict/badge/?version=stable)](https://k3dict.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3dict)](https://pypi.org/project/k3dict)

Dict operation utilities including iteration, getter/setter makers, and attribute access.

k3dict is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3dict
```

## Quick Start

```python
import k3dict

mydict = {'a':
              {'a.a': 'v-a.a',
               'a.b': {'a.b.a': 'v-a.b.a'},
               'a.c': {'a.c.a': {'a.c.a.a': 'v-a.c.a.a'}}
               }
          }

# depth-first iterate the dict
for rst in k3dict.depth_iter(mydict):
    print(rst)

# output:
#     (['a', 'a.c', 'a.c.a', 'a.c.a.a'], 'v-a.c.a.a')
#     (['a', 'a.b', 'a.b.a'], 'v-a.b.a')
#     (['a', 'a.a'], 'v-a.a')

# breadth-first iterate the dict
for rst in k3dict.breadth_iter(mydict):
    print(rst)
```

## API Reference

::: k3dict

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
