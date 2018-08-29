#! /usr/bin/env python


#要使用实现操作的浏览器
BROWSER = 'Chrome'

#用户帐号及密码, 设置后会自动输入, 但是还是需要自己输入验证码登录
#USERNAME =
#PASSWORD =


#要点赞评论的链接地址
URLS = [
        'https://weibo.com/2656274875/GwPZEjBNX?filter=hot&root_comment_id=0&type=comment#_rnd1535501553693',
        ]

#自动发言内容
CONTENT = '互赞互粉[互粉]互粉[互粉]双倍回赞你有意的内容，不粉也来点个赞叭(回粉可能会迟到, 记得私信给我一下噢)'

#微博群链接地址
CHATGROUPURLS = [
        'https://weibo.com/message/history?gid=4075181117196353&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%894%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=4075182799395477&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%895%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=3972213377637760&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E7%B2%89%E4%BA%92%E8%B5%9E%EF%BC%883%EF%BC%89&type=2',
        'https://weibo.com/message/history?gid=3826460924544075&name=%E6%90%9E%E7%AC%91gif%E5%9C%96%E5%88%86%E4%BA%AB%E4%BA%92%E7%B2%892%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=4074460921980762&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E7%B2%89%E4%BA%92%E8%B5%9E6%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=3920811469209060&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%89%E5%8D%81%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=3971237531374456&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%89%E5%85%AD%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=4141723703622660&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E4%B9%9D%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        'https://weibo.com/message/history?gid=4141723703622660&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E4%B9%9D%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        'https://weibo.com/message/history?gid=4026628202350898&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E7%B2%89%E4%BA%92%E8%B5%9E%EF%BC%886%EF%BC%89&type=2',
        'https://weibo.com/message/history?gid=4141337425500935&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E5%9B%9B%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        'https://weibo.com/message/history?gid=3992580855295584&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E7%B2%89%E4%BA%92%E8%B5%9E%E4%BA%94%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=4141340016829150&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E4%B8%83%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        'https://weibo.com/message/history?gid=4141148950415000&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E4%B8%80%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        'https://weibo.com/message/history?gid=4143365216266460&name=%E5%8D%83%E4%BA%BA%E4%BA%92v%E7%B2%89%E6%96%87%E8%89%BA%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E5%BE%AE%E5%8D%9A%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=3991313609800719&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%89%EF%BC%884%EF%BC%89&type=2',
        'https://weibo.com/message/history?gid=3992581052794731&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E7%B2%89%E4%BA%92%E8%B5%9E%E5%9B%9B%E4%BA%92%E8%AF%84%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=3992576555841309&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%89%E4%B8%83%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=3993473004578689&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E7%B2%89%E4%BA%92%E8%B5%9E%E4%B8%89%E4%BA%92%E5%8A%A9%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=4074466726137718&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%893%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=4141722445447076&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E5%85%AB%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        'https://weibo.com/message/history?gid=3992574949796536&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%89%E4%B9%9D%E4%BA%92%E7%B2%89%E7%BE%A4&type=2',
        'https://weibo.com/message/history?gid=4141338394292231&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E4%BA%94%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        'https://weibo.com/message/history?gid=4043329572473656&name=%E4%BA%92%E7%B2%89%E7%BE%A4%201%E4%BA%92%E8%B5%9E%E7%BE%A4%E4%BA%92%E8%AF%84%E7%BE%A4%E4%BA%92%E8%BD%AC%E7%BE%A41&type=2',
        'https://weibo.com/message/history?gid=3971750730009007&name=%E6%96%B0%E6%B5%AA%E4%BA%92%E8%B5%9E%E4%BA%92%E7%B2%89%EF%BC%882%EF%BC%89&type=2',
        'https://weibo.com/message/history?gid=4141336766756880&name=%E5%8D%83%E4%BA%BA%E4%BA%92%20%E7%B2%89%20%E4%B8%89%E7%BE%A4%20%E4%BA%92%E8%AF%84%E4%BA%92%E8%B5%9E%E4%BA%A4%E5%8F%8B&type=2',
        ]
