#!/usr/bin/env python

class WritableObject(object):
    "dummy output stream for pylint"
    def __init__(self):
        self.content = []
    def write(self, st):
        "dummy write"
        self.content.append(st)
    def read(self):
        "dummy read"
        return self.content

def get_global_evaluation(linter):
    if linter.stats['statement'] == 0:
        return 10.0
    evaluation = linter.config.evaluation
    try:
        return eval(evaluation, {}, linter.stats)
    except Exception, ex:
        msg = 'An exception occurred while rating: %s' % ex

def run_pylint(module, ignore=None, min_rating=9.0):
    "run pylint on the given file"
    from pylint import lint
    from pylint.reporters.text import TextReporter
    ARGS = ["-r", "n"]
    if ignore != None:
        ARGS += ['--ignore='+ignore]
    pylint_output = WritableObject()
    print "##### Linting:", module
    lintrun = lint.Run([module]+ARGS, reporter=TextReporter(pylint_output), exit=False)
    for l in pylint_output.read():
        l = l.rstrip()
        if l != "":
            print l
    code_rating = get_global_evaluation(lintrun.linter)
    print "##### Overall code rating:", code_rating
    return code_rating >= min_rating

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('module')
    parser.add_argument('ignore', nargs='?', default=None)
    parser.add_argument('--min_rating', type=float, default=9.0)
    args = parser.parse_args()

    res = run_pylint(args.module, ignore=args.ignore, min_rating=args.min_rating)

    if res:
        sys.exit(0)
    else:
        sys.exit(-1)
