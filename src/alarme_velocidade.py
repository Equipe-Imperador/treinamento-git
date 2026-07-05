def ver_velocidade(velocidade):
    LIMITE_VELOCIDADE = 50
    if velocidade > LIMITE_VELOCIDADE:
        print(f"\a[ALERTA DE VELOCIDADE] Velocidade atual de {velocidade}km/h excede o limite de {LIMITE_VELOCIDADE}km/h")
        return True
    return False
    

