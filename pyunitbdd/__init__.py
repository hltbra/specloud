import sys
import subprocess


def main():
    sys.exit(
            subprocess.call(['nosetests',
                    '-i',
                    '^(it|ensure|must|should)',
                    ] + sys.argv[1:]))
