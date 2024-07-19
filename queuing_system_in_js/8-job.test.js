import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', function () {
    before(function () {
        queue.testMode.enter();
    });

    afterEach(function () {
        queue.testMode.clear();
    });

    after(function () {
        queue.testMode.exit();
    });

    it('display a error message if jobs is not an array', function () {
        expect(() => createPushNotificationsJobs(42, queue)).to.throw(Error, 'Jobs is not an array');
        expect(() => createPushNotificationsJobs("nope", queue)).to.throw(Error, 'Jobs is not an array');
        expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
        expect(queue.testMode.jobs.length).to.equal(0);
    });

    it('create two new jobs to the queue', function () {
        const testJobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 2341 to verify your account'
            },
        ];

        expect(() => createPushNotificationsJobs(testJobs, queue)).to.not.throw();
        expect(queue.testMode.jobs.length).to.equal(2);

        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.equal(testJobs[0]);

        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.equal(testJobs[1]);
    });
});
