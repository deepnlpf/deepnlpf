# Created by ioluwayo on 2018-02-11.
import argparse
import inflect # really awesome module that does to conversion.
import logging
from utils import moduleLogger # has method for initializing logging object.

def cli():
    parser = argparse.ArgumentParser(description="This script converts numbers to words.")
    parser.add_argument('number', type=str, help="The number to convert to words.")
    parser.add_argument("-g", type=int, default=0, help="Split the number int g groups before converting.")
    parser.add_argument("-v", "--verbose", action='store_true', help="Verbose logging.")
    return parser.parse_args()

def main():
    args = cli() # get user inputs from command line
    number = args.number
    groups = args.g
    verbose = args.verbose

    # check verbose flag to initialize logger with appropriate level.
    if(verbose):
        logger = moduleLogger.init_logger(__name__,logging.INFO)
    else:
        logger = moduleLogger.init_logger(__name__)

    inf = inflect.engine()

    logger.info('About to convert %s , to words.' %number) # info level only displays when verbose is true

    try:
        number = int(number)
        number = inf.number_to_words(number,group=groups)
        print number
    except ValueError as E:
        logger.error(E.message)
    except inflect.BadChunkingOptionError as E:
        logger.error('Group value is too large.') # error level log always displays


if __name__ == '__main__':
    main()