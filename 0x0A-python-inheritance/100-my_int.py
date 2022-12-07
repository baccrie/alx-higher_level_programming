#!/usr/bin/python3
"""This program create a new int called MyInt and is rebel!!!"""


class MyInt(int):
    """Class MyInt is like an int but Rebel"""

    def __eq__(self, other_num):
        """
        Returns wahala
        """
        return (super().__ne__(other_num))

    def __ne__(self, other_num):
        """
        Retrurns wahala
        """

        return (super().__eq__(other_num))
