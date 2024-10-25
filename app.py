from urllib.parse import urlparse, urlunparse, parse_qsl, quote, urlencode
import re
import idna

def normalize_url(url):
    # 解析 URL
    parsed_url = urlparse(url)

    # 协议规范化 & 统一为 HTTPS
    scheme = parsed_url.scheme.lower().replace('http://', 'https://')

    # 域名小写化 & IDN 归一化 & www 子域规范化
    host = parsed_url.hostname.lower()
    host = idna.decode(idna.encode(host))  # IDN 处理
    if host.startswith('www.'):
        host = host[4:]  # 去除 www 子域

    # 移除默认端口
    port = parsed_url.port
    if (scheme == 'https' and port == 443) or (scheme == 'http' and port == 80):
        port = None

    # 去除多余斜杠 & 空目录
    path = re.sub(r'/+', '/', parsed_url.path)
    path = re.sub(r'/(\./)+', '/', path)  # 去除单独的 ./
    segments = []
    for segment in path.split('/'):
        if segment == '..':
            if segments:
                segments.pop()  # 处理 ..
        elif segment and segment != '.':
            segments.append(segment)
    path = '/' + '/'.join(segments)

    # 目录斜杠处理
    if len(path) > 1 and path.endswith('/'):
        path = path.rstrip('/')

    # 排序查询参数 & 去除冗余参数 & 查询参数编码
    query_params = parse_qsl(parsed_url.query, keep_blank_values=False)
    query_params = [(k, v) for k, v in query_params if not k.startswith('utm_') and v != '']  # 去除冗余参数
    query_params.sort(key=lambda x: x[0])  # 按照字典顺序排序
    encoded_query = urlencode(query_params, quote_via=quote)

    # Fragment 去除
    fragment = ''

    # 组装标准化后的 URL
    netloc = host
    if port:
        netloc += f':{port}'
    normalized_url = urlunparse((scheme, netloc, path, parsed_url.params, encoded_query, fragment))
    return normalized_url

# 用户输入
url = "https://uhaka.com:80//123"
normalized_url = normalize_url(url)
print("标准化后的URL：", normalized_url)
