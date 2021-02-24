import subprocess
import re
from typing import Optional, List, Tuple
from enum import Enum

DIFF_REGEX = re.compile(r"^diff --git a.*b(.*?)\n(\n|.)*?@@ [+-]\d+,\d+ [+-](\d+),(\d+)", flags=re.MULTILINE)


class DiffType(Enum):
	Create = 'Create'
	Change = 'Change'
	Delete = 'Delete'


class Diff:
	def __init__(self, diff_type: DiffType, filepath: str, change_range: Optional[Tuple[int, int]]):
		self.diff_type = diff_type
		self.filepath = filepath
		self.change_range = change_range

	def __repr__(self):
		return f"Diff object >> type: {self.diff_type}, file: {self.filepath}, lines: {self.change_range}>"


def diff():
	changelist = []

	diff_output = subprocess.check_output(["git", "diff-index", "-p", "HEAD"]).decode('utf8')
	for d in re.finditer(DIFF_REGEX, diff_output):
		filepath = d.group(1)
		start = int(d.group(3))
		end = int(d.group(4))
		changelist.append(Diff(DiffType.Change, filepath, (start, end)))

	return changelist


if __name__ == '__main__':
	print(diff())
