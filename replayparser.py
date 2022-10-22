from urllib.request import Request, urlopen

req = Request('https://replay.pokemonshowdown.com/gen8vgc2022-1688203768-ern0p8wp16ja3eto2mxkkjtwhjg8bippw', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req,timeout=10).read()
str = webpage.decode('utf-8').split('\n')
player1 = ''
player2 = ''
team1 = []
team2 = []
comp1 = []
comp2 = []
winner = 0

def normalizeName (name) : 
    if '-' not in name:
        return name
    if name.startswith(('Necrozma-', 'Kyurem-', 'Calyrex-', 'Ho-Oh', 'Porygon-Z')) :
        return name
    if name.endswith(('-F', '-Therian')):
        return name
    if name.endswith('-Gmax'):
        return name[:len(name)-5]
    if name.endswith('-*'):
        return name[:len(name)-2]
    
# TODO: Deal with Porygon-Z exception
def getCompIndex(team, comp) :
    compNumber = []
    for pokeT in team :
        for pokeC in comp :
            if pokeT == pokeC.split('-')[0] :
                compNumber.append(team.index(pokeT)+1)
    return compNumber
    
for line in str:
    args = line.split('|')
    argc = len(args)
    if argc<2 or args[1]=='':
        continue  
    match args[1]:
        case 'player':
            if args[2]=='p1':
                player1=args[3]
            else : player2=args[3]
        case 'poke':
            if args[2]=='p1':
                team1.append(normalizeName(args[3].split(',')[0]))
            else : team2.append(normalizeName(args[3].split(',')[0]))
        case 'switch':
            pos = args[2].split(':')[0]
            poke = args[3].split(',')[0]
            match pos :
                case 'p1a' | 'p1b' : 
                    if poke not in comp1 :
                        comp1.append(poke)
                case 'p2a' | 'p2b' :
                    if poke not in comp2 :
                        comp2.append(poke)
        case 'win' :
            if args[2]==player1:
                winner = 1
            else : winner = 2       
     
print("TEAMS:") 
print(team1)
print(team2)
print("COMPS:")
print(getCompIndex(team1,comp1))
print(getCompIndex(team2,comp2))
print("WINNER:")
print(winner)