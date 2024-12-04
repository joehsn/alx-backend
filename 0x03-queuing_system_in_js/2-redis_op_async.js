import util from 'util';
import redis from 'redis';

const client = redis.createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = (schoolName, value) => client.SET(schoolName, value, redis.print);

const displaySchoolValue = async (schoolName) => console.log(await util.promisify(client.GET).bind(client)(schoolName));

async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
    console.log('Redis client connected to the server');
    await main();
});
