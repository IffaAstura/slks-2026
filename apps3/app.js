const express = require('express');
const AWS = require('aws-sdk');
require('dotenv').config();

const app = express();
const s3 = new AWS.S3();
const bucket = process.env.S3_BUCKET_NAME;

app.get('/app3', async (req, res) => {
  try {
    const data = await s3.listObjectsV2({ Bucket: bucket }).promise();
    const items = data.Contents.map(i => i.Key);
    res.send(`<h1>S3 Files</h1><ul>${items.map(i => `<li>${i}</li>`).join('')}</ul>`);
  } catch (err) {
    res.send("Error: " + err);
  }
});

app.listen(5000, () => console.log("Running on port 5000"));
