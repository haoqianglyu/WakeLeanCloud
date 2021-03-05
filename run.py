import requests
import sys
import time
import leancloud

class Comment(leancloud.Object):
    pass

if (len(sys.argv) >= 3):
    appid = sys.argv[1]
    appsec = sys.argv[2]

leancloud.init(appid, master_key=appsec)
comment=Comment()
comment.set('comment','waaaaaaakeup')
comment.set('mail','test@test.cn')
comment.save()
print("唤醒完毕")
time.sleep(10)
Comment = leancloud.Object.extend('Comment')
query = Comment.query
query.equal_to('comment','waaaaaaakeup')
reslist=query.find()
for item in reslist:
    item.destroy()
print("唤醒评论清除完毕")
