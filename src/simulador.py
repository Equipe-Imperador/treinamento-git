import time
import random

# Variáveis globais para a Fase 2 (Linear)
# Na Fase 1, elas ainda não serão usadas.
rpm_atual = 1000
vel_atual = 0
temp_cvt_atual = 40
bateria_atual = 100

def ler_sensores():
    """
    Função responsável por ler (ou simular) os dados dos sensores do carro.
    """
    # G1: Motor (Marcha lenta ~1000, limite ~3800)
    rpm = random.randint(1000, 3800)
    
    # G2: Velocidade em km/h
    velocidade = random.randint(0, 60)
    
    # G3: Temperatura da CVT em °C
    temp_cvt = random.randint(40, 90)
    
    # G4: Nível da Bateria em %
    bateria = random.randint(10, 100)
    
    return rpm, velocidade, temp_cvt, bateria

def exibir_painel(rpm, velocidade, temp_cvt, bateria):
    """
    Função responsável por formatar e exibir os dados lidos no terminal.
    """
    print("-" * 40)
    print("PAINEL DE TELEMETRIA - BAJA IMPERADOR")
    print("-" * 40)
    print(f"Motor:        {rpm} RPM")
    print(f"Velocidade:   {velocidade} km/h")
    print(f"Temp. CVT:    {temp_cvt} °C")
    print(f"Bateria:      {bateria} %")
    print("-" * 40)
    print("Aperte Ctrl+C para sair.\n")

def main():
    print("Iniciando Simulador do Baja...\n")
    time.sleep(1)
    
    try:
        while True:
            # 1. Lê os dados
            rpm, vel, temp, bat = ler_sensores()
            
            # 2. Exibe os dados no painel
            exibir_painel(rpm, vel, temp, bat)
            
            # 3. Delay de telemetria
            time.sleep(1.5)
            
    except KeyboardInterrupt:
        print("\nSimulador encerrado. Até a próxima corrida!")

if __name__ == "__main__":
    main()