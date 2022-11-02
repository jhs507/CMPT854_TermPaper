from pydriller import Repository

def main():

    repo = Repository(
    "mines/abseil-cpp",
    only_in_branch='master',
    only_no_merge=True
    )


    i = 0
    for commit in repo.traverse_commits():
         i = i + 1
         print(str(i) + " ", end='')
         print('Hash {}, author {}'.format(commit.hash, commit.author.name))



if __name__ == "__main__":
    main()
