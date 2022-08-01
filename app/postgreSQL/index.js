
class PostgreSQL {
  constructor(){
      const { Client } = require('pg')
      this.client = new Client({
        user: process.env.PGUSER,
        host: '127.0.0.1',
        database: process.env.PGDATABASE,
        password: process.env.PGPASSWORD,
        port: 5432,
      });
      this.client.connect();
  }

  create(query){
    //
  }

  delet(query){
    //
  }

  update(query){
    //
  }

  read(query){
    return this.client.query(query)
  };

}

module.exports = PostgreSQL // 👈 Export class
  