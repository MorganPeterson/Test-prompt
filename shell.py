#!/usr/bin/env python

"""
    shell.py

    Takes in a list of values (arg 1) and tests another value (arg 2) against
    that list. When done, prints out list of accepted values.

    NOTICE:
    1.) All imported values are converted to strings!
    2.) list of values should be a comma seperated string that gets split into
        a list of passed values.
"""

import sys

class TEST_PROMPT:
    def __init__(self):
        if len(sys.argv) != 3:
            print 'USAGE: {0} {1} {2}'.format(\
                sys.argv[0], 'ListOfTestValues','ValueToTestAgainstList')
            sys.exit(1)
        else:
            # assigns list of values
            self.test_values   = sys.argv[1].split(',')
            # value we are testing against
            self.base_value    = sys.argv[2]

        self.return_values = []

        # user input test
        self.pos_cont = 'y'
        self.pos_stop = '1'
        self.neg_cont = 'n'

        #All formatting for our command instructions is done here
        self.fmt_str  = '{0} - {1} ({2})'
        self.yes_cont = self.fmt_str.format('Yes','continue', self.pos_cont)
        self.no_cont  = self.fmt_str.format('No','continue', self.neg_cont)
        self.yes_stop = self.fmt_str.format('Yes', 'stop', self.pos_stop)
        self.no_stop  = self.fmt_str.format('No','stop','any key')
        self.our_prmt = '{0} | {1} | {2} | {3}\n'.format(\
            self.yes_cont, self.no_cont, self.yes_stop, self.no_stop)

        # formating for our command prompt
        self.pmpt_fmt = '{0}Is this {1} > {2}? > '

    def main(self):
        # Main loop through list provided by user
        for values in self.test_values:
            x = raw_input(self.pmpt_fmt.format(\
                self.our_prmt, values, self.base_value))

            if x is self.pos_cont:
                self.return_values.append(values)
            elif x is self.pos_stop:
                self.return_values.append(values)
                break
            elif x is self.neg_cont:
                pass
            else:
                break

        print self.return_values

if __name__ == '__main__':
    TEST_PROMPT().main()

