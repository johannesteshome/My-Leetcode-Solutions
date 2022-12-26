<h2><a href="https://leetcode.com/problems/goal-parser-interpretation/">1678. Goal Parser Interpretation</a></h2><h3>Easy</h3><hr><div><p>You own a <strong>Goal Parser</strong> that can interpret a string <code data-copier-init="true">command</code>. The <code data-copier-init="true">command</code> consists of an alphabet of <code data-copier-init="true">"G"</code>, <code data-copier-init="true">"()"</code> and/or <code data-copier-init="true">"(al)"</code> in some order. The Goal Parser will interpret <code data-copier-init="true">"G"</code> as the string <code data-copier-init="true">"G"</code>, <code data-copier-init="true">"()"</code> as the string <code data-copier-init="true">"o"</code>, and <code data-copier-init="true">"(al)"</code> as the string <code data-copier-init="true">"al"</code>. The interpreted strings are then concatenated in the original order.</p>

<p>Given the string <code data-copier-init="true">command</code>, return <em>the <strong>Goal Parser</strong>'s interpretation of </em><code data-copier-init="true">command</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> command = "G()(al)"
<strong>Output:</strong> "Goal"
<strong>Explanation:</strong>&nbsp;The Goal Parser interprets the command as follows:
G -&gt; G
() -&gt; o
(al) -&gt; al
The final concatenated result is "Goal".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> command = "G()()()()(al)"
<strong>Output:</strong> "Gooooal"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> command = "(al)G(al)()()G"
<strong>Output:</strong> "alGalooG"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= command.length &lt;= 100</code></li>
	<li><code data-copier-init="true">command</code> consists of <code data-copier-init="true">"G"</code>, <code data-copier-init="true">"()"</code>, and/or <code data-copier-init="true">"(al)"</code> in some order.</li>
</ul>
</div>