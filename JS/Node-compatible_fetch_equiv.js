const https = require('https');

//uses the basic built-in 'https' module for Node.js to re-create
//the 'fetch' function available in browser-based JS

//Takes in a url, and returns a promise with the JSON for the URL, which is
//actually a step farther than the original fetch function, but it can easily
//be modified to accomodate non-JSON responses
//Rejects the promise on any errors!
async function fetch_equivalent(url) {
    return new Promise((resolve, reject) =>
        (https.get(url,(res) => {
            let body = "";

            res.on("data", (chunk) => {
                body += chunk;
            });

            res.on("end", () => {
                try {
                    let json = JSON.parse(body);
                    resolve(json);
                } catch (error) {
                    console.error(error.message);
                    reject(error);
                };
            });

        }).on("error", (error) => {
            console.error(error.message);
            reject(error)
        });
    );
}
