class Routes {
    constructor(app){
        this.app = app;
    }
    main(){
        this.app.post('/api/login', (req, res) => {
            const book = req.body;
            // Output the book to the console for debugging
            console.log(book);
            res.send('Sucess');
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