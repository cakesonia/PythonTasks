import re


if __name__ == "__main__":
    count = 0
    pattern_date = re.compile('[01]/Jul/[1995]:[0][2]:([3][5-9]|[4-5][0-9])|[0][3]:([0][0-9]|[1][0-8])')
    pattern_status = re.compile('200')
    with open("access_log_Jul95") as file:
        for line in file:
            if re.search(pattern_date, str(line)) and re.search(pattern_status, str(line)):
                count += 1
                if count <= 5:
                    print(line)
