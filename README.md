协议规范化（Scheme Normalization）
● 描述：将所有协议（如 http 和 https）统一为小写。
● 示例：
  ○ HTTP://Example.com → http://example.com
2. 域名小写化（Host Normalization）
● 描述：将URL中的域名部分统一转换为小写，因为域名不区分大小写。
● 示例：
  ○ http://Example.com/Page1 → http://example.com/Page1
3. 默认端口去除（Remove Default Ports）
● 描述：去掉URL中的默认端口号，如HTTP的默认端口80，HTTPS的默认端口443。
● 示例：
  ○ http://example.com:80/page → http://example.com/page
  ○ https://example.com:443/page → https://example.com/page
4. 目录斜杠处理（Trailing Slash Handling）
● 描述：统一URL结尾是否带有斜杠。可以选择保留或去掉，但需要保持一致。
● 示例：
  ○ http://example.com/page/ → http://example.com/page
  ○ 或者：http://example.com/page → http://example.com/page/
5. Fragment 去除（Remove Fragments）
● 描述：去掉URL中 # 后面的部分，因为它是客户端片段标识符，不影响资源的获取。
● 示例：
  ○ http://example.com/page#section1 → http://example.com/page
6. 排序查询参数（Sort Query Parameters）
● 描述：将查询参数按照字典序进行排序，以保证相同的查询参数顺序一致。
● 示例：
  ○ http://example.com/page?b=2&a=1 → http://example.com/page?a=1&b=2
7. 去除冗余查询参数（Remove Redundant Query Parameters）
● 描述：去除对资源无意义或重复的查询参数，如空值参数或跟踪参数（例如 utm_*）。
● 示例：
  ○ http://example.com/page?a=1&b=&utm_source=google → http://example.com/page?a=1
8. 字符编码规范化（Character Encoding Normalization）
● 描述：将所有非ASCII字符进行URL编码，或将已编码的字符解码为对应字符（保留保留字符）。
● 示例：
  ○ http://example.com/%7Euser → http://example.com/~user
9. 协议统一为 HTTPS（HTTPS Enforce）
● 描述：将所有 http 协议转换为 https，用于提高安全性。
● 示例：
  ○ http://example.com/page → https://example.com/page
10. 处理特殊路径符号（Dot-Segment Normalization）
● 描述：将路径中的 . 或 .. 进行规范化，以简化路径。
● 示例：
  ○ http://example.com/a/b/../c/./d → http://example.com/a/c/d
11. 去除多余的斜杠（Remove Multiple Slashes）
● 描述：将路径中多余的连续斜杠合并为一个。
● 示例：
  ○ http://example.com//a///b → http://example.com/a/b
12. 标准化 www 子域（Normalize www Subdomain）
● 描述：将带 www 和不带 www 的 URL 统一成一种形式。
● 示例：
  ○ http://www.example.com/page → http://example.com/page
  ○ 或者反之。
13. 移除空目录（Remove Empty Directory Paths）
● 描述：移除路径中没有实际意义的空目录。
● 示例：
  ○ http://example.com/a//b → http://example.com/a/b
14. 统一查询参数编码（Query Parameter Encoding）
● 描述：将查询参数值中的特殊字符进行统一的编码处理。
● 示例：
  ○ http://example.com/page?a=b+c → http://example.com/page?a=b%20c
15. IDN（国际化域名）归一化
● 描述：将国际化域名（IDN）转换为其原始的 Punycode 格式，或者将 Punycode 转换为用户可读的域名。
● 示例：
  ○ http://xn--fsq.com → http://例子.com