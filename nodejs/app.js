const express = require('express'),
      bodyParser = require('body-parser'),
      m = require('mathjs'),
      app = express();

m.import(require('mathjs-simple-integral'));

app.set('view engine', 'ejs');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended:true }));
app.use(bodyParser.json());

// Routes
app.get('/', function (req, res) {
    var value = '',
        variable = 'x';
   res.render('base', { value:value, variable:variable, noValue:true, equation:'', first:true });
});

app.post('/', function(req, res) {

    // HESAPLAMA
    var value = req.body['value'],
        variable = req.body['variable'],
        operation = req.body['formsubmit'],
        isOkay = true;

    equation = '';

    if(variable == ''){
        variable = 'x';
    }

    if(value && variable) {
        if (operation == 'Türev al') {
            try {
                equation = m.derivative(value, variable).toTex();
            } catch(err) {
                isOkay = false;
            }
        } else if (operation == 'İntegral al') {
            try {
                equation = m.integral(value, variable).toTex();
            } catch(err) {
                isOkay = false;
            }
        }
        var ip = req.header('x-forwarded-for') || req.connection.remoteAddress;
        console.log('[POST] ' + ip + ' | OPERATION: ' + operation);
        res.render('base', { equation:equation, isOkay:isOkay, operation:operation, variable:variable, value:value, noValue:false, first:false })
    }else{
        res.render('base', { equation:equation, isOkay:isOkay, operation:operation, variable:variable, value:value, noValue:true, first:false })
    }

});

app.get('*', function (req, res) {
    res.send('404');
});

const server = app.listen(80, function () {
    console.log('Sunucu baslatildi. (PORT: ' + server.address().port + ')');
});