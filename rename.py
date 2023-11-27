import os

FILE_NAMES = [
    'squad_std_stats.csv',
    'score_fixtures.csv',
    'squad_goalkeeping_stats.csv',
    'squad_adv_goalkeeping_stats.csv',
    'squad_shooting_stats.csv',
    'squad_passing_stats.csv',
    'squad_passtypes_stats.csv',
    'squad_goal_shoot_creation_stats.csv',
    'squad_defensive_stats.csv',
    'squad_possesion_stats.csv',
    'squad_playingtime_stats.csv',
    'squad_miscellaneous_stats.csv',
    'regular_season.csv',
    'home_away.csv'
]

def count_directories(folder_path):
    entries = os.listdir(folder_path)
    directories = (entry for entry in entries if os.path.isdir(os.path.join(folder_path, entry)))
    directory_names = list(directories)
    num_directories = len(directory_names)

    return num_directories, directory_names


def rename_files(dir_path):
    for i, file_name in enumerate(FILE_NAMES):
        old_file_path = os.path.join(dir_path, f'{i}.csv')
        new_file_path = os.path.join(dir_path, file_name)
        os.rename(old_file_path, new_file_path)

    print("File renaming completed.")

if __name__ == "__main__":
    date_path = '2023_11_24'

    num_directories, directory_names = count_directories(date_path)

    for i in range(num_directories):
        path = os.path.join(date_path, directory_names[i])

        rename_files(path)