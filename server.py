from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from urllib.parse import unquote
import os

# Function to handle encryption
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            unicode_point = ord(char)
            if char.isupper():
                encrypted_unicode = ((unicode_point - 65 + shift) % 26) + 65
            else:
                encrypted_unicode = ((unicode_point - 97 + shift) % 26) + 97
            encrypted_text += chr(encrypted_unicode)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt
def decrypt_caesar_cipher(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)

# HTTPRequestHandler class
class HTTPRequestHandler(BaseHTTPRequestHandler):

    # GET method
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("text_encryption.html", "rb") as file:
                self.wfile.write(file.read())
        elif parsed_path.path == "/encrypt":
            params = parse_qs(parsed_path.query)
            text = unquote(params['text'][0])
            shift = int(params['shift'][0])
            encrypted_text = caesar_cipher(text, shift)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(encrypted_text.encode())
        elif parsed_path.path == "/decrypt":
            params = parse_qs(parsed_path.query)
            encrypted_text = unquote(params['text'][0])
            shift = int(params['shift'][0])
            decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(decrypted_text.encode())
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

# Main function
def main():
    try:
        # Create an HTTP server and define the handler
        server = HTTPServer(('localhost', 8080), HTTPRequestHandler)
        print('Starting server, use <Ctrl-C> to stop')
        # Start the server
        server.serve_forever()
    except KeyboardInterrupt:
        print('Server interrupted')
        server.socket.close()

if __name__ == '__main__':
    main()
