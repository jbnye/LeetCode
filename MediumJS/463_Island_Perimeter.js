var islandPerimeter = function (grid) {
  let rows = grid.length;
  let cols = grid[0].length;
  let visited = Array.from({ length: rows }, () => Array(cols).fill(false));

  const dfs = (i, j) => {
    if (i < 0 || i >= rows || j < 0 || j >= cols) return 1;
    if (grid[i][j] === 0) return 1;
    if (visited[i][j]) return 0;

    visited[i][j] = true;

    return dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1);
  };

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === 1) {
        return dfs(i, j);
      }
    }
  }
};

var islandPerimeter = function (grid) {
  let ans = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == "1") {
        ans += 4;
        if (i > 0 && grid[i - 1][j] == "1") ans -= 2;
        if (j > 0 && grid[i][j - 1] == "1") ans -= 2;
      }
    }
  }
  return ans;
};
