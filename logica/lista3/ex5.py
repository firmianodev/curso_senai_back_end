def retorna_segundos_em_hotas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = minutos % 60 // 60

    return horas, minutos, segundos

def main():
    tempo = retorna_segundos_em_hotas(5400) 
    print(f"{tempo[0]} horas, {tempo[1]} minutos e {tempo[2]} segundos")

if __name__ == "__main__":
    main()