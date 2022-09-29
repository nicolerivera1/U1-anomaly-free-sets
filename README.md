# U1-anomaly-free-sets

![Python package](https://github.com/nicolerivera1/U1-anomaly-free-sets/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/nicolerivera1/U1-anomaly-free-sets/workflows/Upload%20Python%20Package/badge.svg)
![GitHub contributors](https://img.shields.io/github/contributors/nicolerivera1/U1-anomaly-free-sets?style=plastic)

**by: Nicole Rivera**

Finds anomaly-free solutions to the U1 gauge group. Code implementation of https://doi.org/10.1103/PhysRevLett.123.151601

## Install
```bash
$ pip install -i https://test.pypi.org/simple/ U1-anomaly-free-sets
```
## USAGE
From python interface
```python
>>> from U1-anomaly-free-sets import joint, find_all_sets
>>> joint(5)
array([ 21.,  -6., -22.,  12.,  -5.]), [7], [9, 6], 54
```

Command line use

1. Only one solution
```bash
$ U1-anomaly-free-sets 5
Input arguments: {'n': 5, 'ALL': False, 'N': None, 'zmax': None, 'imax': None, 'outfile_name': None}
(array([ 21.,  -6., -22.,  12.,  -5.]), [7], [9, 6], 54)
```
2. All possible solutions according to sample size. This last method exports
a json file with all quiral sets and their l, k, gcd.
```bash
$ U1-anomaly-free-sets 5 -a --N=20 --zmax=30 --m_max=10 --outfile_name=ttk
Input arguments: {'n': 5, 'ALL': True, 'N': 20, 'zmax': 30, 'm_max': 10, 'outfile_name': 'ttk'}
Program finished in 0.009126128999923822 seconds
total free anomaly sets:  6
```

Links:
* [Test pip page](https://test.pypi.org/project/U1-anomaly-free-sets/)
* Flake8 Tool For Style Guide Enforcement
  * https://flake8.pycqa.org/ 
  * https://peps.python.org/pep-0008/
* [Test python code](https://docs.pytest.org/en/7.1.x/)
* [GitHub actions](https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions)


