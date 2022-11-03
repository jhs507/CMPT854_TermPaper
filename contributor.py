import datetime

class Contributor(object):
    """Data object for a contributor to a repository.

    Fields:
    name - The name of the contributor.
    commits - List of commits made by the contributor.
    num_commits - Number of commits made by the contributor.

    Methods:
    add_commit(commit) - Adds commit to the list of commits.
    first_six_months() - Returns number of commits contributor made in first six months
    lines_in_six_months() - Returns number of lines contributor made in first six months

    Static Methods:
    compare(A, B) - Used to compare two contributors sorting on number of commits
    """


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


    @staticmethod
    def compare(A, B):
        """Compares two contributor objects.

        Returns 1 if the number of commits in A is more than in B
        Returns -1 if the number of commits in B is more than in A
        """
        if A.num_commits > B.num_commits:
            return 1
        else:
            return -1


    def add_commit(self, commit):
        """Adds the passed in commit to the list of commits.

        Increments the num_commits field.

        Parameters:
        commit - The commit to be added to the internal list.
        """
        self.commits.append(commit)
        self.num_commits = self.num_commits + 1


    def first_six_months(self):
        """Returns number of commits in the first six months of the first commit"""
        first_commit_date = self.commits[0].author_date
        six_month_delta = datetime.timedelta(days=180)

        count = 0
        for commit in self.commits:
            if commit.author_date - first_commit_date < six_month_delta:
                count = count + 1

        return count

    def lines_in_six_months(self):
        """Returns number of lines contributed in first six months of first commit."""
        first_commit_date = self.commits[0].author_date
        six_month_delta = datetime.timedelta(days=180)

        line_count = 0
        for commit in self.commits:
            if commit.author_date - first_commit_date < six_month_delta:
                line_count = line_count + commit.lines

        return line_count
