const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
    let logSpy;

    beforeEach(function() {
        logSpy = sinon.spy(console, 'log');
    });

    afterEach(function() {
        logSpy.restore();
    });

    it('logs the correct output with args: 100, 20', function() {
        sendPaymentRequestToApi(100, 20);
        expect(logSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    });

    it('logs the correct output with args: 10, 10', function() {
        sendPaymentRequestToApi(10, 10);
        expect(logSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    });
});
