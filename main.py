import dht                      # Importa bibliotecas
from machine import Pin
from time import sleep

sensor = dht.DHT22(Pin(15))     # Define a entrada
rele = Pin(2, Pin.OUT)          # Define a saída
rele.on()

while True:
    try:
        sensor.measure()                    # Recebe dados do sensor
        temp = sensor.temperature()         # Guarda o valor recebido da temperatura na variável "Temp"

        print ("\n----------------")
        print (f"Temperatura:{temp:.1f}ºC") # Exibe a temperatura no terminal
        print ("----------------")

        if temp >= 26:                                          # Sempre que a temperatura for maior que 26ºC
            rele.off()                                           # o relé será ativado
            print ("\n* Sistema de ventilção acionado *")
        elif temp < 25:                                                   # Caso contrário será desativado
            rele.on()
            print("\n* Sistema em estado normal *")

        sleep(3)                                            # Espera 3 segundos
        
    except OSError as e:                                                            
        print ("Falha na leitura (ETIMEDOUT). Verifique ligaçoes/alimentação")      # Exibe uma mensagem se houver erro