<h2><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist/">1346. Check If N and Its Double Exist</a></h2><h3>Easy</h3><hr><div><p>Given an array <code data-copier-init="true">arr</code> of integers, check if there exist two indices <code data-copier-init="true">i</code> and <code data-copier-init="true">j</code> such that :</p>

<ul>
	<li><code data-copier-init="true">i != j</code></li>
	<li><code data-copier-init="true">0 &lt;= i, j &lt; arr.length</code></li>
	<li><code data-copier-init="true">arr[i] == 2 * arr[j]</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> arr = [10,2,5,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> arr = [3,1,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no i and j that satisfy the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">2 &lt;= arr.length &lt;= 500</code></li>
	<li><code data-copier-init="true">-10<sup>3</sup> &lt;= arr[i] &lt;= 10<sup>3</sup></code></li>
</ul>
</div>