class Contributor(object):
    """Data object for a contributor to a repository."""

    def __init__(self, name):
        super(Contributor, self).__init__()
        self.name = name
        self.commits = []
