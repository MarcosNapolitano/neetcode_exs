#!/usr/bin/env -S node --experimental-strip-types

function trap(height: number[]): number {

  let rain = 0;
  let l = 0;
  let r = height.length - 1;
  let maxL = 0;
  let maxR = 0;

  while (l < r) {

    if (height[l] < height[r]) {
      if (height[l] >= maxL)
        maxL = height[l];
      else
        rain += maxL - height[l]
      l++;
    }
    else{

      if(height[r]>= maxR)
        maxR = height[r];
      else
        rain += maxR - height[r]
      r--
    };
  }

  return rain;
};


console.log(trap([5, 4, 1, 2]));
console.log(trap([4, 2, 3]));
console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]));
console.log(trap([4, 2, 0, 3, 2, 5]));
console.log(trap([4, 9, 4, 5, 3, 2]))
