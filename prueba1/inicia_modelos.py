import os
from multiprocessing import Process

def run_modelo_bert_base():
    os.system('python /app/modelo_bert_base.py')

def run_modelo_distilbert():
    os.system('python /app/modelo_distilbert.py')

def run_modelo_albert_tiny():
    os.system('python /app/modelo_albert_tiny.py')

if __name__ == '__main__':
    # Crear procesos para cada modelo
    proceso1 = Process(target=run_modelo_bert_base)
    proceso2 = Process(target=run_modelo_distilbert)
    proceso3 = Process(target=run_modelo_albert_tiny)

    # Iniciar los procesos
    proceso1.start()
    proceso2.start()
    proceso3.start()

    # Esperar a que todos los procesos terminen
    proceso1.join()
    proceso2.join()
    proceso3.join()



