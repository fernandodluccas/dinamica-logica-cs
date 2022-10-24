function solve(year) {
  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    return '12.09.' + year;
  } else {
    return '13.09.' + year;
  }
}

module.exports = {
  solve,
};
