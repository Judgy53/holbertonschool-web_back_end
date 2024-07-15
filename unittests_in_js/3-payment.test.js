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
});
