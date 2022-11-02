import datetime

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

    def compare(a, b):
        if a.num_commits > b.num_commits:
            return 1
        else:
            return -1

    def add_commit(self, commit):
        self.commits.append(commit)
        self.num_commits = self.num_commits + 1

    def first_six_months(self):
        first_commit_date = self.commits[0].author_date

        for commit in self.commits:
            print("Delta: "+str(commit.author_date - first_commit_date))
