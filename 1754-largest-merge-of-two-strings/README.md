<h2><a href="https://leetcode.com/problems/largest-merge-of-two-strings/">1754. Largest Merge Of Two Strings</a></h2><h3>Medium</h3><hr><div><p>You are given two strings <code data-copier-init="true">word1</code> and <code data-copier-init="true">word2</code>. You want to construct a string <code data-copier-init="true">merge</code> in the following way: while either <code data-copier-init="true">word1</code> or <code data-copier-init="true">word2</code> are non-empty, choose <strong>one</strong> of the following options:</p>

<ul>
	<li>If <code data-copier-init="true">word1</code> is non-empty, append the <strong>first</strong> character in <code data-copier-init="true">word1</code> to <code data-copier-init="true">merge</code> and delete it from <code data-copier-init="true">word1</code>.

	<ul>
		<li>For example, if <code data-copier-init="true">word1 = "abc" </code>and <code data-copier-init="true">merge = "dv"</code>, then after choosing this operation, <code data-copier-init="true">word1 = "bc"</code> and <code data-copier-init="true">merge = "dva"</code>.</li>
	</ul>
	</li>
	<li>If <code data-copier-init="true">word2</code> is non-empty, append the <strong>first</strong> character in <code data-copier-init="true">word2</code> to <code data-copier-init="true">merge</code> and delete it from <code data-copier-init="true">word2</code>.
	<ul>
		<li>For example, if <code data-copier-init="true">word2 = "abc" </code>and <code data-copier-init="true">merge = ""</code>, then after choosing this operation, <code data-copier-init="true">word2 = "bc"</code> and <code data-copier-init="true">merge = "a"</code>.</li>
	</ul>
	</li>
</ul>

<p>Return <em>the lexicographically <strong>largest</strong> </em><code data-copier-init="true">merge</code><em> you can construct</em>.</p>

<p>A string <code data-copier-init="true">a</code> is lexicographically larger than a string <code data-copier-init="true">b</code> (of the same length) if in the first position where <code data-copier-init="true">a</code> and <code data-copier-init="true">b</code> differ, <code data-copier-init="true">a</code> has a character strictly larger than the corresponding character in <code data-copier-init="true">b</code>. For example, <code data-copier-init="true">"abcd"</code> is lexicographically larger than <code data-copier-init="true">"abcc"</code> because the first position they differ is at the fourth character, and <code data-copier-init="true">d</code> is greater than <code data-copier-init="true">c</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> word1 = "cabaa", word2 = "bcaaa"
<strong>Output:</strong> "cbcabaaaaa"
<strong>Explanation:</strong> One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> word1 = "abcabc", word2 = "abdcaba"
<strong>Output:</strong> "abdcabcabcaba"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= word1.length, word2.length &lt;= 3000</code></li>
	<li><code data-copier-init="true">word1</code> and <code data-copier-init="true">word2</code> consist only of lowercase English letters.</li>
</ul>
</div>