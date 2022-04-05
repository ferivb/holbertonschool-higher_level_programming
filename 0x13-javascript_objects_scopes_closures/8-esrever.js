#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  let l = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    tsil[l] = list[i];
    l++;
  }
  return (tsil);
};
