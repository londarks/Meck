const { response } = require('express');
const JWT =  require('../jwt/index.js');
const PostgreSQL =  require('../postgreSQL/index.js');

class Routes {
    constructor(app){
        this.app = app;
        this.jwt = new JWT()
        this.postgresql = new PostgreSQL()
        this.crypto = require("crypto");
        this.DATA_ENCRYPTOGRAPH = {
            algorithm : "aes256",
            key : "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
            type : "hex"
        };
    };

    encrypt(password){
        const cipher = this.crypto.createCipher(this.DATA_ENCRYPTOGRAPH.algorithm, this.DATA_ENCRYPTOGRAPH.key);
        cipher.update(password);
        return cipher.final(this.DATA_ENCRYPTOGRAPH.type);
    };

    main(){
        this.app.post('/api/login', (req, res) => {
            const book = req.body;
            // Output the book to the console for debugging
            //console.log(book);
            if(book['email'] != undefined && book['password'] != undefined){
                const password_hash  = this.encrypt(book['password'])
                this.postgresql.read("SELECT * FROM usuarios WHERE email='"+book['email']+"'").then(response => {
                    if(Object.keys(response['rows']).length){
                        if (response['rows'][0]['password'] == password_hash){
                            let bearer = this.jwt.generation_token(response['rows'][0]['id'])
                            res.json({'message': 'login sucess'
                                      ,'bearer': bearer})
                        }
                        else{
                            res.json({'message': 'password is invalid'})
                        }
                    }
                    else{
                        res.json({'message': 'Error email or password is invalid'});
                    }
                })   // <-- callback de sucesso
                .catch(erro => {
                    console.log(erro)
                    res.json({'message': 'Error email or password is invalid'});
                });  // <-- callback de erro
            }
            else{
                res.json({'message': 'Error email or password is invalid'});
            }
            //res.send('Book is added to the database');
        });

        this.app.post('/api/auth', (req, res) => {
            const book = req.body;
            // Output the book to the console for debugging
            console.log(book);
            res.send('Sucess');
            //res.send('Book is added to the database');
        });

        this.app.post('/api/create', (req, res) => {
            const book = req.body;
            // Output the book to the console for debugging
            console.log(book);
            res.send('Sucess');
            //res.send('Book is added to the database');
        });
    };
  }
  
  module.exports = Routes // 👈 Export class