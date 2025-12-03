const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(`
    <h1>Frontend Dev Container</h1>
    <p>Běžím v Node.js prostředí.</p>
    <p>Zkuste zavolat Backend API: <a href="http://localhost:5000">http://localhost:5000</a></p>
  `);
});

server.listen(3000, () => {
  console.log('Frontend server běží na http://localhost:3000');
});