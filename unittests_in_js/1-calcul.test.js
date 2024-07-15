const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function() {
    describe('type = `SUM`', function() {
        it('should return 4, no rounding', function() {
            assert.equal(calculateNumber('SUM', 1, 3), 4);
        });

        it('should return 4, a and b rounding down', function() {
            assert.equal(calculateNumber('SUM', 1.3, 3.4), 4);
        });

        it('should return 5, a rounding down and b rounding up', function() {
            assert.equal(calculateNumber('SUM', 1.3, 3.7), 5);
        });

        it('should return 5, both rounding up', function() {
            assert.equal(calculateNumber('SUM', 0.9, 3.7), 5);
        });

        it('should return 6, both rounding up', function() {
            assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
        });
    });

    describe('type = `SUBTRACT`', function() {
        it('should return 2, no rounding', function() {
            assert.equal(calculateNumber('SUBTRACT', 3, 1), 2);
        });

        it('should return 2, a and b rounding down', function() {
            assert.equal(calculateNumber('SUBTRACT', 3.4, 1.3), 2);
        });

        it('should return 3, a rounding up and b rounding down', function() {
            assert.equal(calculateNumber('SUBTRACT', 3.7, 1.3), 3);
        });

        it('should return 3, both rounding up', function() {
            assert.equal(calculateNumber('SUBTRACT', 3.7, 0.9), 3);
        });

        it('should return -1, both rounding up', function() {
            assert.equal(calculateNumber('SUBTRACT', 1.5, 2.7), -1);
        });
    });

    describe('type = `DIVIDE`', function() {
        it('should return 2, no rounding', function() {
            assert.equal(calculateNumber('DIVIDE', 10, 5), 2);
        });

        it('should return 1.5, no rounding', function() {
            assert.equal(calculateNumber('DIVIDE', 3, 2), 1.5);
        });

        it('should return 3, a and b rounding down', function() {
            assert.equal(calculateNumber('DIVIDE', 3.4, 1.3), 3);
        });

        it('should return -2, both rounding up', function() {
            assert.equal(calculateNumber('DIVIDE', -4.4444444, 1.5), -2);
        });

        it('should return `Error`', function() {
            assert.equal(calculateNumber('DIVIDE', 49, 0.49), 'Error');
        });
    });

    describe('type = `UNKNOWN`', function() {
        it('should return `Error`', function() {
            assert.equal(calculateNumber('UNKNOWN', 10, 5), 'Error');
        });
    });
});
