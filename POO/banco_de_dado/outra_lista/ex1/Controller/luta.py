def lutar (p1, p2):
    if p1.hp >= 0 or p2.hp >= 0:
        if p1.hp == p2.hp:
            print(f'{p1.nome} ganhou')
            return p1.atacar(p2)
        else:
            print(f'{p2.nome} ganhou')
            return p2.atacar(p1)