<h2><a href="https://leetcode.com/problems/magic-squares-in-grid/">840. Magic Squares In Grid</a></h2><h3>Medium</h3><hr><div><p>A <code data-copier-init="true">3 x 3</code> magic square is a <code data-copier-init="true">3 x 3</code> grid filled with distinct numbers <strong>from </strong><code data-copier-init="true">1</code><strong> to </strong><code data-copier-init="true">9</code> such that each row, column, and both diagonals all have the same sum.</p>

<p>Given a <code data-copier-init="true">row x col</code>&nbsp;<code data-copier-init="true">grid</code>&nbsp;of integers, how many <code data-copier-init="true">3 x 3</code> "magic square" subgrids are there?&nbsp; (Each subgrid is contiguous).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg" style="width: 322px; height: 242px;">
<pre data-copier-init="true"><strong>Input:</strong> grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
<strong>Output:</strong> 1
<strong>Explanation: </strong>
The following subgrid is a 3 x 3 magic square:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg" style="width: 242px; height: 242px;">
while this one is not:
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg" style="width: 242px; height: 242px;">
In total, there is only one magic square inside the given grid.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> grid = [[8]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">row == grid.length</code></li>
	<li><code data-copier-init="true">col == grid[i].length</code></li>
	<li><code data-copier-init="true">1 &lt;= row, col &lt;= 10</code></li>
	<li><code data-copier-init="true">0 &lt;= grid[i][j] &lt;= 15</code></li>
</ul>
</div>