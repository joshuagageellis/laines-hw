from typing import Dict, Tuple, List, Callable
from lib.validators import is_len, contains_oneof

# User input config.
UserParam = Tuple[str, List[Tuple[Callable, List]]]
UserConfig = Dict[str, UserParam]
user_config: UserConfig  = {
	"name": (
		"Please provide your name",
		[(
			is_len,
			[2, "Name must be at least 2 characters long."]
		)]
	),
	"country_abbr": (
		"Please provide your country abbreviation",
		[(
			is_len,
			[2, "Country must be at least 2 characters long."]
		),
		(
			contains_oneof,
			[["usa", "ca", "uk"], "Country must be one of: USA, CA, UK."]
		)]
	),
}

user_config_props_len = len(user_config)

users = []

def validate(val: str, param_config: UserParam):
	for func, args in param_config[1]:
		# Will raise error if invalid.
		func(val, *args)

def get_user(cfg: UserConfig = user_config):
	cfgl = len(cfg)
	out = {}
	while len(out) < cfgl:
		for k, v in cfg.items():
			state = True
			while state:
				try:
					nV = input(f"{v[0]}: ")
					# Validate. Throws.
					validate(nV, v)
					out[k] = nV
					state = False
					break
				except ValueError as e:
					print(e)
	return out

users = [get_user() for _ in range(2)]
print(users)