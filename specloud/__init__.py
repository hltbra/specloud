import sys
import subprocess


def main():
    sys.exit(
            subprocess.call(['nosetests',
                    '-i',
                    '^(it|ensure|must|should|specs?|examples?)',
                    '-i',
                    '(specs?(.py)?|examples?(.py)?)$',
                    '--with-spec',
                    '--spec-color',
                    ] + sys.argv[1:]))
