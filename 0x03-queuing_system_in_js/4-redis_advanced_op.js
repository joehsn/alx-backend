import redis from 'redis';

const client = redis.createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

const updateHash = (hashName, fieldName, fieldValue) => client.HSET(hashName, fieldName, fieldValue, redis.print);

const printHash = (hashName) => client.HGETALL(hashName, (_err, reply) => console.log(reply));

function main() {
    const hashObj = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };
    for (const [field, value] of Object.entries(hashObj)) {
        updateHash('HolbertonSchools', field, value);
    }
    printHash('HolbertonSchools');
}

client.on('connect', () => {
    console.log('Redis client connected to the server');
    main();
});
