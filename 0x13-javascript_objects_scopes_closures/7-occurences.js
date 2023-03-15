#!/usr/bin/node
exports.nbOcccurebces = function (list, searchElement) {
  let apps = 0;
  for (const element of list) {
    if (element === searchElement) {
      apps++;
    }
  }
  return apps;
};
