require 'websocket'
require 'sinatra'

@handshake = WebSocket::Handshake::Server.new

# Parse client request
@handshake << <<EOF
GET /demo HTTP/1.1\r
Upgrade: websocket\r
Connection: Upgrade\r
Host: example.com\r
Sec-WebSocket-Origin: http://example.com\r
Sec-WebSocket-Version: 13\r
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r
\r
EOF

# All data received?
@handshake.finished?

# No parsing errors?
@handshake.valid?

# Create response
@handshake.to_s # HTTP/1.1 101 Switching Protocols
                # Upgrade: websocket
                # Connection: Upgrade
                # Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

