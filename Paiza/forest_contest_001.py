def get_team_size(sport_name):
    team_sizes = {'baseball': 9, 'soccer': 11, 'rugby': 15, 'basketball': 5, 'volleyball': 6}

    return team_sizes.get(sport_name, None)

def main():
    s = input().strip()
    TS = get_team_size(s)

    if TS is not None:
        print(TS)

if __name__ == "__main__":
    main()

