<h2><a href="https://leetcode.com/problems/simplify-path/">71. Simplify Path</a></h2><h3>Medium</h3><hr><div><p>Given a string <code data-copier-init="true">path</code>, which is an <strong>absolute path</strong> (starting with a slash <code data-copier-init="true">'/'</code>) to a file or directory in a Unix-style file system, convert it to the simplified <strong>canonical path</strong>.</p>

<p>In a Unix-style file system, a period <code data-copier-init="true">'.'</code> refers to the current directory, a double period <code data-copier-init="true">'..'</code> refers to the directory up a level, and any multiple consecutive slashes (i.e. <code data-copier-init="true">'//'</code>) are treated as a single slash <code data-copier-init="true">'/'</code>. For this problem, any other format of periods such as <code data-copier-init="true">'...'</code> are treated as file/directory names.</p>

<p>The <strong>canonical path</strong> should have the following format:</p>

<ul>
	<li>The path starts with a single slash <code data-copier-init="true">'/'</code>.</li>
	<li>Any two directories are separated by a single slash <code data-copier-init="true">'/'</code>.</li>
	<li>The path does not end with a trailing <code data-copier-init="true">'/'</code>.</li>
	<li>The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period <code data-copier-init="true">'.'</code> or double period <code data-copier-init="true">'..'</code>)</li>
</ul>

<p>Return <em>the simplified <strong>canonical path</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> path = "/home/"
<strong>Output:</strong> "/home"
<strong>Explanation:</strong> Note that there is no trailing slash after the last directory name.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> path = "/../"
<strong>Output:</strong> "/"
<strong>Explanation:</strong> Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> path = "/home//foo/"
<strong>Output:</strong> "/home/foo"
<strong>Explanation:</strong> In the canonical path, multiple consecutive slashes are replaced by a single one.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= path.length &lt;= 3000</code></li>
	<li><code data-copier-init="true">path</code> consists of English letters, digits, period <code data-copier-init="true">'.'</code>, slash <code data-copier-init="true">'/'</code> or <code data-copier-init="true">'_'</code>.</li>
	<li><code data-copier-init="true">path</code> is a valid absolute Unix path.</li>
</ul>
</div>