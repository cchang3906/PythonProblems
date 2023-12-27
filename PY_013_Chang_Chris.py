glossary = {'insert':'adding terms in a list', 'del':'deleting terms in a list', 'print':'outputing a result in the form of a text', 'if':'asking for a specific condition', 'for':'looping'}
# print(f"insert: {glossary['insert']}")
# print(f"del: {glossary['del']}")
# print(f"print: {glossary['print']}")
# print(f"if: {glossary['if']}")
# print(f"for: {glossary['for']}")

for term, defin in glossary.items():
	print(f"{term.title()}: {defin}")