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
