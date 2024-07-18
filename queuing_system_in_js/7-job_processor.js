import { createQueue } from 'kue'

const queue = createQueue();
const blacklistedPhones = [
    "4153518780",
    "4153518781"
]
/**
 * Send a notification to a phone number
 * @param {string} phoneNumber - phone number of the recipient
 * @param {string} message - message to send to the phone number
 * @param {Job} job - job in progress
 * @param {DoneCallback} done - Callback to kue
 */
function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blacklistedPhones.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }

    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', 2, function (job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
