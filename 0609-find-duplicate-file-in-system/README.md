<h2><a href="https://leetcode.com/problems/find-duplicate-file-in-system/">609. Find Duplicate File in System</a></h2><h3>Medium</h3><hr><div><p>Given a list <code data-copier-init="true">paths</code> of directory info, including the directory path, and all the files with contents in this directory, return <em>all the duplicate files in the file system in terms of their paths</em>. You may return the answer in <strong>any order</strong>.</p>

<p>A group of duplicate files consists of at least two files that have the same content.</p>

<p>A single directory info string in the input list has the following format:</p>

<ul>
	<li><code data-copier-init="true">"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"</code></li>
</ul>

<p>It means there are <code data-copier-init="true">n</code> files <code data-copier-init="true">(f1.txt, f2.txt ... fn.txt)</code> with content <code data-copier-init="true">(f1_content, f2_content ... fn_content)</code> respectively in the directory "<code data-copier-init="true">root/d1/d2/.../dm"</code>. Note that <code data-copier-init="true">n &gt;= 1</code> and <code data-copier-init="true">m &gt;= 0</code>. If <code data-copier-init="true">m = 0</code>, it means the directory is just the root directory.</p>

<p>The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:</p>

<ul>
	<li><code data-copier-init="true">"directory_path/file_name.txt"</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre data-copier-init="true"><strong>Input:</strong> paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
<strong>Output:</strong> [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre data-copier-init="true"><strong>Input:</strong> paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
<strong>Output:</strong> [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= paths.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code data-copier-init="true">1 &lt;= paths[i].length &lt;= 3000</code></li>
	<li><code data-copier-init="true">1 &lt;= sum(paths[i].length) &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code data-copier-init="true">paths[i]</code> consist of English letters, digits, <code data-copier-init="true">'/'</code>, <code data-copier-init="true">'.'</code>, <code data-copier-init="true">'('</code>, <code data-copier-init="true">')'</code>, and <code data-copier-init="true">' '</code>.</li>
	<li>You may assume no files or directories share the same name in the same directory.</li>
	<li>You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Imagine you are given a real file system, how will you search files? DFS or BFS?</li>
	<li>If the file content is very large (GB level), how will you modify your solution?</li>
	<li>If you can only read the file by 1kb each time, how will you modify your solution?</li>
	<li>What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?</li>
	<li>How to make sure the duplicated files you find are not false positive?</li>
</ul>
</div>