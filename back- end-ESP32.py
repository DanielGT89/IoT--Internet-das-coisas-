from machine import Pin
import urequests
import time
import ntptime
import network
import gc
import socket

# Configurações do bot do Telegram
TOKEN = '8056710112:AAGlnoLuwOZE5acNROCg_7LGOqpYldNbCtg'
CHAT_ID = '2109894552'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# Função para enviar mensagem ao Telegram
def send_telegram_message(message):
    try:
        response = urequests.get(f'{URL}?chat_id={CHAT_ID}&text={message}')
        print(response.text)
        response.close()  # Libera o recurso da resposta
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

# Conectar-se à rede Wi-Fi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    print("Conectado ao Wi-Fi")

# Inicializar o sensor PIR e o LED
pirPin = Pin(17, Pin.IN)  # GPIO 17 (D1 no ESP32)
ledPin = Pin(2, Pin.OUT)

# Contadores para verificações
no_motion_count = 0  # Contador de verificações sem movimento
check_count = 0      # Contador total de verificações

# Função para obter a hora local
def get_local_hour():
    year, month, day, hour, minute, second, _, _ = time.localtime()
    hour -= 3  # Ajuste para UTC-3
    if hour < 0:
        hour += 24  # Se a hora ficar negativa, ajuste para o intervalo correto
    return hour

# Função para verificar se estamos no intervalo das 13h às 17h
def is_within_time():
    hour = get_local_hour()  # Obtém a hora local ajustada
    return 13 <= hour < 17  # Verifica se está entre 13h e 17h

# Função para verificar a memória disponível
def print_memory():
    gc.collect()  # Coleta lixo para liberar memória
    print("Memória disponível:", gc.mem_free(), "bytes")

# Definindo um servidor NTP diferente
NTP_SERVER = "pool.ntp.org"

def set_time():
    try:
        addr = socket.getaddrinfo(NTP_SERVER, 123)[0][-1]  # Obtém o endereço do servidor NTP
        ntptime.NTP_SERVERS = [addr]  # Define o servidor NTP
        ntptime.settime()  # Define a hora
        print("Hora ajustada com sucesso.")
    except Exception as e:
        print("Erro ao definir hora:", e)

# Conectar ao Wi-Fi (preencha com os dados da sua rede)
connect_wifi('ROTEADOR', '9230A9230')
time.sleep(5)  # Aguarda 5 segundos para estabilizar a conexão
set_time()  # Chama a função para definir a hora

# Lógica principal
while True:
    try:
        if is_within_time():  # Verifica se está entre 13h e 17h
            if pirPin.value() == 1:  # Movimento detectado
                print("Movimento detectado.")
                ledPin.on()  # Acende o LED
                no_motion_count = 0  # Reseta o contador de sem movimento
            else:
                print("Sem movimento.")
                ledPin.off()  # Apaga o LED
                no_motion_count += 1  # Incrementa o contador de sem movimento
            
            check_count += 1  # Incrementa o contador total de verificações
            
            # Se já tiver feito 10 verificações
            if check_count >= 2:
                if no_motion_count >= 2:  # Se houver 2 verificações sem movimento
                    send_telegram_message("Aviso: Não há movimento na sala vania.")
                # Reseta os contadores após 10 verificações
                check_count = 0
                no_motion_count = 0  # Reseta o contador de sem movimento após as 10 verificações
            
            print_memory()  # Imprime a memória disponível
            time.sleep(5)  # Aguarde 10 segundos antes da próxima verificação
        else:
            print("Fora do horário de monitoramento.")
            ledPin.off()  # Certifique-se de que o LED está apagado fora do horário
            time.sleep(600)  # Aguardar 10 minutos fora do horário
    except Exception as e:
        print("Erro no loop principal:", e)
        time.sleep(5)  # Espera antes de tentar novamente em caso de erro

