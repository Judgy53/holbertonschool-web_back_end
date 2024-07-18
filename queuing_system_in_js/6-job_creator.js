import { createQueue } from 'kue'

const queue = createQueue();
const jobData = {
    phoneNumber: "+331535393016",
    message: "Job's message",
};

const job = queue.create('push_notification_code', jobData).save(function (err) {
    if (!err)
        console.log('Notification job created: ' + job.id);
});

job.on('complete', function () {
    console.log('Notification job completed');
});

job.on('failed', function () {
    console.log('Notification job failed');
});
