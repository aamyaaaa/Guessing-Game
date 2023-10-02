import socket
import random

IP = "127.0.0.1"
PORT = 65432
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()
print("Server is waiting for a connection...")
connection, address = server_socket.accept()
print(f"Connection from {address} has been established!")
# Server chooses a random number between 1 and 100
chosen_number = random.randint(1, 100)
attempts = 0
while True:
    data = connection.recv(1024).decode()
    if not data:
        break

    guess = int(data)
    attempts += 1

    if guess < chosen_number:
        connection.sendall(b"LOW")
    elif guess > chosen_number:
        connection.sendall(b"HIGH")
    else:
        connection.sendall(b"CORRECT")
        print(f"Client guessed the number {chosen_number} in {attempts} attempts!")
        break

connection.close()
