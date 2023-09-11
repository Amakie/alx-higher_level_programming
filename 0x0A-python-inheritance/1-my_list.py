#!/usr/bin/python3
"""inherits class list"""


class MyList(list):
    """parent class called mylist"""

    def print_sorted(self):
        """Inherits class called MyList"""

        print(sorted(self))
