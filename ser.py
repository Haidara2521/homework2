import socket
import threading


QUESTION = {
"1) in which continent is Russia located ?\na.Asia\nb.Europe\n": "b", 
"2) in which continent is Syria located ?\na.Asia\nb.Europe\n": "a", 
"3) in which continent is Spain located ?\na.Asia\nb.Europe\n": "b", 
"4) in which continent is Iraq located ?\na.Asia\nb.Europe\n": "a", 
"5) in which continent is Jordan located ?\na.Asia\nb.Europe\n": "a",
"6) in which continent is France located ?\na.Asia\nb.Europe\n": "b", 
"7) in which continent is Italy located ?\na.Asia\nb.Europe\n": "b", 
"8) in which continent is Lebanon located ?\na.Asia\nb.Europe\n": "a", 
"9) in which continent is Iran located ?\na.Asia\nb.Europe\n": "a", 
"10) in which continent is India located ?\na.Asia\nb.Europe\n": "a", 
"11) in which continent is Portugal located ?\na.Asia\nb.Europe\n": "b", 
"12) in which continent is Austria located ?\na.Asia\nb.Europe\n": "b", 
"13) in which continent is Holland located ?\na.Asia\nb.Europe\n": "b", 
"14) in which continent is Germany located ?\na.Asia\nb.Europe\n": "b", 
"15) in which continent is UAE located ?\na.Asia\nb.Europe\n": "a", 
"16) in which continent is Qatar located ?\na.Asia\nb.Europe\n": "a", 
"17)in which continent is yemen located ?\na.Asia\nb.Europe\n": "a", 
"18) in which continent is Denmark located ?\na.Asia\nb.Europe\n": "b", 
"19) in which continent is Kuwait located ?\na.Asia\nb.Europe\n": "a", 
"20) in which continent is Croatia located ?\na.Asia\nb.Europe\n": "b"
}
scores = {}

def h_clien(clien_sock, address):
    for q in QUESTION.keys():
        clien_sock.send(q.encode())
        answer1 = clien_sock.recv(1024).decode().strip()

        if answer1 == QUESTION[q]:
            scores[address] = scores.get(address, 0) + 1

    if address in scores:
        sc_message = 'Your score: {}/{}'.format(scores[address], len(QUESTION))
        clien_sock.send(sc_message.encode())

    clien_sock.close()

def start_ser():
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_sock.bind(('localhost', 5555))
    ser_sock.listen(5)
    print('Server started.port 5555')

    while True:
        clien_sock, address = ser_sock.accept()
        print('New connection :', address)

        clien_thread = threading.Thread(target=h_clien, args=(clien_sock, address))
        clien_thread.start()


start_ser()

