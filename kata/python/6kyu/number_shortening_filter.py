def shorten_number(prefixes, base):
	def simplify(instr):
		divs = [(base ** i, prefixes[i]) for i in range(0, len(prefixes))]
		try:
			num = int(instr)
			for i in range(len(divs)-1, -1, -1):
				if num // divs[i][0] > 0:
					return str(num // divs[i][0]) + divs[i][1]
		except (ValueError, TypeError) as e:
			return str(instr)
	return simplify