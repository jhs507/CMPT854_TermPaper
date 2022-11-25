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

def perform_analysis(repository_path, branch, project_name, project_code):
    on_boarded_contributors = find_onboarded_contributors_list(repository_path, branch, project_name)
    fillPickelJar(on_boarded_contributors, project_code)
    print_formatted_output(on_boarded_contributors, project_code, ",", sys.stdout)

def main():

    print("Project Name,Contributor Name,Contributor Code,Initial Commit Hash,Commits in first six months,lines of code in first six months,Initial lines of code,Inital Comment Lines of Code,Initial average CCN,Number of Functions,Number of functions with CCN > 10,Comment Ratio,Modularity Level,Documentation Level,Presence of Install Guide,Presence of Build Guide,Presence of Getting Started Guide")

    tuples = [
        ("mines/rock-kernel-driver","master","radeonopencompute/rock-kernel-driver"),
        ("mines/alios-things","master","alibaba/alios-things"),
        #("mines/vk-gl-cts","main","khronosgroup/vk-gl-cts"),
        ("mines/caseflow","master","department-of-veterans-affairs/caseflow"),
        ("mines/snorkel","main","snorkel-team/snorkel"),
        ("mines/devito","master","devitocodes/devito"),
        ("mines/sqltoolsservice","main","microsoft/sqltoolsservice"),
        ("mines/openhab-docs","main","openhab/openhab-docs"),
        ("mines/botbuilder-samples","main","microsoft/botbuilder-samples"),
        ("mines/decrediton","master","decred/decrediton"),
        ("mines/oneflow","master","oneflow-inc/oneflow"),
        ("mines/picocli","main","remkop/picocli"),
        ("mines/service-ui","master","reportportal/service-ui"),
        ("mines/dde-dock","master","linuxdeepin/dde-dock"),
        ("mines/mythril","develop","consensys/mythril"),
        ("mines/kimai2","master","kevinpapst/kimai2"),
        ("mines/ovn-kubernetes","master","ovn-org/ovn-kubernetes"),
        ("mines/tasks","master","nextcloud/tasks"),
        ("mines/symplify","main","symplify/symplify"),
        ("mines/atrium","main","robstoll/atrium"),
        ("mines/redex","main","facebook/redex"),
        ("mines/swift-snapshot-testing","main","pointfreeco/swift-snapshot-testing"),
        ("mines/terraform-provider-cloudflare","master","cloudflare/terraform-provider-cloudflare"),
        ("mines/swift-protobuf","main","apple/swift-protobuf"),
        ("mines/continuous-integration","master","bazelbuild/continuous-integration"),
        ("mines/publishpress","development","publishpress/publishpress"),
        ("mines/appdaemon","dev","appdaemon/appdaemon"),
        ("mines/falco","master","falcosecurity/falco"),
        ("mines/icingaweb2-module-director","master","icinga/icingaweb2-module-director"),
        ("mines/mjml","master","mjmlio/mjml"),
        ("mines/redisjson","master","redisjson/redisjson"),
        ("mines/sled","main","spacejam/sled"),
        ("mines/goose","master","pressly/goose"),
        ("mines/fosite","master","ory/fosite"),
        #("gcapes/git-course","gh-pages","gcapes/git-course"),
        ("mines/blaze","master","meteor/blaze"),
        ("mines/h2","master","hyperium/h2"),
        ("mines/coding-standard","master","slevomat/coding-standard"),
        ("mines/picom","next","yshui/picom"),
        ("mines/nodejs-logging","main","googleapis/nodejs-logging"),
        ("mines/laravel-shopify","master","osiset/laravel-shopify"),
        ("mines/puppetlabs-kubernetes","main","puppetlabs/puppetlabs-kubernetes"),
        ("mines/volley","master","google/volley"),
        ("mines/django-bootstrap4","main","zostera/django-bootstrap4"),
        ("mines/databricks-cli","main","databricks/databricks-cli")
    ]

    i = 0
    for tuple in tuples:
        i = i + 1
        repository_path = tuple[0]
        branch = tuple[1]
        project_name = tuple[2]
        project_code = "P" + str(i)
        perform_analysis(repository_path, branch, project_name, project_code)


if __name__ == "__main__":
    main()
