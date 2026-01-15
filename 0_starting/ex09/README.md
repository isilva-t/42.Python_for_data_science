# ft_package

A Python package example for ex09.

## Step 1 -  Build
```bash
python3 -m build
```
if 'build' isnt installed
```bash
pip install build
```

## Step 2 - Installation
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```
or
```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage example
```bash
python3 -c "
from ft_package import count_in_list
print(count_in_list(['toto', 'tata', 'toto'], 'toto'))
print(count_in_list(['toto', 'tata', 'toto'], 'tutu'))
"
```

# Check

```bash
pip show -v ft_package
```

## Uninstall
```bash
pip uninstall ft_package -y
rm -rf dist/ build/ *.egg-info ft_package.egg-info
```

## Author

isilva-t - 42 Porto
