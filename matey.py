import argparse
from data2bids.data2bids import Data2Bids


def get_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter
        , description=""
        , epilog="""
            Documentation at https://github.com/SIMEXP/Data2Bids
            """)

    parser.add_argument(
        "-d"
        , "--input_dir"
        , required=False
        , default=None
        , help="Input data directory(ies), Default: current directory",
    )

    parser.add_argument(
        "-c"
        , "--config"
        , required=False
        , default=None
        , help="JSON configuration file (see example/config.json)",
    )

    parser.add_argument(
        "-o"
        , "--output_dir"
        , required=False
        , default=None
        , help="Output BIDS directory, Default: Inside current directory ",
    )

    # Add logging
    #    parser.add_argument(
    #            "-l"
    #            , "--log_level"
    #            , required=False
    #            , default="INFO"
    #            , choices=["DEBUG","INFO","WARNING","ERROR","CRITICAL"]
    #            , help="Set logging level",
    #            )

    return parser


def main():
    args = get_parser().parse_args()
    data2bids = Data2Bids("C:\\Users\\User\Downloads\\20230727", "C:\\Users\\User\\Downloads\\20230727\config.json", "C:\\Users\\User\Downloads\\20230727\\file")
    data2bids.run()


if __name__ == '__main__':
    main()