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
