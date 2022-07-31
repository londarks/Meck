const Routes =  require('./routes/index.js');

class Meck{
    constructor() {
        this.express = require('express')
        this.app = this.express();
        this.port = 3000;
        const cors = require('cors');
        const bodyParser = require('body-parser');
        this.app.use(cors());
        // Configuring body parser middleware
        this.app.use(bodyParser.urlencoded({ extended: false }));
        this.app.use(bodyParser.json());
        this.routes = new Routes(this.app)
        this.routes.main()
    };

    main(){
        this.app.listen(this.port, () => console.log(`Meck listening on port ${this.port}!`));
    };
};

const server = new Meck();
server.main();
