import pprint

from libhoyolab import configs, bbs, auth, set_current_user, get_current_user
import webview

# login by password
# print('is login successful: ',
#       auth.login(auth.getLoginTicketByPassword('YOUR_USERNAME_HERE', 'YOUR_PASSWORD_HERE')['token']))
# login by web (require module 'pywebview')
# auth.logout()
# auth.loginByWeb()  # custom gui page also available, pass the html document to the method
# webview.start(debug=True)
# get current user nickname in miyoushe
print(set_current_user('198597220'))
print(get_current_user())
print(bbs.get_current_user())
print(bbs.User().getNickname())
print(bbs.User().getUid())
print(configs.readAccount(str))
# get title and contents in article 43124340
article = bbs.Article(43124340)
print(article.result['data']['post']['post']['subject'])  # title
print(article.getContent())  # contents
# get the first comment in article 43124340
comment = bbs.Comments(43124340, 2, 1)
print(comment.comments[0])
# some of the actions for article
bbs.Actions.upvotePost(43124340)
bbs.Actions.collectPost(43124340)
# bbs.Actions.releaseReply({'ops': [{'insert': '一个字：穷'}]}, '一个字：穷', 43124340)  # really released
# get the article set from feed
page = bbs.Page('2', 'feed')
print(list(item['title'] for item in page.articles))
# get all the forum in miyoushe
forums = bbs.Forum.getAllForum()
pprint.pprint(forums)
# get the article set in the forum
forum = bbs.Forum('26', '2', '1')
pprint.pprint(forum.articles)
