ns,ss,es,ws = "-n", "-s", "-e","-w"
def collide(a,b):
	if a != "-" and a==b:
		return True
	return False
combos = []
for n1 in ns:
	for s1 in ss:
		for e1 in es:
			for w1 in ws:
				for n2 in ns:
					for s2 in ss:
						for e2 in es:
							for w2 in ws:
								if collide(n1,n2) or collide(s1,s2) or collide(e1,e2) or collide(w1,w2):
									continue
								first = f"{n1}{s1}{e1}{w1}"
								second = f"{n2}{s2}{e2}{w2}"
								if first == "----" or second == "----":
									continue
								together = f"{first}:{second}"
								if len(together.replace("-","")) < 3:
									continue
								print(f"\"{first}:{second}\": \"\",")
								combos.append(together)
								pass
							pass
						pass
					pass
				pass
			pass
		pass
	pass
pass
print(len(combos))
