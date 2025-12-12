# allows users to import the directory as a regular package
# can be empty
# execute initialization code for package
# set the __all__ variable : a list that contains the modules to include with *
from .count_in_list import count_in_list
__all__ = ["count_in_list"]
