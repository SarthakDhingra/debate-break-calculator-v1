# Debate Break Calculator

## Overview
- Debating is an increasingly popular activity where teams will argue against each either in favour or against a motion. Thousands of debating tournaments are hosted every single year and the most recent Worlds Universities Debating Championships held in Thailand had over 1000 participants.
- Typically debating tournaments consist of preliminary rounds and outrounds. In preliminary rounds, teams are ranked in comparison to other teams they debated against (determined by a panel of judges) and awarded points based off of their ranking. After preliminary rounds are over, teams with the highest amount of points 'break', or advance, to outrounds (for example quarterfinals or semi-finals). There can be a lot of variation in the number of points you need to advance to outrounds. With this in mind, Debate Break Calculator calculates the best-case (lowest amount of points needed to break) and worst-case (highest amount of points needed to break) break scenarios based on the number of teams in the tournament, number of rounds in the tournament, number of teams advancing to outrounds, and the style of debate

## Running the program
- Install Python 3: https://www.python.org/downloads/
- Install virtualenv: pip install virtualenv
- run `setup.sh` in the root folder
- run `flask run` in the root folder
- At this point the site should be running in your browser at whatever url flask specifies in your 
- To terminate the server run 'Ctrl C' or 'CMD C' if you are on a Mac
- run `deactivate` to terminate the virtual environment

## 



## TO DO
- Handle Edge Cases
    - No Guranteed Break
    - Only one round (already done I think)
- Fix form resubmission error for refresh after invalid input (should probably use post --> redirect --> get pattern)