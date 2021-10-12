import Utils


def add_score(diff):
    points_of_winning = (int(diff) * 3) + 5
    try:
        read_write_score_file = open(Utils.SCORES_FILE_NAME, "r+")
        score_file = read_write_score_file.read()
        int_score_file = int(score_file)
        sum_score_file = int_score_file + points_of_winning
        read_write_score_file.seek(0)
        read_write_score_file.write(str(sum_score_file))




    except FileNotFoundError:
        score_file = open(Utils.SCORES_FILE_NAME, "w")
        score_file.write(str(points_of_winning))




