
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

  // test the average() function
  BOOST_AUTO_TEST_CASE(test_average)
  {
    // check no runs gives an average of 0.
    BOOST_CHECK(average(1,0)==0.);
    // check the average of one leap needed is always 1
    BOOST_CHECK(average(1,10)==1.);

    // check the average of n leaps possible is close to the nth harmonic number for the first 10 n
    double sum=1.;
    for (int itr=2;itr<11;++itr)
    {
      sum+=1./itr;
      BOOST_CHECK_CLOSE_FRACTION(average(itr,10000),sum,0.05);
    }
  }

  // test the simulate() function
  BOOST_AUTO_TEST_CASE(test_simulate)
  {
    int n_itr=10;
    double *mean=new double[n_itr];
    // check the average of one leap needed is always 1
    simulate(1,n_itr,mean);
    for (int itr=0;itr<n_itr;++itr)
    {
      BOOST_CHECK(*(mean+itr)==1);
    }
    delete mean;

    // check the average of n leaps possible is close to the nth harmonic number for the first 10 n
    double sum=1.;
    n_itr=10000;
    for (int itr=2;itr<11;++itr)
    {
      mean=new double[n_itr];
      sum+=1./itr; // calculate the itrth harmonic number
      simulate(itr,n_itr,mean);
      // the average is the last element of mean
      BOOST_CHECK_CLOSE_FRACTION(*(mean+n_itr-1),sum,0.05);
      delete mean;
    }
  }

BOOST_AUTO_TEST_SUITE_END()
} // namespace BoardTesting
