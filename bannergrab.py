import socket

def BannerGrabber(addr, port):
  socket.setdefaulttimeout(2)
  bannergrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    bannergrab.connet((addr, port))
    bannergrab.send(b"GET HTTP/1.1 \r\n")
    banner = bannergrab.recv(1024)
    bannergrab.close()
    print(banner), "\n"
  except:
    print("Cannot connect to port"), port

BannerGrabber('google.com', 80)
