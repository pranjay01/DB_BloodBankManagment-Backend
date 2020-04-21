#! /usr/bin/env node

require("dotenv").config({ silent: true });
const path = require("path");
const express = require("express");
const publicPath = path.join(__dirname, "build");
const app = express();
const cors = require('cors');



app.use(express.static(publicPath));
app.use(cors());



//Host react application on root url
app.get("/", (req, res) => {
  res.sendFile(path.join(publicPath, "index.html"));
});

const port = process.env.PORT || 80;

app.listen(port, () => {
  console.log("Server running on port: %d", port);
});

