class JWT {
    constructor(app){
        this.jwt = require('jsonwebtoken');
        this.key = 'AAAAAAAAAAAAAAA'
    };

    generation_token(){
        const token = jwt.sign({ foo: 'bar' }, this.key, { algorithm: 'HS256'});
        console.log(token)
        return token

    }
  }
  
  module.exports = JWT // 👈 Export class