const request = require("request");
const expect = require('chai').expect;

describe('GET /', function() {
    it('returns the correct status code', function (done) {
        request('http://localhost:7865', function (error, response, _) {
            if (error)
                done(error);
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('returns the correct result', function (done) {
        request('http://localhost:7865', function (error, _, body) {
            if (error)
                done(error);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});

describe('GET /cart/:id', function() {
    it('returns status code 200 when `id` is a number', function (done) {
        request('http://localhost:7865/cart/12', function (error, response, _) {
            if (error)
                done(error);
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('returns correct body output when `id` is a number', function (done) {
        request('http://localhost:7865/cart/12', function (error, _, body) {
            if (error)
                done(error);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('returns status code 404 when `id` is NOT a number', function (done) {
        request('http://localhost:7865/cart/hello', function (error, response, _) {
            if (error)
                done(error);
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});

describe('GET /available_payments', function() {
    it('returns status code 200', function (done) {
        request('http://localhost:7865/available_payments', function (error, response, _) {
            if (error)
                done(error);
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('returns correct body content', function (done) {
        request('http://localhost:7865/available_payments', function (error, _, body) {
            if (error)
                done(error);
            const bodyJson = JSON.parse(body);
            expect(bodyJson).to.deep.equal({payment_methods: {credit_cards: true, paypal: false}});
            done();
        });
    });
});

describe('POST /login', function() {
    const reqOptions = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        headers: {'content-type': 'application/json' },
        body: {userName: 'Betty'},
        json: true
    }

    it('returns status code 200', function (done) {
        request(reqOptions, function (error, response, _) {
            if (error)
                done(error);
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('returns correct body content', function (done) {
        request(reqOptions, function (error, _, body) {
            if (error)
                done(error);
            expect(body).to.equal('Welcome Betty');
            done();
        });
    });
});
