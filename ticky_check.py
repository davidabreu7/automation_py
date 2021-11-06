import re
import os


def read_log():
    file_path = os.path.dirname(__file__)
    filename = os.path.join(file_path, "log_reader", "syslog.log")
    with open(filename, "r") as f:
        log_list = [line.strip() for line in f.readlines()]

    return log_list


def search_log_regex(list_log):
    search_string = re.compile(r"(INFO|ERROR)\s(.+)\s.*\((.+)\)")
    search_list = []
    for line in list_log:
        busca = re.search(search_string, line)
        if busca:
            search_list.append({
                "type": busca.group(1),
                "service": busca.group(2).lower(),
                "user": busca.group(3)
            })
    return search_list


def create_error_report(dict_list):
    count_dict = {}

    for elem in dict_list:

        if elem["type"] == "ERROR":
            error = elem["service"]
            if error in count_dict:
                count_dict[error] += 1
            else:
                count_dict[error] = 1

    return dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))


def create_user_report(dict_list):
    user_report_dict = {}
    for elem in dict_list:
        user = elem["user"]
        type = elem["type"]

        if user in user_report_dict:
            user_report_dict[user][type] += 1
        else:
            user_report_dict[user] = {
                    "INFO": 0,
                    "ERROR": 0
                }
            user_report_dict[user][type] += 1

    return dict(sorted(user_report_dict.items(), key=lambda x: x[0]))

def user_report_csv(user_report_dict):
    import csv
    fields = ["Username", "INFO", "ERROR"]

    with open("user_statics.csv", "w", newline='') as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        for k in user_report_dict:
            w.writerow({field: user_report_dict[k].get(field, k) for field in fields})

def error_report_csv(error_report_dict):
    import csv
    fields = ["Error", "Count"]

    with open("error_message.csv", "w", newline='') as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        for k in error_report_dict:
            w.writerow({
                "Error": k,
                "Count": error_report_dict[k]
                        })


def main():
    log = read_log()
    search = search_log_regex(log)
    user_report_dict = create_user_report(search)
    error_report_dict = create_error_report(search)
    user_report_csv(user_report_dict)
    error_report_csv(error_report_dict)

    # print(user_report_dict)
    # print(error_report_dict)


if __name__ == "__main__":
    main()

