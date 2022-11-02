class Contributor(object):
    """Data object for a contributor to a repository."""

    def __init__(self, name):
        super(Contributor, self).__init__()
        self.name = name
        self.commits = []
        self.num_commits = 0

    def __str__(self):
        string = self.name
        string += ", "
        string += str(self.num_commits)
        string += " commits"
        return string


    def add_commit(self, commit):
        self.commits.append(commit)
        self.num_commits = self.num_commits + 1
