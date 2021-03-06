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

#ifndef INCLUDED_TEST_TESTBLOCK_IMPL_H
#define INCLUDED_TEST_TESTBLOCK_IMPL_H

#include <test/testblock.h>

namespace gr {
  namespace test {

    class testblock_impl : public testblock
    {
     private:
      // Nothing to declare in this block.
    	const std::string portname{"msg"};
		gr::thread::thread d_thread;
		gr::thread::mutex d_mutex;
		bool d_finished{false};
		void run();

     public:
		testblock_impl(int port);
		~testblock_impl();

		bool start() override;

    };

  } // namespace test
} // namespace gr

#endif /* INCLUDED_TEST_TESTBLOCK_IMPL_H */

