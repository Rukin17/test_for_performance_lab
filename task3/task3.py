import json
import sys


def fill_report(values_file, tests_file, report_file):
    with open(values_file, 'r') as f:
        values_data = json.load(f)
    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    values_dict = {value["id"]: value["value"] for value in values_data["values"]}

    def insert_value(tests):
        if isinstance(tests, dict):
            for key in tests:
                if key == 'id' and tests[key] in values_dict:
                    tests['value'] = values_dict[tests[key]]
                elif isinstance(tests[key], dict) or isinstance(tests[key], list):
                    insert_value(tests[key])
        elif isinstance(tests, list):
            for i in range(len(tests)):
                insert_value(tests[i])

    insert_value(tests_data['tests'])

    with open(report_file, 'w') as f:
        json.dump(tests_data, f, indent=4)


if __name__ == '__main__':
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    fill_report(values_file, tests_file, report_file)