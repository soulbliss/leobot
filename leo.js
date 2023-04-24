const fs = require("fs");
require("dotenv").config();

const quote_list = [];

fs.readFile("quotes", "utf8", (err, data) => {
  if (err) throw err;

  const lines = data.split(/\r?\n/);
  for (const line of lines) {
    if (line.trim() !== "") {
      quote_list.push(line.trim());
    }
  }
  
  const { WebClient } = require("@slack/web-api");

  // Create a new instance of the WebClient with your Slack API token
  const slack_token = process.env.SLACK_API_TOKEN;
  const slackClient = new WebClient(slack_token);

  // Define the channel where you want to post the message
  const channel = process.env.SLACK_CHANNEL_NAME

  // Define the message text
  const pick_quote = quote_list[Math.floor(Math.random() * quote_list.length)];
  const message = pick_quote;

  // Call the chat.postMessage method using the WebClient
  slackClient.chat
    .postMessage({
      channel: channel,
      text: message
    })
    .then(result => {
      console.log(`Message posted to ${channel}: ${message}`);
    })
    .catch(error => {
      console.error(error);
    });
});
