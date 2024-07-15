const utils = require('./utils');

/**
 * Calculate total price and send the payment request
 * @param {number} totalAmount
 * @param {number} totalShipping
 */
function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const total = utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${total}`);
}
module.exports = sendPaymentRequestToApi;
