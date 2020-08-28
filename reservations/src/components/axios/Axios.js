const axios = require('axios');

export function get(url) 
{
    axios.get(url)
    .then(function (response) {
        // handle success
        console.log(response);
    })
    .catch(function (error) {
        // handle error
        console.log(error);
    })
}