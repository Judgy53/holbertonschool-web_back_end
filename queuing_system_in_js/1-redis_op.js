import { createClient, print } from 'redis';

/**
 * Set the value for the key `schoolName` in Redis
 * @param {string} schoolName
 * @param {string} value
 */
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

/**
 * Get the value for the key `schoolName` in Redis and logs it to console
 * @param {string} schoolName
 */
function displaySchoolValue(schoolName) {
    client.get(schoolName, function (_, reply) {
        console.log(reply);
    });
}

const client = createClient();

client.on('connect', function () {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
    console.log('Redis client not connected to the server: ' + err)
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
