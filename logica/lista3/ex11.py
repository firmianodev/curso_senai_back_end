def mostra_conceito(media):
    if media >= 0 and media <= 4.9:
        return "D"
    elif media >= 5 and media <= 6.9:
        return "C"
    elif media >= 7 and media <= 8.9:
        return "B"
    elif media >= 9 and media <= 10:
        return "A"
    
def main():
    print(mostra_conceito(10))

if __name__ == "__main__":
    main()