import redis from "redis";

const client = redis.createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => console.log('Redis client connected to the server'));

const setNewSchool = (schoolName, value) => client.SET(schoolName, value, redis.print);

const displaySchoolValue = (schoolName) => {
    client.GET(schoolName, (_err, reply) => {
        console.log(reply);

    });

};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
