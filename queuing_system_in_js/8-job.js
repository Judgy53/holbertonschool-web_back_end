/**
 * Create jobs in the queue
 * @param {Object[]} jobs - array of job data
 * @param {Kue} queue - queue to create jobs in
 */
function createPushNotificationsJobs(jobs, queue) {
    if (!(jobs instanceof Array))
        throw new Error('Jobs is not an array');

    jobs.forEach(job => {
        const queueJob = queue.create('push_notification_code_3', job);

        queueJob.save(function (err) {
            if (!err)
                console.log(`Notification job created: ${queueJob.id}`);
        });

        queueJob.on('complete', function () {
            console.log(`Notification job ${queueJob.id} completed`);
        });

        queueJob.on('failed', function (err) {
            console.log(`Notification job ${queueJob.id} failed: ${err}`);
        });

        queueJob.on('progress', function (progress) {
            console.log(`Notification job #${queueJob.id} ${progress}% complete`);
        });
    });
}
module.exports = createPushNotificationsJobs;
