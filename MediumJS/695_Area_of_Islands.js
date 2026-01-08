/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  const directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];
  let ans = 0;
  const bfs = (i, j) => {
    let queue = [[i, j]];
    let temp = 1;
    grid[i][j] = "0";
    while (queue.length) {
      const [x, y] = queue.shift();

      for (const [dx, dy] of directions) {
        let newx = dx + x;
        let newy = dy + y;
        if (
          newx >= 0 &&
          newx < grid.length &&
          newy >= 0 &&
          newy < grid[0].length &&
          grid[newx][newy] == "1"
        ) {
          temp++;
          queue.push([newx, newy]);
          grid[newx][newy] = "0";
        }
      }
    }
    return temp;
  };

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == "1") {
        temp = 0;
        ans = Math.max(ans, bfs(i, j));
      }
    }
  }
  return ans;
};

var maxAreaOfIsland = function (grid) {
  let ans = 0;
  const dfs = (i, j) => {
    if (i >= 0 && i < grid.length && j >= 0 && j < grid[0].length) {
      if (grid[i][j] == "1") {
        grid[i][j] = "0";
        return (
          1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        );
      } else {
        return 0;
      }
    } else {
      return 0;
    }
  };

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == "1") {
        ans = Math.max(ans, dfs(i, j));
      }
    }
  }
  return ans;
};
