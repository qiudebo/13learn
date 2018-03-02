import option
import os
from stockholm import Stockholm


def main():
	args=option.parser.parse_args()
	print(args)
	stockh = Stockholm(args)
	stockh.run()


if __name__ == '__main__':
	main()