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
        
        test_src = periodic_msg_source(pmt.intern("foo"), 100, 5, True, False)
        
        foo = test.testblock(1234)
        
        self.tb.msg_connect(test_src, "out", msg_debug, msg_debug_port)
        self.tb.msg_connect(foo, "msg", msg_debug, msg_debug_port)  # test terminates if commented out
       
        # set up fg
        print("staring run")    # won't print
        self.tb.run()
        print("finished run()")
        msg_no = msg_debug.num_messages()
        msg1 = pmt.to_python(msg_debug.get_message(1))
        self.assertTrue(msg_no != 0, "received no message..")
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_testblock)
