require 'websocket'


@handshake = WebSocket::Handshake::Client.new(url: 'ws://localhost:4567', headers: { 'Cookie' => 'SESSIONID=1234' })
# Create request
@handshake.to_s # GET /demo HTTP/1.1
                # Upgrade: websocket
                # Connection: Upgrade
                # Host: example.com
                # Cookie: SESSIONID=1234
                # Sec-WebSocket-Origin: http://example.com
                # Sec-WebSocket-Version: 13
                # Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==

# Parse server response
@handshake << <<EOF
HTTP/1.1 101 Switching Protocols\r
Upgrade: websocket\r
Connection: Upgrade\r
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\r
\r
EOF

# All data received?
@handshake.finished?

# No parsing errors?
@handshake.valid?


