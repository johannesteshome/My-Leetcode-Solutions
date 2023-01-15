<h2><a href="https://leetcode.com/problems/search-a-2d-matrix/">74. Search a 2D Matrix</a></h2><h3>Medium</h3><hr><div><p>You are given an <code data-copier-init="true">m x n</code> integer matrix <code data-copier-init="true">matrix</code> with the following two properties:</p>

<ul>
	<li>Each row is sorted in non-decreasing order.</li>
	<li>The first integer of each row is greater than the last integer of the previous row.</li>
</ul>

<p>Given an integer <code data-copier-init="true">target</code>, return <code data-copier-init="true">true</code> <em>if</em> <code data-copier-init="true">target</code> <em>is in</em> <code data-copier-init="true">matrix</code> <em>or</em> <code data-copier-init="true">false</code> <em>otherwise</em>.</p>

<p>You must write a solution in <code data-copier-init="true">O(log(m * n))</code> time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;">
<pre data-copier-init="true"><strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg" style="width: 322px; height: 242px;">
<pre data-copier-init="true"><strong>Input:</strong> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">m == matrix.length</code></li>
	<li><code data-copier-init="true">n == matrix[i].length</code></li>
	<li><code data-copier-init="true">1 &lt;= m, n &lt;= 100</code></li>
	<li><code data-copier-init="true">-10<sup>4</sup> &lt;= matrix[i][j], target &lt;= 10<sup>4</sup></code></li>
</ul>
</div>