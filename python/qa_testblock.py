#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 M.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from foo.foo_swig import periodic_msg_source
import test_swig as test
import pmt

class qa_testblock(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
        msg_debug = blocks.message_debug()
        msg_debug_port = "store"
        
        test_str = "foo"
        test_src = periodic_msg_source(pmt.intern(test_str), 100, -1, True, False)
        
        foo = test.testblock(1234)
        
        self.tb.msg_connect(test_src, "out", msg_debug, msg_debug_port)
        self.tb.msg_connect(foo, "msg", msg_debug, msg_debug_port)
       
        # set up fg
        self.tb.run()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_testblock)
