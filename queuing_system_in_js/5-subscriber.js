import { createClient } from 'redis';

const client = createClient();

client.on('connect', function () {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
    console.log('Redis client not connected to the server: ' + err)
});

client.on('message', function (_, message) {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
});

client.subscribe('holberton school channel');
