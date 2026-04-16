def returna_idade_em_anos_meses_dias(anos, meses, dias):
    anos_em_dias = anos * 12 * 30.4375
    meses_em_dias = meses * 30.4375

    tempo_em_dias = anos_em_dias + meses_em_dias + dias
    return tempo_em_dias

def main():
    ex1 = returna_idade_em_anos_meses_dias(30, 8, 4)
    print(ex1)

if __name__ == "__main__":
    main()