def matrix(a, b, n):
	m = sum(len(row) for row in a)
	out = ""
	out += "SparseArray[{"
	boxnum = 1
	for i in range(1, len(a) + 1):
		for j in range(1, len(a[i-1]) + 1):
			if j < len(a[i-1]):
				out += f"{{{boxnum}, {boxnum+1}}} -> 1,"
			if a[i-1][j-1] != 0:
				out += f"{{{m + 1}, {boxnum}}} -> {a[i-1][j-1]},"
			if b[i-1][j-1] != 0:
				out += f"{{{boxnum}, {m + n}}} -> {b[i-1][j-1]},"
			boxnum += 1
	for i in range(m + 1, m + n + 1):
		if i != m + n:
			out += f"{{{i}, {i+1}}} -> 1,"
	if out[-1] == ",":
		out = out[:-1]
	out += f"}}, {{{m + n}, {m + n}}}]\n"
	return out
