const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
    it('returns a Success Promise when `true` is passed', function(done) {
        const tokenPromise = getPaymentTokenFromAPI(true);

        tokenPromise.then(function(result) {
            expect(result).to.have.all.keys('data');
            expect(result['data']).to.equal('Successful response from the API');
            done();
        });
    });
});
