import sys
import subprocess


def main():
    sys.exit(
            subprocess.call(['nosetests',
                    '-i',
                    '^(it|ensure|must|should)',
                    '--with-spec',
                    '--spec-color',
                    ] + sys.argv[1:]))
