import re


def shorten(s):
	ignore = ['the', 'of', 'in', 'from', 'by', 'with', 'and', 'or', 'for', 'to', 'at', 'a']
	return ''.join([w[0].upper() for w in s.split('-') if w not in ignore])


def generate_bc(url, separator):
	splt = re.match(r'(https?:\/\/)?(.*)', url).group(2).rstrip('/').split('/')
	if 'index' in splt[-1]:
		splt.pop(-1)
	bcs = []
	for i, s in enumerate(splt):
		s = re.match(r'(.*?)([\?\#\.]|$)', s).group(1)
		sshort = (shorten(s) if len(s) > 30 else s).replace('-', ' ').upper()
		bcs += [('/', 'HOME')] if i == 0 else [('', sshort)] if i == len(splt) - 1 else [(bcs[i-1][0] + s + '/', sshort)]
	return separator.join(['<a href="{}">{}</a>'.format(bc[0], bc[1]) if i < len(bcs) - 1 else '<span class="active">{}</span>'.format(bc[1]) for i, bc in enumerate(bcs)])