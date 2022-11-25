import datetime
import numpy as np
import subprocess
import pandas as pd

from os.path import exists
from os import makedirs
from pydriller import Git



class Contributor(object):
    """Data object for a contributor to a repository.

    Fields:
    name - The name of the contributor.
    repository_path - Path to the repository the contributor commited to.
    commits - List of commits made by the contributor.
    num_commits - Number of commits made by the contributor.
    lizard_analysis_data - A python dataframe that holds the data from the first commit this contributor made
    lizard_analysis_status - True if the lizard_analysis_data is up to date false otherwise.

    Methods:
    add_commit(commit) - Adds commit to the list of commits.
    first_six_months() - Returns number of commits contributor made in first six months
    lines_in_six_months() - Returns number of lines contributor made in first six months
    get_code_size_inital() - Returns the number of lines in the code base for the contributor's first commit

    Static Methods:
    compare(A, B) - Used to compare two contributors sorting on number of commits
    """


    def __init__(self, name, repository_path):
        super(Contributor, self).__init__()
        self.name = name
        self.repository_path = repository_path
        self.commits = []
        self.num_commits = 0

        self.lizard_analysis_data = None
        self.lizard_analysis_status = False


    def __str__(self):
        string = self.name
        string += ", "
        string += str(self.num_commits)
        string += " commits"
        return string


    def lizard_analysis_clean(self):
        """Returns true if the lizard_stats do not need to be recalcualted"""
        if self.lizard_analysis_data is None:
            self.lizard_analysis_status = False

        return self.lizard_analysis_status


    def perform_lizard_analysis(self):
        """Calcualtes the lizard_analysis_data for the first commit made by this contributor"""
        directory_name = 'lizard_stats/'+ self.repository_path + "/"
        outfile_name = 'lizard_stats/'+ self.repository_path + "/" + self.commits[0].hash

        if not exists(directory_name):
            makedirs(directory_name)

        if not exists(outfile_name):
            git = Git(self.repository_path)
            git.checkout(self.commits[0].hash)
            command = [
                'lizard',
                '--csv',
                '-o',
                outfile_name,
                self.repository_path
            ]
            completed_process = subprocess.run(command)
            if completed_process.returncode == 0:
                pass
            else:
                print("Error running lizard on hash " + self.commits[0].hash)
            git.reset()

        headings = [
            'NLOC',
            'CCN',
            'Token',
            'Param',
            'Length',
            'Location',
            'File',
            'Function',
            'Signature',
            'Start_Line',
            'End_Line'
        ]

        self.lizard_analysis_data = pd.read_csv(outfile_name, sep=',', header=0, names=headings)
        self.lizard_analysis_status = True


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
        self.lizard_analysis_status = False


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


    def get_commit_plot_data(self):
        """Returns two np arrays representing the data points for the commits made in the first six months."""
        x_list = []
        y_list = []

        first_commit_date = self.commits[0].author_date
        six_month_delta = datetime.timedelta(days=180)

        commit_count = 0
        for commit in self.commits:
            if commit.author_date - first_commit_date < six_month_delta:
                delta = commit.author_date - first_commit_date
                x = delta.total_seconds()
                commit_count = commit_count + 1
                y = commit_count
                x_list.append(x)
                y_list.append(y)

        return np.array(x_list), np.array(y_list)


    def get_lines_plot_data(self):
        """Returns two np arrays representing the data points for the lines contributed in the first six months"""
        x_list = []
        y_list = []

        first_commit_date = self.commits[0].author_date
        six_month_delta = datetime.timedelta(days=180)

        line_count = 0
        for commit in self.commits:
            if commit.author_date - first_commit_date < six_month_delta:
                delta = commit.author_date - first_commit_date
                x = delta.total_seconds()
                line_count = line_count + commit.lines
                y = line_count
                x_list.append(x)
                y_list.append(y)

        return np.array(x_list), np.array(y_list)


    def get_code_size_inital(self):
        """Returns the cumulatave lines of code for the functions of the program at the frist commit from this contributor."""
        if not self.lizard_analysis_clean():
            self.perform_lizard_analysis()

        col_NLOC = self.lizard_analysis_data['NLOC']
        return col_NLOC.sum()

    def get_code_size_cloc(self):
        git = Git(self.repository_path)
        git.checkout(self.commits[0].hash)

        cloc_command = [
            "cloc",
            "--quiet",
            "--csv",
            self.repository_path,

        ]
        completed_process = subprocess.run(cloc_command, capture_output=True)

        tail_command = [
            "tail",
            "-n",
            "1"
        ]
        completed_process = subprocess.run(tail_command, input=completed_process.stdout, capture_output=True)
        output_line = completed_process.stdout.decode("utf-8")

        split_output = output_line.split(",")
        code_count = int(split_output[4])
        comment_count = int(split_output[3])
        git.reset()

        return code_count, comment_count

    def get_code_complex_avg_inital(self):
        """Returns the average cyclomatic complexity of the funcitons of the program at the first commit from this contributor."""
        if not self.lizard_analysis_clean():
            self.perform_lizard_analysis()

        col_CCN = self.lizard_analysis_data['CCN']
        return col_CCN.mean()


    def get_code_file_num_inital(self):
        """Returns the number of code bearing files in the code base at the inital commit by this contributor"""
        if not self.lizard_analysis_clean():
            self.perform_lizard_analysis()

        col_file = self.lizard_analysis_data['File']
        unique = col_file.unique()

        return unique.size


    def get_code_num_complex_functions_inital(self):
        """Retruns the number of functions in the code base with a complexity greater than 10"""
        if not self.lizard_analysis_clean():
            self.perform_lizard_analysis()

        df = self.lizard_analysis_data
        col_CCN = df[df['CCN'] > 10]['CCN']
        return col_CCN.size
