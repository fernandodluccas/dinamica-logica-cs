function solve(socks_array) {
  const socks = socks_array.reduce((acc, sock) => {
    acc[sock] = acc[sock] ? acc[sock] + 1 : 1;
    return acc;
  }, {});

  return Object.values(socks).reduce(
    (acc, sock) => acc + Math.floor(sock / 2),
    0
  );
}

module.exports = {
  solve,
};
