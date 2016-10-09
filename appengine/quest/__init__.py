# -*- coding: utf-8 -*-
import webapp2

from manage import post
from manage import get

app = webapp2.WSGIApplication([
    ('/quest/post',post.Handler),
    ('/quest/get',get.Handler)
], debug=True)
