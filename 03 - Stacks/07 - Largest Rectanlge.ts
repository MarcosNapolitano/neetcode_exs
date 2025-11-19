function largestRectangleArea(heights: number[]): number {

  const stack: number[] = [0];
  let maxRect: number = heights[0];
  heights.push(0)

  for (let i = 1; i < heights.length; i++) {

    if (heights[i] <= heights[stack[stack.length - 1]])

      while (stack.length && heights[i] < heights[stack[stack.length - 1]]) {

        const element: number = stack.pop()!;
        let currRect: number = 0;

        stack.length === 0 ? currRect = heights[element] * i : currRect = heights[element] * (i - stack[stack.length - 1] - 1);

        maxRect = Math.max(currRect, maxRect);
      };
    stack.push(i)
  };
  return maxRect;
};
