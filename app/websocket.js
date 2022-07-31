
class MeckWebserver {
    constructor() {
        this.WebSocketServer = require('ws');;
        this.wss = new this.WebSocketServer.Server({ port: 8080 });
    }

    pooling(){
        // Creating connection using websocket
        this.wss.on("connection", ws => {
            console.log("new client connected");
            // sending message
            ws.on("message", data => {
                console.log(`Client has sent us: ${data}`)
            });
            // handling what to do when clients disconnects from server
            ws.on("close", () => {
                console.log("the client has connected");
            });
            // handling client connection error
            ws.onerror = function () {
                console.log("Some Error occurred")
            }
        });

    }
  }

  
// inicializador
// const server = new MeckWebserver();
// server.pooling();