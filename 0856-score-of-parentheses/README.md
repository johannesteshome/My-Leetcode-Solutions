<h2><a href="https://leetcode.com/problems/score-of-parentheses/">856. Score of Parentheses</a></h2><h3>Medium</h3><hr><div><p>Given a balanced parentheses string <code data-copier-init="true">s</code>, return <em>the <strong>score</strong> of the string</em>.</p>

<p>The <strong>score</strong> of a balanced parentheses string is based on the following rule:</p>

<ul>
	<li><code data-copier-init="true">"()"</code> has score <code data-copier-init="true">1</code>.</li>
	<li><code data-copier-init="true">AB</code> has score <code data-copier-init="true">A + B</code>, where <code data-copier-init="true">A</code> and <code data-copier-init="true">B</code> are balanced parentheses strings.</li>
	<li><code data-copier-init="true">(A)</code> has score <code data-copier-init="true">2 * A</code>, where <code data-copier-init="true">A</code> is a balanced parentheses string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "()"
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "(())"
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> s = "()()"
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">2 &lt;= s.length &lt;= 50</code></li>
	<li><code data-copier-init="true">s</code> consists of only <code data-copier-init="true">'('</code> and <code data-copier-init="true">')'</code>.</li>
	<li><code data-copier-init="true">s</code> is a balanced parentheses string.</li>
</ul>
</div>