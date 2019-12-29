
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
//                                                                                                                                       //
// test-frog.hpp                                                                                                                         //
//                                                                                                                                       //
// D. C. Groothuizen Dijkema - December, 2019                                                                                            //
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

// Test file for LeapingFrog


#include <iostream>
#include <limits>

#include <frog.hpp>

namespace BoardTesting
{
BOOST_AUTO_TEST_SUITE(test_frog)

  // test the leap() function
  BOOST_AUTO_TEST_CASE(test_leap)
  {
    // check if no pads are left, the value is the input jumps_made
    int jumps_made=std::uniform_int_distribution<int>(0,std::numeric_limits<int>::max())(std::mt19937_64{std::random_device{}()});
    BOOST_CHECK(leap(0,jumps_made)==jumps_made);

    jumps_made=std::uniform_int_distribution<int>(0,std::numeric_limits<int>::max())(std::mt19937_64{std::random_device{}()});
    // check if there's one pad left, jumps_made gets incremented by one
    BOOST_CHECK(leap(1,jumps_made)==jumps_made+1);
    BOOST_CHECK(leap(1,0)==1);

    // check jumps_made is always between one and the number of pads
    for (int itr=1;itr<1001;++itr)
    {
      BOOST_CHECK(leap(itr,0)>=1&&leap(itr,0)<=itr);
    }
  }
  
BOOST_AUTO_TEST_SUITE_END()
} // namespace BoardTesting
