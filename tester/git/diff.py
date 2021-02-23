import regex
from typing import Optional, Tuple#
from enum import Enum

class DiffType(Enum):
	create: 'create'
	change: 'change'
	delete: 'delete'


class Diff:
	def __init__(self, diff_type: DiffType, filepath: str, change_range: Optional[Tuple[int, int]]):
		pass

def diff(paths):
	difflist = []
	changelist = []

	for diff in difflist:
		pass

	return changelist
