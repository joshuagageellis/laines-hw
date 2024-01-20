from typing import List

# Validate.
# Length
def is_len(s: str, l: int, err: str):
	if len(s) < l:
		raise ValueError(err)
	return True

# Contains text.
# Not case senitive.
def contains(s: str, t: str, err: str):
	s = s.lower()
	t = t.lower()
	if t not in s:
		raise ValueError(err)
	return True

# Contains at least one.
def contains_oneof(s: str, l: List[str], err: str):
	s = s.lower()
	for check in l:
		if check.lower() in s:
			return True
	raise ValueError(err)