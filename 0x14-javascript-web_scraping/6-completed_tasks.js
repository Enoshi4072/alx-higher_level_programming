#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const tasks = JSON.parse(body);

    const completedTasks = tasks.reduce((userTasks, task) => {
      if (task.completed) {
        if (!userTasks[task.userId]) {
          userTasks[task.userId] = 1;
        } else {
          userTasks[task.userId]++;
        }
      }
      return userTasks;
    }, {});

    console.log(completedTasks);
  }
});
