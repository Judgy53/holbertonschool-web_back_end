import { createQueue } from 'kue'

const queue = createQueue();

/**
 * Send a notification to a phone number
 * @param {string} phoneNumber - phone number of the recipient
 * @param {string} message - message to send to the phone number
 */
function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', function (job, done) {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});
