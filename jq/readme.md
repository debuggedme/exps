```
$ cat jq/cat.info | jq .
parse error: Invalid numeric literal at line 1, column 4
$ cat jq/cat.info | jq -R fromjson\?
{
  "cat": "info"
}
```