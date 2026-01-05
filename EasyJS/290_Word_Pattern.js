var wordPattern = function (pattern, s) {
  let pToW = new Map();
  let wToP = new Map();
  let words = s.split(" ");

  if (pattern.length !== words.length) return false;

  for (let i = 0; i < pattern.length; i++) {
    let p = pattern[i];
    let w = words[i];

    if (
      (pToW.has(p) && pToW.get(p) !== w) ||
      (wToP.has(w) && wToP.get(w) !== p)
    ) {
      return false;
    }

    pToW.set(p, w);
    wToP.set(w, p);
  }

  return true;
};
