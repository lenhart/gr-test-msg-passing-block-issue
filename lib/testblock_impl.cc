/* -*- c++ -*- */
/*
 * Copyright 2021 M.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "testblock_impl.h"
#include <gnuradio/thread/thread.h>

namespace gr {
  namespace test {

    testblock::sptr
    testblock::make(int port)
    {
      return gnuradio::get_initial_sptr
        (new testblock_impl(port));
    }


    /*
     * The private constructor
     */
    testblock_impl::testblock_impl(int port)
      : gr::block("testblock",
              gr::io_signature::make(0, 0, sizeof(0)),
              gr::io_signature::make(0, 0, sizeof(0)))
    {
    	message_port_register_out(pmt::mp(portname));
    }

    /*
     * Our virtual destructor.
     */
    testblock_impl::~testblock_impl()
    {
    	gr::thread::scoped_lock d_mutex;
    	d_finished = true;
    	d_thread.join();
    }

    bool testblock_impl::start()
    {
    	d_thread = gr::thread::thread(boost::bind(&testblock_impl::run, this));
    	return true;
    }


    void testblock_impl::run() {
    	while (!d_finished) {
    		// do sth
    		std::cout << "foo\n";
    	}
    }

  } /* namespace test */
} /* namespace gr */

