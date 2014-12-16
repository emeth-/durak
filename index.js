var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var url = require('url');
app.use('/static', express.static(__dirname + '/vendor'));

var bodyParser = require('body-parser')
app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
    extended: true
}));

app.get('/', function(req, res){
    res.sendfile(__dirname + '/index.html');
});
app.get('/cardsdemo/', function(req, res){
    res.sendfile(__dirname + '/vendor/JavaScript-Playing-Cards-master/index.html');
});

app.post('/newRoom', function (req, res) {

    var room = req.body.room;

    if (room) {
        var nsp = io.of('/' + room);
        nsp.on('connection', function (socket) {
            console.log('someone connected to room ' + room);
            socket.emit('welcome', 'Thanks for joining ' + room);
            nsp.emit('someone joined', 'SOME NEW PERSON JOINED');
        });

    }
    res.send({status: 'success'});

    nsp.emit('hi', 'everyone!');
});

io.on('connection', function(socket){
    //console.log(socket);
    console.log('a user connected');
    socket.on('disconnect', function(){
        console.log('user disconnected');
    });

    socket.on('chat message', function(msg){
        io.emit('chat message', msg);
    });
});

http.listen(3000, function(){
    console.log('listening on *:3000');
});