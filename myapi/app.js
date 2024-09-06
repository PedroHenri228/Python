const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.get('/fetch-python-api', async (req, res) => {
    try {
        const response = await axios.get('http://127.0.0.1:5000/api');
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).send('Error fetching data from Python API');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
