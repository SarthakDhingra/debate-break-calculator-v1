#!/usr/bin/env python3

# script to convert my py unittest tests to jest tests

def make_jest():

    f = open("python_tests.txt", "r")

    lines = f.readlines()

    for line in lines:
        if line.strip().startswith('def'):
            print(line)



    wow = """
test('%s', () => {
    let test = {"teams":40,"breaking":8,"rounds":5}
    let answer = {"guranteed_break":11, "speaks_break":10, "breaking_on_speaks":2}
    let style = 4;
    checkAnswer(style, test, answer); 
});\n""" % ("ubciv_2019")

    f = open("jest_output.txt", "w")
    f.write(wow)
    f.write(wow)
    f.close()


if __name__ == "__main__":
    make_jest()