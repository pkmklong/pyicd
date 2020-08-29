import argparse
from data_utils.process_data import retrieve_and_format_gems


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "retrieve_gems_data",
        help="Pull 2018 ICD9 and ICD10 GEMs mapping data from cms.gov",
        type=str,
    )

    # Collect args
    args = parser.parse_args()

    if args.retrieve_gems_data:
        retrieve_and_format_gems()


if __name__ == "__main__":
    run()
