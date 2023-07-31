# JavaScript - Web Scraping

## Background
> JavaScript  

`Web scraping` is the process of extracting data from websites, allowing us to retrieve and manipulate information programmatically. Throughout this project, we will explore how to manipulate JSON data, use the `request` and `fetch` API for making HTTP requests, and read and write files using the `fs` module.


## Premise
```
- Understand why JavaScript programming is powerful for web scraping.
- Manipulate JSON data efficiently.
- Utilize the `request` and `fetch` API to interact with web pages and retrieve data.
- Read and write files using the `fs` module in Node.js.
```


## `JSON`:

`JSON` (JavaScript Object Notation) is a lightweight data-interchange format used for exchanging data between a server and a web application. ***JSON objects*** consist of *key-value* pairs, where keys are strings and values can be strings, numbers, arrays, objects, or even `null`.

#### Example of a JSON object representing a person:

```json
{
  "name": "Satoru Goju",
  "email": "satoru@jujutsukaisen.anime",
  "address": {
    "city": "I have an address in RAM",
    "zipcode": "1010101"
  },
  "hobbies": ["stuff", "stuff-n", "not-coding"]
}
```

### Running Scripts with NodeJS:
```bash
mu-o@HP:~/web_scraping$ cat cisfun
C is super fun!
mu-o@HP:~/web_scraping$ ./0-readme.js cisfun
C is super fun!

mu-o@HP:~/web_scraping$ ./0-readme.js doesntexist
[Error: ENOENT: no such file or directory, open 'doesntexist'] {
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist'
}
mu-o@HP:~/web_scraping$
```

---
### Scraping Data and Parsing it as JSON

- #### Generic Scraping:
```javascript
const request = require('request');
const url = 'https://example.com/api/data';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);

    console.log(data);
  } else {
    console.error('Error:', error);
  }
});
```

- #### Extracting Information from Nested JSON Objects:

```javascript
const request = require('request');
const url = 'https://example.com/api/data';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {

    // parse the response body as JSON
    const data = JSON.parse(body);

    // access nested JSON properties
    const firstName = data.user.name.first;
    const lastName = data.user.name.last;
    const email = data.user.email;

    console.log(`Name: ${firstName} ${lastName}`);
    console.log(`Email: ${email}`);
  } else {
    console.error('Error:', error);
  }
});
```

- #### Looping Through JSON Arrays:

```javascript
const request = require('request');

const url = 'https://example.com/api/books';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // parse the response body as JSON
    const books = JSON.parse(body);

    // Iterate over the array of books
    books.forEach((book) => {
      console.log(`Title: ${book.title}`);
      console.log(`Author: ${book.author}`);
      console.log(`Year: ${book.year}`);
      console.log('---------------------------');
    });
  } else {
    console.error('Error:', error);
  }
});
```

- #### Writing Scraped Data to a JSON File:

```javascript
const fs = require('fs');
const request = require('request');

const url = 'https://example.com/api/data';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // parse the response body as JSON
    const data = JSON.parse(body);
    
    // write JSON to file:
    fs.writeFile('data.json', JSON.stringify(data, null, 2), (err) => {
      if (err) throw err;
      console.log('Data has been written to data.json');
    });
  } else {
    console.error('Error:', error);
  }
});
