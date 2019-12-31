
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
//                                                                                                                                       //
// frog.cpp                                                                                                                              //
//                                                                                                                                       //
// D. C. Groothuizen Dijkema - December, 2019                                                                                            //
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

// Leaping frog simulation

#include <frog.hpp>

std::random_device rd;
std::mt19937_64 gen(rd());

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
  //  - the number of leaps needed to reach the other bank from the current pad
  //

  if (pads_left==0) { return leaps_made; }

  int jump=std::uniform_int_distribution<int>(1,pads_left)(gen);
  return leap(pads_left-jump,leaps_made+1);
}

double __declspec(dllexport) average(const int num_pads, const int num_itr)
{
  //
  // Determine the average number of leaps needed to reach the other bank
  //
  // parameters
  // ----------
  // num_pads : const int
  //  - the number of pads to the other bank, including the other bank
  // num_itr : const int
  //  - the number of times to run the simulation
  //    the higher num_itr is, the more accurate the approximation
  //
  // returns
  // -------
  // double
  //  - the average number of leaps needed to reach the other bank
  //

  double mean=0.;
  for (int itr=0;itr<num_itr;++itr)
  {
    int jumps=leap(num_pads,0);
    mean+=(jumps-mean)/(itr+1);
  }
  return mean;
}

void __declspec(dllexport) simulate(const int num_pads, const int num_itr, double * const ma)
{
  //
  // Determine the average number of leaps needed to reach the other bank, storing the running approximation of the mean
  //
  // parameters
  // ----------
  // num_pads : const int
  //  - the number of pads to the other bank, including the other bank
  // num_itr : const int
  //  - the number of times to run the simulation
  //    the higher num_itr is, the more accurate the approximation
  // ma : int * const
  //  - the moving average of the number of leaps needed to reach the other bank
  //

  double mean=0.;
  for (int itr=0;itr<num_itr;++itr)
  {
    int jumps=leap(num_pads,0);
    mean+=(jumps-mean)/(itr+1);
    *(ma+itr)=mean;
  }
}

double __declspec(dllexport) harmonic(const unsigned int n)
{
  //
  // Calculate a given harmonic number
  //
  // parameters
  // ----------
  // n : const unsigned int
  //  - a positive integer of which to calculate the harmonic number
  //
  // returns
  // -------
  // double
  //  - `n`th harmonic number
  //
  // throws
  // ------
  // std::invalid_argument
  //  - if `n` is not a positive integer
  //

  if (n<1) { throw std::invalid_argument("`n` must be a positive integer."); }

  // calculate the nth harmonic number
  double h=1.;
  for (int itr=2;itr<=n;++itr) { h+=1./itr; }
  return h;
}
