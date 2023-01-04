<h2><a href="https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/">2482. Difference Between Ones and Zeros in Row and Column</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> <code data-copier-init="true">m x n</code> binary matrix <code data-copier-init="true">grid</code>.</p>

<p>A <strong>0-indexed</strong> <code data-copier-init="true">m x n</code> difference matrix <code data-copier-init="true">diff</code> is created with the following procedure:</p>

<ul>
	<li>Let the number of ones in the <code data-copier-init="true">i<sup>th</sup></code> row be <code data-copier-init="true">onesRow<sub>i</sub></code>.</li>
	<li>Let the number of ones in the <code data-copier-init="true">j<sup>th</sup></code> column be <code data-copier-init="true">onesCol<sub>j</sub></code>.</li>
	<li>Let the number of zeros in the <code data-copier-init="true">i<sup>th</sup></code> row be <code data-copier-init="true">zerosRow<sub>i</sub></code>.</li>
	<li>Let the number of zeros in the <code data-copier-init="true">j<sup>th</sup></code> column be <code data-copier-init="true">zerosCol<sub>j</sub></code>.</li>
	<li><code data-copier-init="true">diff[i][j] = onesRow<sub>i</sub> + onesCol<sub>j</sub> - zerosRow<sub>i</sub> - zerosCol<sub>j</sub></code></li>
</ul>

<p>Return <em>the difference matrix </em><code data-copier-init="true">diff</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/11/06/image-20221106171729-5.png" style="width: 400px; height: 208px;">
<pre data-copier-init="true"><strong>Input:</strong> grid = [[0,1,1],[1,0,1],[0,0,1]]
<strong>Output:</strong> [[0,0,4],[0,0,4],[-2,-2,2]]
<strong>Explanation:</strong>
- diff[0][0] = <code data-copier-init="true">onesRow<sub>0</sub> + onesCol<sub>0</sub> - zerosRow<sub>0</sub> - zerosCol<sub>0</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[0][1] = <code data-copier-init="true">onesRow<sub>0</sub> + onesCol<sub>1</sub> - zerosRow<sub>0</sub> - zerosCol<sub>1</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[0][2] = <code data-copier-init="true">onesRow<sub>0</sub> + onesCol<sub>2</sub> - zerosRow<sub>0</sub> - zerosCol<sub>2</sub></code> = 2 + 3 - 1 - 0 = 4 
- diff[1][0] = <code data-copier-init="true">onesRow<sub>1</sub> + onesCol<sub>0</sub> - zerosRow<sub>1</sub> - zerosCol<sub>0</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[1][1] = <code data-copier-init="true">onesRow<sub>1</sub> + onesCol<sub>1</sub> - zerosRow<sub>1</sub> - zerosCol<sub>1</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[1][2] = <code data-copier-init="true">onesRow<sub>1</sub> + onesCol<sub>2</sub> - zerosRow<sub>1</sub> - zerosCol<sub>2</sub></code> = 2 + 3 - 1 - 0 = 4 
- diff[2][0] = <code data-copier-init="true">onesRow<sub>2</sub> + onesCol<sub>0</sub> - zerosRow<sub>2</sub> - zerosCol<sub>0</sub></code> = 1 + 1 - 2 - 2 = -2
- diff[2][1] = <code data-copier-init="true">onesRow<sub>2</sub> + onesCol<sub>1</sub> - zerosRow<sub>2</sub> - zerosCol<sub>1</sub></code> = 1 + 1 - 2 - 2 = -2
- diff[2][2] = <code data-copier-init="true">onesRow<sub>2</sub> + onesCol<sub>2</sub> - zerosRow<sub>2</sub> - zerosCol<sub>2</sub></code> = 1 + 3 - 2 - 0 = 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/11/06/image-20221106171747-6.png" style="width: 358px; height: 150px;">
<pre data-copier-init="true"><strong>Input:</strong> grid = [[1,1,1],[1,1,1]]
<strong>Output:</strong> [[5,5,5],[5,5,5]]
<strong>Explanation:</strong>
- diff[0][0] = onesRow<sub>0</sub> + onesCol<sub>0</sub> - zerosRow<sub>0</sub> - zerosCol<sub>0</sub> = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow<sub>0</sub> + onesCol<sub>1</sub> - zerosRow<sub>0</sub> - zerosCol<sub>1</sub> = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow<sub>0</sub> + onesCol<sub>2</sub> - zerosRow<sub>0</sub> - zerosCol<sub>2</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow<sub>1</sub> + onesCol<sub>0</sub> - zerosRow<sub>1</sub> - zerosCol<sub>0</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow<sub>1</sub> + onesCol<sub>1</sub> - zerosRow<sub>1</sub> - zerosCol<sub>1</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow<sub>1</sub> + onesCol<sub>2</sub> - zerosRow<sub>1</sub> - zerosCol<sub>2</sub> = 3 + 2 - 0 - 0 = 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">m == grid.length</code></li>
	<li><code data-copier-init="true">n == grid[i].length</code></li>
	<li><code data-copier-init="true">1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code data-copier-init="true">1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code data-copier-init="true">grid[i][j]</code> is either <code data-copier-init="true">0</code> or <code data-copier-init="true">1</code>.</li>
</ul>
</div>