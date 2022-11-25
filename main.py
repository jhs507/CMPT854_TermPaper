import datetime
import sys
import pickle
from contributor import Contributor
from contributor_database import ContributorDatabase
from pydriller import Repository

def find_onboarded_contributors_list(repository_path, branch, project_name):
    repo = Repository(
        repository_path,
        only_in_branch=branch,
        only_no_merge=True
    )

    contributor_dict = {}
    total_commit_count = 0
    first_commit_date = None

    # Build a dictionary of contributors
    for commit in repo.traverse_commits():
        if first_commit_date is None:
            first_commit_date = commit.author_date

        author_name = commit.author.name

        if author_name not in contributor_dict:
            contributor_dict[author_name] = Contributor(author_name, repository_path, project_name)
            contributor_dict[author_name].add_commit(commit)
        else:
            contributor_dict[author_name].add_commit(commit)

        total_commit_count += 1

    cdb = ContributorDatabase()
    for con in contributor_dict:
        cdb.add_contributor(contributor_dict[con])


    core_threashold = total_commit_count * 0.80
    commit_count = 0
    core_contributor_database = ContributorDatabase()
    for contributor in cdb.list_of_contributors:
        commit_count = commit_count + contributor.num_commits
        core_contributor_database.add_contributor(contributor)

        if commit_count >= core_threashold:
            break


    two_year_delta = datetime.timedelta(days=730)
    on_boarded_contributor_database = ContributorDatabase()
    for contributor in core_contributor_database.list_of_contributors:
        start_date = contributor.commits[0].author_date

        if start_date - first_commit_date >= two_year_delta:
            on_boarded_contributor_database.add_contributor(contributor)

    return on_boarded_contributor_database.list_of_contributors

def print_formatted_output(on_boarded_contributors, project_code, sep, outfile):

    i = 0
    for contributor in on_boarded_contributors:
        i = i + 1
        project_name = contributor.project_name
        contributor_name = contributor.name
        contributor_code = project_code + "C" + str(i)
        inital_hash = contributor.get_inital_commit_hash()
        commits_six_months = contributor.first_six_months()
        lines_six_months = contributor.lines_in_six_months()
        inital_loc, inital_comment_loc = contributor.get_code_size_cloc()
        inital_average_CCN = contributor.get_code_complex_avg_inital()
        number_of_functions = contributor.get_code_num_functions_inital()
        number_of_complex_functions = contributor.get_code_num_complex_functions_inital()
        comment_ratio = inital_comment_loc / (inital_loc + inital_comment_loc)

        print(project_name, end=sep, file=outfile)
        print(contributor_name, end=sep, file=outfile)
        print(contributor_code, end=sep, file=outfile)
        print(inital_hash, end=sep, file=outfile)
        print(commits_six_months, end=sep, file=outfile)
        print(lines_six_months, end=sep, file=outfile)
        print(inital_loc, end=sep, file=outfile)
        print(inital_comment_loc, end=sep, file=outfile)
        print(inital_average_CCN, end=sep, file=outfile)
        print(number_of_functions, end=sep, file=outfile)
        print(number_of_complex_functions, end=sep, file=outfile)
        print(comment_ratio, end="\n", file=outfile)


def fillPickelJar(on_boarded_contributors, project_code):
    i = 0
    for contributor in on_boarded_contributors:
        i = i + 1
        contributor_code = project_code + "C" + str(i)
        commit_data = contributor.get_commit_plot_data()
        lines_data  = contributor.get_lines_plot_data()

        jar_label = "pickle_jar/"+contributor_code + ".pkl"
        jar = {
            "contributor_code": contributor_code,
            "commit_data": commit_data,
            "lines_data": lines_data
        }

        file = open(jar_label, "wb")
        pickle.dump(jar, file)
        file.close()

def main():

    repository_path = "mines/abseil-cpp"
    project_name = "abseil/abseil-cpp"
    branch = "master"


    on_boarded_contributors = find_onboarded_contributors_list(repository_path, branch, project_name)
    fillPickelJar(on_boarded_contributors, "P1")
    print_formatted_output(on_boarded_contributors, "P1", ",", sys.stdout)





if __name__ == "__main__":
    main()
