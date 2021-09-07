/* -*- c++ -*- */

#define TEST_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "test_swig_doc.i"

%{
#include "test/testblock.h"
%}

%include "test/testblock.h"
GR_SWIG_BLOCK_MAGIC2(test, testblock);
