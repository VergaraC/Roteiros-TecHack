nikto -h  http://192.168.68.113/wordpress
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          192.168.68.113
+ Target Hostname:    192.168.68.113
+ Target Port:        80
+ Start Time:         2022-05-30 00:09:17 (GMT-3)
---------------------------------------------------------------------------
+ Server: Apache/2.2.8 (Ubuntu) DAV/2
+ Retrieved x-powered-by header: PHP/5.2.4-2ubuntu5.10
+ RFC-1918 IP address found in the 'link' header. The IP is "192.168.50.95".
+ The anti-clickjacking X-Frame-Options header is not present.
+ Uncommon header 'link' found, with contents: <http://192.168.50.95/wordpress/index.php/wp-json/>; rel="https://api.w.org/"
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.2.8 appears to be outdated (current is at least Apache/2.2.22). Apache 1.3.42 (final release) and 2.0.64 are also current.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS, TRACE 
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-12184: /wordpress/index.php?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ Server leaks inodes via ETags, header found with file /wordpress/readme, inode: 0x1e0fa, size: 0x1dd4, mtime: 0x5599a725bae80;5e001d635ea40
+ Uncommon header 'tcn' found, with contents: choice
+ OSVDB-3092: /wordpress/readme: This might be interesting...
+ /wordpress/wp-content/plugins/akismet/readme.txt: The WordPress Akismet plugin 'Tested up to' version usually matches the WordPress version
+ OSVDB-62684: /wordpress/wp-content/plugins/hello.php: The WordPress hello.php plugin reveals a file system path
+ OSVDB-3092: /wordpress/license.txt: License file found may identify site software.
+ Uncommon header 'x-frame-options' found, with contents: SAMEORIGIN
+ Cookie wordpress_test_cookie created without the httponly flag
+ /wordpress/wp-login/: Admin login page/section found.
+ OSVDB-: /wordpress/?-s: PHP allows retrieval of the source code via the -s parameter, and may allow command execution. See http://www.kb.cert.org/vuls/id/520827
+ 6544 items checked: 0 error(s) and 19 item(s) reported on remote host
+ End Time:           2022-05-30 00:10:31 (GMT-3) (74 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
tyr@tyrs:~$ 

