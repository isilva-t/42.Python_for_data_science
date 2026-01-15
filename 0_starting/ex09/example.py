"""
example from subject to test our ft_package
to test correctly, after install/uninstall package
move this file to other folder, that not where source code belongs.

Example: if this example.py is on this "ex09" folder, this code will run.
because, it first finds the ft_package folder,
and runs the source code directly.

after moving this file for elsewhere,
the package needs to be installed, for a correct importing and running.
"""

from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
