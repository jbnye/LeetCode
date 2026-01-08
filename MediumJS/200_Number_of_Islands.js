var numIslands = function (grid) {
  let ans = 0;

  let queue = [];

  const helper = (i, j) => {
    if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length) {
      return;
    }

    if (grid[i][j] == "1") {
      grid[i][j] = "0";

      helper(i - 1, j);

      helper(i + 1, j);

      helper(i, j - 1);

      helper(i, j + 1);
    } else {
      return;
    }
  };

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] == "1") {
        ans++;

        helper(i, j);
      }
    }
  }

  return ans;
};

var numIslands = function (grid) {
  let ans = 0;

  const directions = [
    [1, 0],

    [-1, 0],

    [0, 1],

    [0, -1],
  ];

  const bfs = (i, j) => {
    let queue = [[i, j]];

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
          queue.push([newx, newy]);

          grid[newx][newy] = "0";
        }
      }
    }
  };

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] == "1") {
        bfs(i, j);

        ans++;
      }
    }
  }

  return ans;
};
