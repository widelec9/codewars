import numpy as np, re


def top_3_words(text):
	text = re.sub(r'\s{2,}', ' ', re.sub(r'([^A-Za-z\s\']|\s+\'+\s+)', ' ', text).strip()).lower()
	if text == '':
		return []
	else:
		words, counts = np.unique(np.array(text.split(' ')), return_counts=True)
		freq = []
		for i in range(0, min(len(words), 3)):
			idx = np.where(counts == max(counts))[0][0]
			freq += [words[idx]]
			words = np.delete(words, idx)
			counts = np.delete(counts, idx)
		return freq