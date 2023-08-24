const express = require('express');
const app = express();
const path = require('path'); // Import the 'path' module

app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

// Set the 'views' directory and specify EJS as the view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

let currentMessage = '';

app.get('/', (req, res) => {
  res.render('index', { currentMessage }); // Render the 'index' template
});

app.post('/', (req, res) => {
  currentMessage = req.body.message;
  res.redirect('/');
});

app.listen(3000, '192.168.10.92', () => {
  console.log('Server is running on port 3000');
});
