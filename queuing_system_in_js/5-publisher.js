import { createClient } from 'redis';

const client = createClient();

client.on('connect', function () {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
    console.log('Redis client not connected to the server: ' + err)
});

/**
 *
 * Publish a message on `holberton school channel`
 * @param {string} message - message to publish
 * @param {int} time - time to wait before publish (in ms)
 */
function publishMessage(message, time) {
    console.log('About to send ' + message);
    setTimeout(() => client.publish('holberton school channel', message), time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
