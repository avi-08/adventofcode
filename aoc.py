#!/usr/bin/python

import os
import subprocess
import argparse
import sys
import logging

from typing import List


BASE = os.path.dirname(os.path.abspath(__file__))
EVENT_PREFIX = "event"
DAY_PREFIX = "day"
EXECUTABLE = "solution.py"


class EventCommand:
    def __init__(self, event, sub_commands=None, parser=None):
        self.event = event
        self.sub_commands = sub_commands
        self.parser = parser
    
    def __str__(self):
        return f"(Event: {self.event}, Sub-commands: {self.sub_commands}, Parser: {self.parser})"
    
    def get_event(self):
        return self.event
    
    def get_sub_commands(self):
        return self.sub_commands
    
    def get_parser(self):
        return self.parser
    
    def set_event(self, event):
        self.event = event
        
    def set_sub_commands(self, sub_commands):
        self.sub_commands = sub_commands
    
    def set_parser(self, parser):
        self.parser = parser


def get_commands() -> List[EventCommand]:
        events = [x for x in os.listdir(BASE) if os.path.isdir(x) and x.startswith(EVENT_PREFIX)]
        opts = []
        for event in events:
            event_abs = os.path.join(BASE, event)
            days = [x for x in os.listdir(event_abs) if os.path.isdir(os.path.join(event_abs, x)) and x.startswith(DAY_PREFIX)]
            days.sort()
            opts.append(EventCommand(event=event, sub_commands=days))
        return opts


def execute_aoc_solution(args):
    file_to_execute = os.path.join(BASE, args.event, args.day, EXECUTABLE)
    if not os.path.isfile(file_to_execute):
        logging.error(f"No such file exists: {file_to_execute}")
        raise ValueError(f"No such file exists: {file_to_execute}")
    
    logging.info(f"Executing solution of {args.day} from event {args.event}")
    
    cmd = [sys.executable, file_to_execute]
    
    if args.verbose:
        cmd.append("--verbose")
    if args.run_sample:
        cmd.append("--run-sample")
    
    try:
        logging.debug(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd)
    except Exception as ex:
        logging.error(f"Failed to execute, error occurred: {ex}")
        raise ex
    
    logging.info(f"Completed execution of {args.day} from event {args.event}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run adventofcode problem solutions")
    subparsers = parser.add_subparsers(title="event", dest="event", required=True, help='Run problem solutions for adventofcode events')

    cmds = get_commands()

    for event_cmd in cmds:
        event_cmd.set_parser(subparsers.add_parser(event_cmd.get_event(), help=f'Run problem solutions for adventofcode {event_cmd.get_event()}'))
        event_cmd.get_parser().add_argument("-d", "--day", choices=event_cmd.get_sub_commands(), help="Problem of the day")
        event_cmd.get_parser().add_argument("-v", "--verbose", action="store_true", help="Log with more verbosity")
        event_cmd.get_parser().add_argument('-s', '--run-sample', action='store_true', help='Run with sample.txt; if omitted, runs with input.txt')
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    execute_aoc_solution(args)
