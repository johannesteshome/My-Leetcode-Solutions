<h2><a href="https://leetcode.com/problems/merge-sorted-array/">88. Merge Sorted Array</a></h2><h3>Easy</h3><hr><div><p>You are given two integer arrays <code data-copier-init="true">nums1</code> and <code data-copier-init="true">nums2</code>, sorted in <strong>non-decreasing order</strong>, and two integers <code data-copier-init="true">m</code> and <code data-copier-init="true">n</code>, representing the number of elements in <code data-copier-init="true">nums1</code> and <code data-copier-init="true">nums2</code> respectively.</p>

<p><strong>Merge</strong> <code data-copier-init="true">nums1</code> and <code data-copier-init="true">nums2</code> into a single array sorted in <strong>non-decreasing order</strong>.</p>

<p>The final sorted array should not be returned by the function, but instead be <em>stored inside the array </em><code data-copier-init="true">nums1</code>. To accommodate this, <code data-copier-init="true">nums1</code> has a length of <code data-copier-init="true">m + n</code>, where the first <code data-copier-init="true">m</code> elements denote the elements that should be merged, and the last <code data-copier-init="true">n</code> elements are set to <code data-copier-init="true">0</code> and should be ignored. <code data-copier-init="true">nums2</code> has a length of <code data-copier-init="true">n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>Output:</strong> [1,2,2,3,5,6]
<strong>Explanation:</strong> The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6] with the underlined elements coming from nums1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> nums1 = [1], m = 1, nums2 = [], n = 0
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [1] and [].
The result of the merge is [1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> nums1 = [0], m = 0, nums2 = [1], n = 1
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">nums1.length == m + n</code></li>
	<li><code data-copier-init="true">nums2.length == n</code></li>
	<li><code data-copier-init="true">0 &lt;= m, n &lt;= 200</code></li>
	<li><code data-copier-init="true">1 &lt;= m + n &lt;= 200</code></li>
	<li><code data-copier-init="true">-10<sup>9</sup> &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up: </strong>Can you come up with an algorithm that runs in <code data-copier-init="true">O(m + n)</code> time?</p>
</div>