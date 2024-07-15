const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function() {
    describe('type = `SUM`', function() {
        it('should return 4, no rounding', function() {
            expect(calculateNumber('SUM', 1, 3)).to.equal(4);
        });

        it('should return 4, a and b rounding down', function() {
            expect(calculateNumber('SUM', 1.3, 3.4)).to.equal(4);
        });

        it('should return 5, a rounding down and b rounding up', function() {
            expect(calculateNumber('SUM', 1.3, 3.7)).to.equal(5);
        });

        it('should return 5, both rounding up', function() {
            expect(calculateNumber('SUM', 0.9, 3.7)).to.equal(5);
        });

        it('should return 6, both rounding up', function() {
            expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
        });
    });

    describe('type = `SUBTRACT`', function() {
        it('should return 2, no rounding', function() {
            expect(calculateNumber('SUBTRACT', 3, 1)).to.equal(2);
        });

        it('should return 2, a and b rounding down', function() {
            expect(calculateNumber('SUBTRACT', 3.4, 1.3)).to.equal(2);
        });

        it('should return 3, a rounding up and b rounding down', function() {
            expect(calculateNumber('SUBTRACT', 3.7, 1.3)).to.equal(3);
        });

        it('should return 3, both rounding up', function() {
            expect(calculateNumber('SUBTRACT', 3.7, 0.9)).to.equal(3);
        });

        it('should return -1, both rounding up', function() {
            expect(calculateNumber('SUBTRACT', 1.5, 2.7)).to.equal(-1);
        });
    });

    describe('type = `DIVIDE`', function() {
        it('should return 2, no rounding', function() {
            expect(calculateNumber('DIVIDE', 10, 5)).to.equal(2);
        });

        it('should return 1.5, no rounding', function() {
            expect(calculateNumber('DIVIDE', 3, 2)).to.equal(1.5);
        });

        it('should return 3, a and b rounding down', function() {
            expect(calculateNumber('DIVIDE', 3.4, 1.3)).to.equal(3);
        });

        it('should return -2, both rounding up', function() {
            expect(calculateNumber('DIVIDE', -4.4444444, 1.5)).to.equal(-2);
        });

        it('should return `Error`', function() {
            expect(calculateNumber('DIVIDE', 49, 0.49)).to.equal('Error');
        });
    });

    describe('type = `UNKNOWN`', function() {
        it('should return `Error`', function() {
            expect(calculateNumber('UNKNOWN', 10, 5)).to.equal('Error');
        });
    });
});
