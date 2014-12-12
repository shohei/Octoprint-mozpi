var snake = require('to-snake-case'); 

var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({ port: 8080 });

var ws_list = {};
var manager;

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    parseMessage(ws,message);
  });
});

var parseMessage = function(ws,message){
    msg_json = JSON.parse(message);
    if(msg_json.id!=null){
        var place = msg_json.id.place;
        var printer = msg_json.id.printer;
        var id = place +" "+ printer;
        var client = snake(id);
        // if(ws_list.hasOwnProperty(client)){
        //     console.log('client id already exists');
        //     return;
        // }
        console.log('Printer ['+printer+'] from ['+place+'] is now connected.');
        ws_list[client] = ws;
        if(manager!=null){
            console.log("updating manager info");
            var clients_array = Object.keys(ws_list);
            manager.send(clients_array.toString());
        }
    }
    if(msg_json.key=="localgarage-owners"){
        console.log('owner connected');
        manager = ws;
        var clients_array = Object.keys(ws_list);
        manager.send(clients_array.toString());
    }
}

