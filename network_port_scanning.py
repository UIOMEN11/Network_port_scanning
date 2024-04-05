from socket import *
import time

if __name__ == '__main__':
    start_time = time.time()
    target = input("Enter target host for scanning: ")
    t_IP = gethostbyname(target)
    print("Start scanning on host: ", t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))

        if conn == 0:
            print("Port %d: OPEN" % (i,))
        s.close()

    print("Time taken: ", time.time() - start_time)
