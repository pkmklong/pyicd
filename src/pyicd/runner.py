import argparse
from process_data import collect_gems_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "retrieve_gems_data",
        help="Pull 2018 ICD9 and ICD10 GEMs mapping data from cms.gov",
        type=bool,
    )

    # Collect args
    args = parser.parse_args()

    # if args.retrieve_gems_data == True:
    collect_gems_data()


if __name__ == "__main__":
    main()
