valasz = input('Jön ma Henrik kosarazni? igen/nem ')
valasz1 = input('Jön ma Hanna kosarazni? igen/nem ')


if valasz and valasz1 == "igen":
    print('Mindeketten jönnek kosarazni.')
elif valasz and valasz1 == "nem":
    print('Egyikük se jön kosarazni.')
else:
    print('Csak az egyikük jön kosarazni.')
print('>> A program vége! <<')
