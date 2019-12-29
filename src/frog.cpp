
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
//                                                                                                                                       //
// frog.cpp                                                                                                                              //
//                                                                                                                                       //
// D. C. Groothuizen Dijkema - December, 2019                                                                                            //
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

// Leaping frog simulation


#include <frog.hpp>

int leap(const int pads_left, const int leaps_made)
{
  //
  // Determine the number of leaps needed to reach the other bank recursively
  //
  // parameters
  // ----------
  // pads_left : const int
  //  - the number of pads left to reach the other bank, including the other bank
  // leaps_made : const int
  //  - the number of leaps already made
  //
  // returns
  // -------
  // int
  //  - the number of jumps needed to reach the other bank from the current pad
  //

  if (pads_left==0) { return leaps_made; }

  int jump=std::uniform_int_distribution<int>(1, pads_left)(std::mt19937_64{std::random_device{}()});
  return leap(pads_left-jump,leaps_made+1);
}
