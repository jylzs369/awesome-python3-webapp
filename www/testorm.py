# -*- coding: utf-8 -*-
import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
  await orm.create_pool(loop=loop, user='www-data', password='www-data', database='awesome')
  u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
  r = await u.save()
  await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
