import multiprocessing
import time
import sys
from multiprocessing import Queue, Pipe
from datetime import datetime


def process_a(input_queue, output_conn, log_file):
    while True:
        if not input_queue.empty():
            message = input_queue.get()  # Получаем сообщение из очереди
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(
                f"({timestamp}) Процесс A получил сообщение: {message}\n")
            print(f"({timestamp}) Процесс A получил сообщение: {message}")
            message = message.lower()  # Приводим к нижнему регистру
            # Передаем сообщение в процесс B через Pipe
            output_conn.send(message)
        time.sleep(1)


def process_b(input_conn, output_conn, log_file):
    while True:
        if input_conn.poll(5):  # Проверяем, есть ли данные для чтения из Pipe
            message = input_conn.recv()  # Получаем сообщение из процесса A через Pipe
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(
                f"({timestamp}) Процесс B получил сообщение: {message}\n")
            print(f"({timestamp}) Процесс B получил сообщение: {message}")
            encoded_message = encode_rot13(message)  # Кодируем сообщение ROT13
            log_file.write(
                f"({timestamp}) Процесс B отправил сообщение: {encoded_message}\n")
            print(encoded_message)  # Выводим закодированное сообщение в stdout
            # Отправляем закодированное сообщение в главный процесс
            output_conn.send(encoded_message)


def encode_rot13(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded = ""
    for char in message:
        if char.isalpha():
            shifted_index = (alphabet.index(char) + 13) % 26
            encoded += alphabet[shifted_index]
        else:
            encoded += char
    return encoded


if __name__ == '__main__':
    # Создаем очередь для обмена данными между главным процессом и процессом A
    input_queue = Queue()
    conn_a, conn_b = Pipe()  # Создаем Pipe для обмена данными между процессами A и B

    with open("interaction_log.txt", "a") as log_file:
        proc_a = multiprocessing.Process(
            target=process_a, args=(input_queue, conn_a, log_file))
        proc_b = multiprocessing.Process(target=process_b, args=(
            conn_b, None, log_file))  # Pass None instead of sys.stdout

        proc_a.start()
        proc_b.start()

        try:
            while True:
                message = input("Введите сообщение: ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(
                    f"({timestamp}) Главный процесс отправил сообщение: {message}\n")
                print(
                    f"({timestamp}) Главный процесс отправил сообщение: {message}")
                # Помещаем сообщение в очередь для процесса A
                input_queue.put(message)
        except KeyboardInterrupt:
            proc_a.terminate()
            proc_b.terminate()
            proc_a.join()  # Wait for process A to finish
            proc_b.join()  # Wait for process B to finish
