var jwt = require('jsonwebtoken');
var token = jwt.sign({ foo: 'bar' }, 'shhhhh', { algorithm: 'HS256'});
console.log(token)

// class Jwt {
//     constructor(app){
//         this.app = app;
//     }
//   module.exports = Jwt // 👈 Export class