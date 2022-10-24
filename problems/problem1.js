function solve(arrival_times, threshold) {
  return arrival_times.filter((time) => time <= 0).length >= threshold
    ? 'SIM'
    : 'NÃO';
}
module.exports = {
  solve,
};
