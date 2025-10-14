
import random

lista = ['piedra', 'papel', 'tijeras']

while True:
    computadora = random.choice(lista)
    jugador = None

    while jugador not in lista:
        jugador = input('piedra, papel o tijeras?: ').lower()

    if jugador == computadora:
        print('Computadora: ', computadora)
        print('Jugador: ', jugador)
        print('Empate! ')
    elif jugador == 'piedra':
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste! ')
        elif computadora == 'tijeras':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste! ')
    elif jugador == 'papel':
        if computadora == 'tijeras':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste! ')
        elif computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste! ')
    elif jugador == 'tijeras':
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Perdiste! ')
        elif computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Ganaste! ')

    jugar_de_nuevo = input('Quieres jugar de nuevo? (si/no):').lower()

    if jugar_de_nuevo != 'si':
        break

print('Fin de la partida, Adios!')

