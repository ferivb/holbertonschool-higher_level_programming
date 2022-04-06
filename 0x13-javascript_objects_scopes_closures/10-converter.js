#!/usr/bin/node
exports.converter = function (base) {
  return (radix) => radix.toString(base);
};
