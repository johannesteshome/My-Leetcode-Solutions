<h2><a href="https://leetcode.com/problems/shifting-letters-ii/">2381. Shifting Letters II</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code data-copier-init="true">s</code> of lowercase English letters and a 2D integer array <code data-copier-init="true">shifts</code> where <code data-copier-init="true">shifts[i] = [start<sub>i</sub>, end<sub>i</sub>, direction<sub>i</sub>]</code>. For every <code data-copier-init="true">i</code>, <strong>shift</strong> the characters in <code data-copier-init="true">s</code> from the index <code data-copier-init="true">start<sub>i</sub></code> to the index <code data-copier-init="true">end<sub>i</sub></code> (<strong>inclusive</strong>) forward if <code data-copier-init="true">direction<sub>i</sub> = 1</code>, or shift the characters backward if <code data-copier-init="true">direction<sub>i</sub> = 0</code>.</p>

<p>Shifting a character <strong>forward</strong> means replacing it with the <strong>next</strong> letter in the alphabet (wrapping around so that <code data-copier-init="true">'z'</code> becomes <code data-copier-init="true">'a'</code>). Similarly, shifting a character <strong>backward</strong> means replacing it with the <strong>previous</strong> letter in the alphabet (wrapping around so that <code data-copier-init="true">'a'</code> becomes <code data-copier-init="true">'z'</code>).</p>

<p>Return <em>the final string after all such shifts to </em><code data-copier-init="true">s</code><em> are applied</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
<strong>Output:</strong> "ace"
<strong>Explanation:</strong> Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "dztz", shifts = [[0,0,0],[1,1,1]]
<strong>Output:</strong> "catz"
<strong>Explanation:</strong> Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= s.length, shifts.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code data-copier-init="true">shifts[i].length == 3</code></li>
	<li><code data-copier-init="true">0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt; s.length</code></li>
	<li><code data-copier-init="true">0 &lt;= direction<sub>i</sub> &lt;= 1</code></li>
	<li><code data-copier-init="true">s</code> consists of lowercase English letters.</li>
</ul>
</div>