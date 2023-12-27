insect = ['ants', 'butterflies', 'beetle', 'ladybugs', 'cicadas']
print("\nUnsorted")
print(insect)

print("\nTemp sorted")
print(sorted(insect))

print("\nTemp reverse sorted")
print(sorted(insect,reverse=True))

print("\nPerm reverse sorted")
insect.reverse()
print(insect)

print("\nUnsorted")
insect.reverse()
print(insect)

print("\nPerm sorted")
insect.sort()
print(insect)

print(f"\nlength of list: {len(insect)}")