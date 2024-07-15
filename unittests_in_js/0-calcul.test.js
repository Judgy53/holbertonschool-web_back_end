const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
    it('should return 4, no rounding', function() {
        assert.equal(calculateNumber(1, 3), 4);
    });

    it('should return 4, a and b rounding down', function() {
        assert.equal(calculateNumber(1.3, 3.4), 4);
    });

    it('should return 5, a rounding down and b rounding up', function() {
        assert.equal(calculateNumber(1.3, 3.7), 5);
    });

    it('should return 5, both rounding up', function() {
        assert.equal(calculateNumber(0.9, 3.7), 5);
    });

    it('should return 6, both rounding up', function() {
        assert.equal(calculateNumber(1.5, 3.7), 6);
    });
});
