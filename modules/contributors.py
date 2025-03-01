def list_all_contributors(repo, contributors):
    list_contributors = []
    contributors_all = ''
    for contributor in contributors:
        list_contributors.append(contributor['login'])
        contributors_all += f'{contributor["login"]}, '
    contributors_all = contributors_all[:-2]
    print(f'{repo} has contributor/s: {contributors_all} ')