import { promisify } from 'util'
import { createClient, print } from 'redis';

const client = createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', function () {
    console.log('Redis client connected to the server');
});

client.on('error', function (err) {
    console.log('Redis client not connected to the server: ' + err)
});

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
async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
