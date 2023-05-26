import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

headers = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    headers += data

mysock.close()

# Decode the headers and data
headers = headers.decode()
header_end = headers.find('\r\n\r\n')
header_data = headers[:header_end]
body_data = headers[header_end + 4:]

# Extract the header values
header_lines = header_data.split('\r\n')
header_dict = {}
for line in header_lines:
    if ': ' in line:
        key, value = line.split(': ')
        header_dict[key] = value

# Print the header values
print("Last-Modified:", header_dict.get('Last-Modified'))
print("ETag:", header_dict.get('ETag'))
print("Content-Length:", header_dict.get('Content-Length'))
print("Cache-Control:", header_dict.get('Cache-Control'))
print("Content-Type:", header_dict.get('Content-Type'))

# Print the data
print(body_data)
