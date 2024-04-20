import socket
def server():
    host = socket.gethostname()                   # 獲取主機名稱
    port = 5000                                   # 設定連接埠號
    server_socket = socket.socket()               # 創建套接字對象
    server_socket.bind((host, port))              # 將套接字綁定到指定的主機和連接埠
    server_socket.listen(2)                       # 設定最大等待連線數為2，可以同時處理兩個客戶端的連線請求
    conn, address = server_socket.accept()        # 等待客戶端的連線請求，接受並返回連線對象(conn)和客戶端地址(address)
    print("Connection from: " + str(address))     # 顯示連線來源的客戶端地址
    conn.settimeout(20)                           # 設定連線的超時時間為20秒
    try:
        while True:
            data = conn.recv(1024).decode()       # 接收來自客戶端的訊息並解碼
            if not data:                          #client輸入goodbye，break迴圈
                break
            print("from client : " + str(data))   # 顯示來自客戶端的訊息
            data = input('server ->')             # 提示用戶輸入訊息
            conn.send(data.encode())              # 將輸入的訊息編碼並發送給客戶端
    except socket.timeout:
        print("Timeout!!")                        # 顯示連線超時的訊息
    finally:
        conn.close()                              # 關閉連線
        server_socket.close()                     # 關閉套接字
    
if __name__ == '__main__':
    server()  
