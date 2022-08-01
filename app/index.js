const Routes =  require('./routes/index.js');

class Meck{
    constructor() {
        this.port = 3000;
        this.express = require('express')
        const cors = require('cors');
        const bodyParser = require('body-parser');
        this.app = this.express();
        // this.jwt = new JWT()
        // this.postgresql = new PostgreSQL()
        //create routes and others files
        this.routes = new Routes(this.app)
        this.app.use(cors());
        // Configuring body parser middleware
        this.app.use(bodyParser.urlencoded({ extended: false }));
        this.app.use(bodyParser.json());
        this.routes.main()
    };

    main(){
        this.app.listen(this.port, () => console.log(`Meck listening on port ${this.port}!`));
    };
};

const server = new Meck();
server.main();
