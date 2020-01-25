
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
//                                                                                                                                       //
// frog.hpp                                                                                                                              //
//                                                                                                                                       //
// D. C. Groothuizen Dijkema - December, 2019                                                                                            //
//+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

// Header file for leaping frog simulation


#pragma once

#ifndef FROG_H__
#define FROG_H__

#include <random>
#include <stdexcept>

int leap(const int pads_left, const int leaps_made);
double __declspec(dllexport) average(const int num_pads, const int num_itr);
void __declspec(dllexport) simulate(const int num_pads, const int num_itr, double * const leaps);

double __declspec(dllexport) harmonic(unsigned int n);

#endif // FROG_H__
