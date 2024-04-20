import socket

def client():
    host = socket.gethostname()                  # 獲取主機名稱
    port = 5000                                  # 設定連接埠號
    client_socket = socket.socket()              # 創建套接字對象
    client_socket.connect((host, port))          # 連接到伺服器
    message = input("client -> ")                # 提示用戶輸入訊息
    while message.lower().strip() != 'goodbye':  # 當輸入的訊息不是'goodbye'時執行迴圈
        client_socket.send(message.encode())     # 將輸入的訊息編碼並發送給伺服器
        data = client_socket.recv(1024).decode() # 接收伺服器發送的訊息並解碼
        print('from server: ' + data)            # 顯示伺服器發送的訊息
        message = input("client -> ")            # 再次提示用戶輸入訊息
    client_socket.close()                        # 關閉套接字

if __name__ == '__main__':
    client()  
