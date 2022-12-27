<h2><a href="https://leetcode.com/problems/number-of-good-pairs/">1512. Number of Good Pairs</a></h2><h3>Easy</h3><hr><div><p>Given an array of integers <code data-copier-init="true">nums</code>, return <em>the number of <strong>good pairs</strong></em>.</p>

<p>A pair <code data-copier-init="true">(i, j)</code> is called <em>good</em> if <code data-copier-init="true">nums[i] == nums[j]</code> and <code data-copier-init="true">i</code> &lt; <code data-copier-init="true">j</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> nums = [1,2,3,1,1,3]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> nums = [1,1,1,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Each pair in the array are <em>good</em>.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= nums.length &lt;= 100</code></li>
	<li><code data-copier-init="true">1 &lt;= nums[i] &lt;= 100</code></li>
</ul>
</div>