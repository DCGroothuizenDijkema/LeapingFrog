
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
//                                                                                                                                       //
// frog.hpp                                                                                                                              //
//                                                                                                                                       //
// D. C. Groothuizen Dijkema - December, 2019                                                                                            //
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

// Header file for leaping frog simulation


#include <random>

int leap(const int pads_left, const int jumps_made);
double __declspec(dllexport) probability(const int num_pads, const int num_itr);
void __declspec(dllexport) simulate(const int num_pads, const int num_itr, int * const leaps);