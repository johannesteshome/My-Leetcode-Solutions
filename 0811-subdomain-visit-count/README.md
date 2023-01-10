<h2><a href="https://leetcode.com/problems/subdomain-visit-count/">811. Subdomain Visit Count</a></h2><h3>Medium</h3><hr><div><p>A website domain <code data-copier-init="true">"discuss.leetcode.com"</code> consists of various subdomains. At the top level, we have <code data-copier-init="true">"com"</code>, at the next level, we have <code data-copier-init="true">"leetcode.com"</code>&nbsp;and at the lowest level, <code data-copier-init="true">"discuss.leetcode.com"</code>. When we visit a domain like <code data-copier-init="true">"discuss.leetcode.com"</code>, we will also visit the parent domains <code data-copier-init="true">"leetcode.com"</code> and <code data-copier-init="true">"com"</code> implicitly.</p>

<p>A <strong>count-paired domain</strong> is a domain that has one of the two formats <code data-copier-init="true">"rep d1.d2.d3"</code> or <code data-copier-init="true">"rep d1.d2"</code> where <code data-copier-init="true">rep</code> is the number of visits to the domain and <code data-copier-init="true">d1.d2.d3</code> is the domain itself.</p>

<ul>
	<li>For example, <code data-copier-init="true">"9001 discuss.leetcode.com"</code> is a <strong>count-paired domain</strong> that indicates that <code data-copier-init="true">discuss.leetcode.com</code> was visited <code data-copier-init="true">9001</code> times.</li>
</ul>

<p>Given an array of <strong>count-paired domains</strong> <code data-copier-init="true">cpdomains</code>, return <em>an array of the <strong>count-paired domains</strong> of each subdomain in the input</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> cpdomains = ["9001 discuss.leetcode.com"]
<strong>Output:</strong> ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
<strong>Explanation:</strong> We only have one website domain: "discuss.leetcode.com".
As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre data-copier-init="true"><strong>Input:</strong> cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
<strong>Output:</strong> ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
<strong>Explanation:</strong> We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code data-copier-init="true">1 &lt;= cpdomain.length &lt;= 100</code></li>
	<li><code data-copier-init="true">1 &lt;= cpdomain[i].length &lt;= 100</code></li>
	<li><code data-copier-init="true">cpdomain[i]</code> follows either the <code data-copier-init="true">"rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>.d3<sub>i</sub>"</code> format or the <code data-copier-init="true">"rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>"</code> format.</li>
	<li><code data-copier-init="true">rep<sub>i</sub></code> is an integer in the range <code data-copier-init="true">[1, 10<sup>4</sup>]</code>.</li>
	<li><code data-copier-init="true">d1<sub>i</sub></code>, <code data-copier-init="true">d2<sub>i</sub></code>, and <code data-copier-init="true">d3<sub>i</sub></code> consist of lowercase English letters.</li>
</ul>
</div>