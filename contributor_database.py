from contributor import Contributor
from functools import cmp_to_key

class ContributorDatabase(object):
    """Holds contributor objects and provides utilites to manipulate them."""

    def __init__(self):
        super(ContributorDatabase, self).__init__()
        self.list_of_contributors = []


    def add_contributor(self, contributor):
        self.list_of_contributors.append(contributor)
        self.list_of_contributors.sort(
            key=cmp_to_key(Contributor.compare),
            reverse=True
        )
