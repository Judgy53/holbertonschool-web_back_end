const Utils = {
    /**
    * Round 2 numbers and perform an operation on them.
    * @param {string} type - Type of operation. Can be `SUM`, `SUBTRACT` or `DIVIDE`
    * @param {number} a - First number
    * @param {number} b - Second Number
    * @returns {(number|string)} Result of operation or `Error`
    */
    calculateNumber: function (type, a, b) {
        a = Math.round(a);
        b = Math.round(b);
        switch (type) {
            case 'SUM':
                return a + b;
            case 'SUBTRACT':
                return a - b;
            case 'DIVIDE':
                if (b === 0)
                    return 'Error';
                return a / b;
            default:
                return 'Error';
        }
    }
}
module.exports = Utils;
