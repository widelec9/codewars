import re


def insert_spaces(newline, width):
	spaces_pos = [m.start() for m in re.finditer(' ', newline)]
	spaces_left = width - len(newline)

	if len(spaces_pos) > 0 and spaces_left > 0:
		spaces = [' ' * (spaces_left // len(spaces_pos)) for i in range(0, len(spaces_pos))]
		spaces_left -= (spaces_left // len(spaces_pos)) * len(spaces_pos)
		for i in range(0, spaces_left):
			spaces[i] += ' '
			spaces_left -= 1
		shift = 0
		for i in range(0, len(spaces_pos)):
			newline = newline[:spaces_pos[i] + shift] + spaces[i] + newline[spaces_pos[i] + shift:]
			shift += len(spaces[i])
	return newline


def justify(text, width):
	start = 0
	out = ''
	while start < len(text):
		if start + width < len(text):
			stop = len(re.sub(r'(.*)\s.*$', r'\1', text[:start+width])) if not text[start + width].isspace() else start + width
			newline = text[start:stop]
			start = stop + 1
			newline = insert_spaces(newline, width)
		else:
			newline = text[start:]
			start = len(text)
		out += newline + '\n'
	return out[:-1]