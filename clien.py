import socket

def s_c():
    ser_address = ('localhost', 5555)
    clien_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clien_sock.connect(ser_address)
    
    for i in range (20):
        q = clien_sock.recv(1024).decode()
        print("Question:", q)
        answer = input("Your answer (a/b): ")
        clien_sock.sendall(answer.encode())
    
    final_s = clien_sock.recv(1024).decode()
    print("score" , final_s)


s_c()
