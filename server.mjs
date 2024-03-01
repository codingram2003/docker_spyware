import express from "express";

const app = express();
const port = 3000;

app.post('/', (req, res) => {
  res.send('Trigger sent!');
  console.log(req.body)
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});