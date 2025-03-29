import random
import time

def sensor_movimento():
    return random.choice([True, False])

def sensor_temperatura():
    return random.uniform(18.0, 30.0)

while True:
    movimento = sensor_movimento()
    temperatura = sensor_temperatura()
    print(f"Movimento: {'Detectado' if movimento else 'Não detectado'}, Temperatura: {temperatura:.2f}°C")
    time.sleep(5)

    