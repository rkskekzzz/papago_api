import argparse
import sys
from utils.fetchdata import translateProcess


def args():
	parser = argparse.ArgumentParser(description='rfc 번역 스크립트')
	parser.add_argument('--rfc', '-r', required=True, help='rfc number')

	return parser.parse_args()

if __name__ == "__main__":
	args = args()

	translateProcess(args.rfc)
