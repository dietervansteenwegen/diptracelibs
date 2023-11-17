# -*- coding: utf-8 -*-
import pathlib

global issues
issues: list = []


def check_file(inp: pathlib.Path) -> None:
    with open(inp) as src:
        for line_no, line in enumerate(src, start=1):
            if '\t' in line:
                issues.append(f'\\t on line {line_no} in {inp}.')
            if not line.startswith('<'):
                issues.append(f'Line {line_no} in {inp} does not start with <.')


def main() -> None:
    for inp_xml in pathlib.Path.cwd().glob('*.*xml'):
        check_file(inp_xml)
    if issues:
        print(f'Found {len(issues)} issues:')
        for issue in issues:
            print(issue)
    else:
        print('No issues found.')


if __name__ == '__main__':
    main()
