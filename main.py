import datetime
from contributor import Contributor
from contributor_database import ContributorDatabase
from pydriller import Repository

def main():

    repository_path = "mines/abseil-cpp"

    #Define the Repository to mine from
    repo = Repository(
    repository_path,
    only_in_branch='master',
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
            contributor_dict[author_name] = Contributor(author_name, repository_path)
            contributor_dict[author_name].add_commit(commit)
        else:
            contributor_dict[author_name].add_commit(commit)

        total_commit_count += 1

    cdb = ContributorDatabase()
    for con in contributor_dict:
        cdb.add_contributor(contributor_dict[con])


    print("Total Commits: "+str(total_commit_count))

    core_threashold = total_commit_count * 0.80
    commit_count = 0
    core_contributor_database = ContributorDatabase()
    for contributor in cdb.list_of_contributors:
        commit_count = commit_count + contributor.num_commits
        core_contributor_database.add_contributor(contributor)

        if commit_count >= core_threashold:
            break

    print("\nCore Contributor List:")
    for contributor in core_contributor_database.list_of_contributors:
        print(contributor.name +" "+ str(contributor.num_commits) + " commits.")


    two_year_delta = datetime.timedelta(days=730)
    on_boarded_contributor_database = ContributorDatabase()
    for contributor in core_contributor_database.list_of_contributors:
        start_date = contributor.commits[0].author_date

        if start_date - first_commit_date >= two_year_delta:
            on_boarded_contributor_database.add_contributor(contributor)


    print("\nOn-boarded Contributor List:")
    for contributor in on_boarded_contributor_database.list_of_contributors:
        print(contributor.name +
        " "+
        str(contributor.first_six_months()) +
        " commits. "+
        str(contributor.lines_in_six_months())+
        " lines."
        )



if __name__ == "__main__":
    main()
