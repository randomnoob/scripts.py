# -*- coding: UTF-8 -*-

"""
publish blog to blog site, cnblog or oschina
"""

import xmlrpc.client

class BlogPublisher:
    """
    base class for blog publish
    """

    def __init__(self, username, password, url):
        """
        initialize the username, password and mateWeblog url
        :param username:
        :param password:
        :param url: mateWeblog url
        """
        self.username = username
        self.password = password
        self.url = url

    def publish(self, title, content):
        """
        publish blog to 
        :param content: blog content to publish (markdown syntax)
        :return: 
        """
        pass


class CnBlogPublisher(BlogPublisher):
    """
    blog publisher to cnblog.com
    """

    def __init__(self):
        super("baiyangcao", "y2211612", "http://rpc.cnblogs.com/metaweblog/baiyangcao")
        self.appKey = "baiyangcao"
        self.server = xmlrpc.client.ServerProxy(self.url)
        info = self.server.blogger.getUsersBlogs(self.appKey, self.username, self.password)
        self.blogid = info[0]["blogid"]

    def publish(self, title, content):
        """
        publish blog to 
        :param content: blog content to publish (markdown syntax)
        :return: 
        """
        post = {
            "title": title,
            "description": content
        }
        self.server.metaWeblog.newPost(self.blogid, self.username, self.password, post, False)



class OsChinaPublisher(BlogPublisher):
    """
    blog publisher to oschina.com
    """

    def __init__(self):
        super.__init__()

    def publish(self, title, content):
        """
        publish blog to 
        :param content: blog content to publish (markdown syntax)
        :return: 
        """
        pass
