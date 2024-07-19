import { promisify }  from 'util';
import express from 'express';
import redis from 'redis';

const listProducts = [
    {
        itemId: 1,
        itemName: "Suitcase 250",
        price: 50,
        initialAvailableQuantity: 4
    },
    {
        itemId: 2,
        itemName: "Suitcase 450",
        price: 100,
        initialAvailableQuantity: 10
    },
    {
        itemId: 3,
        itemName: "Suitcase 650",
        price: 350,
        initialAvailableQuantity: 2
    },
    {
        itemId: 4,
        itemName: "Suitcase 1050",
        price: 550,
        initialAvailableQuantity: 5
    },
];

/**
 * Get item data from listProducts based on id
 * @param {int} id - id of the item
 * @returns {(Object|null)}
 */
function getItemById(id) {
    for (const item of listProducts) {
        if (item.itemId === id)
            return { ...item };
    }

    return null;
}

const client = redis.createClient();
const asyncHget = promisify(client.hget).bind(client);
const keyReserved = 'reserved';

/**
 * Set item's reserved stock in redis
 * @param {int} itemId
 * @param {int} stock
 */
function reserveStockById(itemId, stock) {
    client.hset(keyReserved, itemId, stock, redis.print);
}

/**
 * Get reserved stock for item
 * @param {int} itemId
 * @returns {int}
 */
async function getCurrentReservedStockById(itemId) {
    const stock = await asyncHget(keyReserved, itemId);
    if (stock === null)
        return 0;
    return parseInt(stock);
}

const app = express();
app.use(express.json());

const port = 1245;
app.listen(port, () => {
    console.log(`Express server available on localhost port ${port}`);
});

app.get('/list_products', function (_, res) {
    res.json(listProducts);
});

app.get('/list_products/:itemId([0-9]+)', async function (req ,res) {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (item === null) {
        res.json({status: "Product not found"});
        return;
    }

    const reserved = await getCurrentReservedStockById(itemId);
    item.currentQuantity = item.initialAvailableQuantity - reserved;

    res.json(item);
});

app.get('/reserve_product/:itemId([0-9]+)', async function (req, res) {
    const itemId = parseInt(req.params.itemId);
    const item = getItemById(itemId);
    if (item === null) {
        res.json({status: "Product not found"});
        return;
    }

    const reserved = await getCurrentReservedStockById(itemId);
    if (reserved >= item.initialAvailableQuantity) {
        res.json({status: "Not enough stock available", itemId: itemId});
        return;
    }

    reserveStockById(itemId, reserved + 1);
    res.json({status: "Reservation confirmed", itemId: itemId});
});
