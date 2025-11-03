# ShonH_12-10_HW.py


def main():
    input_filename = input("Enter the name of the input file: ")

    # --- Step 1: Read and clean file lines ---
    with open(input_filename, 'r') as input_file:
        file_lines = [line.strip() for line in input_file if line.strip()]

    # --- Step 2: Build dictionary of seasons → shows ---
    seasons_to_shows = {}
    line_index = 0

    while line_index < len(file_lines) - 1:
        season_line = file_lines[line_index]
        show_line = file_lines[line_index + 1]

        try:
            season_count = int(season_line)
        except ValueError:
            line_index += 1
            continue  # skip malformed lines

        if season_count not in seasons_to_shows:
            seasons_to_shows[season_count] = []
        seasons_to_shows[season_count].append(show_line)

        line_index += 2  # move to next pair

    # --- Step 3: Sort by season count (descending) and write output_keys.txt ---
    with open('output_keys.txt', 'w') as output_by_keys:
        for season_count in sorted(seasons_to_shows.keys(), reverse=True):
            joined_titles = '; '.join(seasons_to_shows[season_count])
            output_by_keys.write(f"{season_count}: {joined_titles}\n")

    # --- Step 4: Sort all shows alphabetically and write output_titles.txt ---
    all_shows = []
    for shows_list in seasons_to_shows.values():
        all_shows.extend(shows_list)

    # Sort in reverse alphabetical order
    all_shows.sort(reverse=True)

    with open('output_titles.txt', 'w') as output_by_titles:
        for show_name in all_shows:
            output_by_titles.write(f"{show_name}\n")


if __name__ == "__main__":
    main()
