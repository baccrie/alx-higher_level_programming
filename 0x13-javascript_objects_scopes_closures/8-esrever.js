#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  let size = list.length - 1;
  for (let i = 0; i < list.length; i++, --size) {
    rev[i] = list[size];
  }

  return (rev);
};
