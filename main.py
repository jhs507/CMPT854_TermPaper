from contributor import Contributor
from contributor_database import ContributorDatabase
from pydriller import Repository

def main():

    #Define the Repository to mine from
    repo = Repository(
    "mines/abseil-cpp",
    only_in_branch='master',
    only_no_merge=True
    )

    contributor_dict = {}

    # Build a dictionary of contributors
    for commit in repo.traverse_commits():
        author_name = commit.author.name

        if author_name not in contributor_dict:
            contributor_dict[author_name] = Contributor(author_name, "mines/abseil-cpp")
            contributor_dict[author_name].add_commit(commit)
        else:
            contributor_dict[author_name].add_commit(commit)


    db = ContributorDatabase()
    for con in contributor_dict:
        db.add_contributor(contributor_dict[con])

#    for con in db.list_of_contributors:
#        print(str(con)+" lines in first six months: "+str(con.lines_in_six_months()))

#    db.list_of_contributors[3].first_six_months()


    #comms = db.list_of_contributors[3].commits
    #first_date = comms[0].author_date


#    x_arr, y_arr = db.list_of_contributors[3].get_lines_plot_data()
#    print(x_arr)
#    print(y_arr)

    #Calculate lines of code at inital commit for a contributor
    size = db.list_of_contributors[3].get_code_size_inital()
    print("Inital loc: " + str(size))

    complex = db.list_of_contributors[3].get_code_complex_avg_inital()
    print("Inital Complex: " + str(complex))

    files = db.list_of_contributors[3].get_code_file_num_inital()
    print("Inital file count: " + str(files))

if __name__ == "__main__":
    main()
