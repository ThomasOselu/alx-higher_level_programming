#!/usr/bin/node

exports.esrever = function (list) {
  const newAra = [];
  for (let x = list.length - 1; x >= 0; x--) {
    newAra.push(list[x]);
  }
  return (newAra);
};
