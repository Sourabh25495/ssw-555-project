#!/usr/bin/python3
from prettytable import PrettyTable
from datetime import datetime
import US04
FILE_PATH = './Gedcom1.ged'
INDIs = {}
FAMs = {}

def parse(file):
    # Open the file and get the number of lines
    f = open(file, 'r')
    lines = f.read().splitlines()
    current = 0
    last = len(lines)

    # Loop till all lines are done
    while current < last:
        # Split the line to parts
        _line_parts = split_line(lines[current])
        # Move the to current to the next line
        current += 1
        # Check if the line start with 0
        if _line_parts[0] == '0':
            # Check if it INI or FAM
            if _line_parts[2] == 'INDI':
                _individual = Individual(_line_parts[1])
                # As long the line don't start with 0, keep reading and
                # populate the individual
                while True:
                    _line_parts = split_line(lines[current])
                    if _line_parts[0] == '1':
                        if _line_parts[1] == 'NAME':
                            _individual.name = _line_parts[2]
                        elif _line_parts[1] == 'SEX':
                            _individual.gender = _line_parts[2]
                        elif _line_parts[1] == 'BIRT':
                            _date_line_parts = split_line(lines[current+1])
                            if _date_line_parts[1] == 'DATE':
                                _individual.birthday = _date_line_parts[2]
                                current += 1
                        elif _line_parts[1] == 'DEAT':
                            _date_line_parts = split_line(lines[current+1])
                            if _date_line_parts[1] == 'DATE':
                                _individual.death = _date_line_parts[2]
                                current += 1
                        elif _line_parts[1] == 'FAMC':
                            _individual.child = _line_parts[2]
                        elif _line_parts[1] == 'FAMS':
                            _individual.spouse = _line_parts[2]
                        current += 1
                    elif _line_parts[0] == '2':
                        current += 1
                    else:
                        # Add _individual to list then break to the next one
                        INDIs[_individual.indiid] = _individual
                        break
            elif _line_parts[2] == 'FAM':
                _familie = Familie(_line_parts[1])
                # As long the line don't start with 0, keep reading and
                # populate the familie
                while True:
                    _line_parts = split_line(lines[current])
                    if _line_parts[0] == '1':
                        if _line_parts[1] == 'HUSB':
                            _familie.husbandid = _line_parts[2]
                        elif _line_parts[1] == 'WIFE':
                            _familie.wifeid = _line_parts[2]
                        elif _line_parts[1] == 'CHIL':
                            _familie.children.append(_line_parts[2])
                        elif _line_parts[1] == 'MARR':
                            _date_line_parts = split_line(lines[current+1])
                            if _date_line_parts[1] == 'DATE':
                                _familie.married = _date_line_parts[2]
                                current += 1
                        elif _line_parts[1] == 'DIV':
                            _date_line_parts = split_line(lines[current+1])
                            if _date_line_parts[1] == 'DATE':
                                _familie.divorced = _date_line_parts[2]
                                current += 1
                        current += 1
                    else:
                        # Add _familie to list then break to the next one
                        FAMs[_familie.famid] = _familie
                        break

def split_line(line):
    '''Split the line to 3 parts: level, part_one and part_two'''

    _line_parts = line.split(' ', 2)
    _level = _line_parts[0]
    _part_one = _line_parts[1].rstrip()
    _part_two = ''
    try:
        _part_two = _line_parts[2].rstrip()
    except Exception as e:
        pass
    return [_level, _part_one, _part_two]

def print_individuals():
    '''Print all individuals using PrettyTable'''

    _individuals_table = PrettyTable(['ID', 'Name', 'Gender', 'Birthday',
        'Alive', 'Death', 'Child', 'Spouse'])
    for k, v in INDIs.items():
        _is_alive = 'True'
        if v.death != 'N/A':
            _is_alive = 'False'
        _individuals_table.add_row([v.indiid, v.name, v.gender, v.birthday,
            _is_alive, v.death, v.child, v.spouse])
    print(_individuals_table)

def print_families():
    '''Print all families using PrettyTable'''

    _families_table = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID',
        'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
    for k, v in FAMs.items():
        _families_table.add_row([v.famid, v.married, v.divorced, v.husbandid,
            INDIs[v.husbandid].name, v.wifeid, INDIs[v.wifeid].name,
            v.children])
    print(_families_table)

class Individual(object):
    '''Class represent an Individual'''

    def __init__(self, indiid):
        self.indiid = indiid
        self.name = ''
        self.gender = ''
        self.birthday = ''
        self.death = 'N/A'
        self.child = 'N/A'
        self.spouse = 'N/A'


class Familie(object):
    '''Class represent a family'''

    def __init__(self, famid):
        self.famid = famid
        self.married = ''
        self.divorced = 'N/A'
        self.husbandid = ''
        self.wifeid = ''
        self.children = []


