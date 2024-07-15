const expect = require('chai').expect;
const sinon = require('sinon');
const utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
    it('uses calculateNumber with the correct arguments', function() {
        const calcSpy = sinon.spy(utils, "calculateNumber");
        sendPaymentRequestToApi(100, 20);

        expect(calcSpy.calledOnceWithExactly('SUM', 100,  20)).to.be.true;

        calcSpy.restore();
    });

    it('uses calculateNumber and logs the correct output', function() {
        const calcStub = sinon.stub(utils, "calculateNumber");
        calcStub.returns(10);
        const logSpy = sinon.spy(console, "log");

        sendPaymentRequestToApi(100, 20);

        expect(calcStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(logSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

        calcStub.restore();
        logSpy.restore();
    });
});
