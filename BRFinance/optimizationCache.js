
//npm install redis

const redis = require('redis');
const client = redis.createClient();

// Function to fetch data from the cache or the original source
async function fetchDataFromCacheOrSource(key) {
  return new Promise((resolve, reject) => {
    client.get(key, (error, result) => {
      if (error) {
        reject(error);
      } else if (result) {
        resolve(JSON.parse(result));
      } else {
        // Fetch data from the original source
        const data = fetchFromOriginalSource();
        
        // Store the data in the cache
        client.set(key, JSON.stringify(data));
        
        // Set an expiration time for the cache entry (e.g., 1 hour)
        client.expire(key, 3600);
        
        resolve(data);
      }
    });
  });
}

// Example usage
async function getData() {
  const cacheKey = 'example-data';
  
  try {
    const data = await fetchDataFromCacheOrSource(cacheKey);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Function to fetch data from the original source
function fetchFromOriginalSource() {
  // Simulate fetching data from the original source (e.g., database, API)
  return { name: 'John', age: 30 };
}
