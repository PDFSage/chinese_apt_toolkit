const axios = require('axios');
const cheerio = require('cheerio');

const url = 'http://example.com';

axios.get(url)
    .then(response => {
        const $ = cheerio.load(response.data);
        $('a').each((i, link) => {
            console.log($(link).attr('href'));
        });
    })
    .catch(error => {
        console.log(error);
    });
