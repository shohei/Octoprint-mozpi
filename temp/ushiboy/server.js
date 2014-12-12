// http server
var connect = require('connect');
var httpServer = connect()
.use(connect.static(__dirname + '/webroot'))
.listen(1234);

// WebSocket Server
var WebSocketServer = require('websocket').server;
var wsServer = new WebSocketServer({
    httpServer : httpServer,
    autoAcceptConnections : true
});

// クライアント接続イベント
wsServer.on('connect', function(client) {
    // クライアントからのメッセージ受信イベント
    client.on('message', function(message) {
        if (message.type === 'utf8') {
            // 文字列だったら文字列としてそのまま送信
            client.sendUTF(message.utf8Data);
        } else if (message.type === 'binary') {
            // バイナリだったらバイナリとしてそのまま送信
            client.sendBytes(message.binaryData);
        } else {
            console.log('nanigashi');
        }   
    }); 
});

