const { Client } = require('pg')

const client = new Client({
  user: process.env.PGUSER,
  host: '127.0.0.1',
  database: process.env.PGDATABASE,
  password: process.env.PGPASSWORD,
  port: 5432,
})

client.connect()


client.query("SELECT * FROM usuarios WHERE email='admin@gmail.com'", (err, res) => {
    if(Object.keys(res['rows']).length){
        console.log(res['rows'])
    }
    else{
        //User not found
        console.log('nao achei nada')
    }
    client.end()
  })
  