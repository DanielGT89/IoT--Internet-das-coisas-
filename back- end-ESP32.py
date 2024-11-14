from machine import Pin
import urequests
import time
import ntptime
import network
import gc
import socket


TOKEN = ''
CHAT_ID = ''
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


def send_telegram_message(message):
    try:
        response = urequests.get(f'{URL}?chat_id={CHAT_ID}&text={message}')
        print(response.text)
        response.close()  
    except Exception as e:
        print("Erro ao enviar mensagem:", e)


def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    print("Conectado ao Wi-Fi")


pirPin = Pin(17, Pin.IN)  #
ledPin = Pin(2, Pin.OUT)


no_motion_count = 0 
check_count = 0      


def get_local_hour():
    year, month, day, hour, minute, second, _, _ = time.localtime()
    hour -= 3  
    if hour < 0:
        hour += 24  
    return hour


def is_within_time():
    hour = get_local_hour()  
    return 13 <= hour < 17  


def print_memory():
    gc.collect()  
    print("Memória disponível:", gc.mem_free(), "bytes")


NTP_SERVER = "pool.ntp.org"

def set_time():
    try:
        addr = socket.getaddrinfo(NTP_SERVER, 123)[0][-1]  
        ntptime.NTP_SERVERS = [addr]  
        ntptime.settime()  
        print("Hora ajustada com sucesso.")
    except Exception as e:
        print("Erro ao definir hora:", e)


connect_wifi('ROTEADOR', '9230A9230')
time.sleep(5)  
set_time()  


while True:
    try:
        if is_within_time(): 
            if pirPin.value() == 1:  
                print("Movimento detectado.")
                ledPin.on() 
                no_motion_count = 0  
            else:
                print("Sem movimento.")
                ledPin.off()  
                no_motion_count += 1  
            
            check_count += 1 
            
            
            if check_count >= 2:
                if no_motion_count >= 2:  
                    send_telegram_message("Aviso: Não há movimento na sala vania.")
                
                check_count = 0
                no_motion_count = 0  
            
            print_memory()  
            time.sleep(5)  
        else:
            print("Fora do horário de monitoramento.")
            ledPin.off()  
            time.sleep(600)  
    except Exception as e:
        print("Erro no loop principal:", e)
        time.sleep(5)  

