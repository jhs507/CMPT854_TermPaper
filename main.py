from Contributor import Contributor
from pydriller import Repository

def main():

    #Define the Repository to mine from
    repo = Repository(
    "mines/abseil-cpp",
    only_in_branch='master',
    only_no_merge=True
    )

    contributor_dict = {}

    for commit in repo.traverse_commits():
        author_name = commit.author.name

        if author_name not in contributor_dict:
            contributor_dict[author_name] = Contributor(author_name)
            contributor_dict[author_name].commits.append(commit)
        else:
            contributor_dict[author_name].commits.append(commit)

    i = 0
    for con in contributor_dict:
        i = i + 1
        print(str(i)+": "+contributor_dict[con].name+" made "+ str(len(contributor_dict[con].commits)) +" commits")

if __name__ == "__main__":
    main()
