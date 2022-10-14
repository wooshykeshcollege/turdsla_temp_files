def get_last_line():
    with open('data.csv', 'r')as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        last_line = int(last_line.split(",")[0])
        return last_line

#[0] is frame count that is fetched to keep track of image#
