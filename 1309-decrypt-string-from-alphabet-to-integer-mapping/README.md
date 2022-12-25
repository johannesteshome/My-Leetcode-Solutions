<h2><a href="https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/">1309. Decrypt String from Alphabet to Integer Mapping</a></h2><h3>Easy</h3><hr><div><p>You are given a string <code data-copier-init="true">s</code> formed by digits and <code data-copier-init="true">'#'</code>. We want to map <code data-copier-init="true">s</code> to English lowercase characters as follows:</p>

<ul>
	<li>Characters (<code data-copier-init="true">'a'</code> to <code data-copier-init="true">'i'</code>) are represented by (<code data-copier-init="true">'1'</code> to <code data-copier-init="true">'9'</code>) respectively.</li>
	<li>Characters (<code data-copier-init="true">'j'</code> to <code data-copier-init="true">'z'</code>) are represented by (<code data-copier-init="true">'10#'</code> to <code data-copier-init="true">'26#'</code>) respectively.</li>
</ul>

<p>Return <em>the string formed after mapping</em>.</p>

<p>The test cases are generated so that a unique mapping will always exist.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "10#11#12"
<strong>Output:</strong> "jkab"
<strong>Explanation:</strong> "j" -&gt; "10#" , "k" -&gt; "11#" , "a" -&gt; "1" , "b" -&gt; "2".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "1326#"
<strong>Output:</strong> "acz"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= s.length &lt;= 1000</code></li>
	<li><code data-copier-init="true">s</code> consists of digits and the <code data-copier-init="true">'#'</code> letter.</li>
	<li><code data-copier-init="true">s</code> will be a valid string such that mapping is always possible.</li>
</ul>
</div>