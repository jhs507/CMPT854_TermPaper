from contributor import Contributor
from functools import cmp_to_key

class ContributorDatabase(object):
    """Holds contributor objects and provides utilites to manipulate them.

    Fields:
    list_of_contributors - list of contributors sorted by number of commits

    Methods:
    add_contributor(contributor) - Adds contributor to the list of contributors.
    """

    def __init__(self):
        super(ContributorDatabase, self).__init__()
        self.list_of_contributors = []


    def add_contributor(self, contributor):
        """Adds contributor to list of contributors.

        Sorts the list of contributors decending by number of commits.
        """
        self.list_of_contributors.append(contributor)
        self.list_of_contributors.sort(
            key=cmp_to_key(Contributor.compare),
            reverse=True
        )
