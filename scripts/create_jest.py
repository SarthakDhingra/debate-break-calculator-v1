#!/usr/bin/env python3

import re

# script to convert my py unittest tests to jest tests

def make_jest():

    f = open("python_tests.txt", "r")

    lines = f.readlines()

    i = 0

    f = open("jest_output.txt", "w")

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('def'):
            test_name =  line.strip().split()[1][5:-7]
            test = lines[i+1].strip()
            answer = lines[i+2].strip()
            style = re.search(r'\d+', lines[i+3].strip()).group()
            final_test = """
            test('%s', () => {
                let %s
                let %s
                let style = %s;
                checkAnswer(style, test, answer); 
            });\n""" % (test_name, test, answer, style)
            f.write(final_test)
            print(i)
        i += 1

    f.close()

if __name__ == "__main__":
    make_jest()