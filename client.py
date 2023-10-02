import socket

IP = "127.0.0.1"
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

print("Connected to the server!")
print("Try to guess the number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")
    client_socket.sendall(guess.encode())

    response = client_socket.recv(1024).decode()

    if response == "LOW":
        print("Your guess is too low!")
    elif response == "HIGH":
        print("Your guess is too high!")
    elif response == "CORRECT":
        print(f"Congratulations! You've guessed the correct number!")
        break

client_socket.close()
