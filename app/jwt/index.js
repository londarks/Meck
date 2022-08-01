class JWT {
    constructor(){
        this.jwt = require('jsonwebtoken');
        this.key = 'AAAAAAAAAAAAAAA'
    };

    generation_token(id_session){
        try{
            const token = this.jwt.sign({ 'id': id_session }, this.key, {algorithm: 'HS256',
                                                                         expiresIn: '30d'});
            //console.log(token)
            return token
        }
        catch (e){
            console.log('ERROR', e)
            return 'ERROR 502'
        }
    }
    auth_token(token){
    }
  }
  
  module.exports = JWT // 👈 Export class