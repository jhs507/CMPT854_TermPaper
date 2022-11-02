class Contributor(object):
    """Data object for a contributor to a repository."""

    def __init__(self, name):
        super(Contributor, self).__init__()
        self.name = name
        self.commits = []
        self.num_commits = 0


    def add_commit(self, commit):
        self.commits.append(commit)
        self.num_commits = self.num_commits + 1
