#ifndef _L1Trig
#define _L1Trig
//#define DEBUG
////////////////////////////////////////////////////////////////////////////
//
// This class gives the L1 trigger response. It requires a vector of Jet
// objects (Jet objects are included) and can also get the L1MET.
// the L1 response is given by 
//
////////////////////////////////////////////////////////////////////////////
#include <vector>
#include <algorithm>
#include "../SimpleJet/SimpleJet.h"
// used to pass calibrated jets to this class, see Init_L1Trig

using namespace std;

class L1Trig {
  float _calib_jet1_et;
  float _calib_jet2_et;
  float _calib_jet3_et;
  float _calib_jet4_et;
  float _L1_met;

 public:
  L1Trig () {
  _calib_jet1_et = 0;
  _calib_jet2_et = 0;
  _calib_jet3_et = 0;
  _calib_jet4_et = 0;
  _L1_met = 0;
  }

  // Function to sort the vector in Pt
  void Sort (vector<SimpleJet> &);
  // Requires a vector of Jet objects and a float for the MET
  void Fill (vector<SimpleJet> &, float);
  // alternate method requiring only the vector of jet, MET is set = 0
  void Fill (vector<SimpleJet> & );
  // Get the standard L1 response for the Multijet Trigger
  bool Response ();
  // Response to the L1 Multijet trigger for the assigned cuts
  bool Response (float, float, float);
  // Response to the L1 MET+Jet trigger for the assigned cuts (this order)
  bool Response (float, float);
};

void L1Trig::Sort ( vector<SimpleJet> & vec_L1jet ) {
  // Overload the < operator to sort Jet objects
  // -------------------------------------------

  sort( vec_L1jet.begin(), vec_L1jet.end() );
  reverse( vec_L1jet.begin(), vec_L1jet.end() );
}

void L1Trig::Fill (vector<SimpleJet> & vec_L1jet, float L1_met) {
  // sort the vector in Pt
  Sort(vec_L1jet);

  _calib_jet1_et = 0;
  _calib_jet2_et = 0;
  _calib_jet3_et = 0;
  _calib_jet4_et = 0;
  _L1_met = 0;

  if (vec_L1jet.size() > 0) {
    _calib_jet1_et = vec_L1jet.at(0).pt();
  }
  if (vec_L1jet.size() > 1) {
    _calib_jet2_et = vec_L1jet.at(1).pt();
  }
  if (vec_L1jet.size() > 2) {
    _calib_jet3_et = vec_L1jet.at(2).pt();
  }
  if (vec_L1jet.size() > 3) {
    _calib_jet4_et = vec_L1jet.at(3).pt();
  }
  _L1_met = L1_met;
}
void L1Trig::Fill (vector<SimpleJet> & vec_L1jet) {
  // sort the vector in Pt
  Sort(vec_L1jet);

  _calib_jet1_et = 0;
  _calib_jet2_et = 0;
  _calib_jet3_et = 0;
  _calib_jet4_et = 0;
  _L1_met = 0;

  if (vec_L1jet.size() > 0) {
    _calib_jet1_et = vec_L1jet.at(0).pt();
  }
  if (vec_L1jet.size() > 1) {
    _calib_jet2_et = vec_L1jet.at(1).pt();
  }
  if (vec_L1jet.size() > 2) {
    _calib_jet3_et = vec_L1jet.at(2).pt();
  }
  if (vec_L1jet.size() > 3) {
    _calib_jet4_et = vec_L1jet.at(3).pt();
  }
}

bool L1Trig::Response () {
#ifdef DEBUG
  std::cout << "_calib_jet1_et = " << _calib_jet1_et << std::endl;
  std::cout << "_calib_jet2_et = " << _calib_jet2_et << std::endl;
  std::cout << "_calib_jet3_et = " << _calib_jet3_et << std::endl;
  std::cout << "_calib_jet4_et = " << _calib_jet4_et << std::endl;
#endif

  // High luminosity thresholds (taken from the trigger TDR)
  if (_calib_jet1_et >= 250. || _calib_jet2_et >= 200. || _calib_jet3_et >= 100. || _calib_jet4_et >= 80.)
    return true;
  return false;
}
bool L1Trig::Response (float ET1, float ET3, float ET4) {
  if (_calib_jet1_et >= ET1 || _calib_jet3_et >= ET3 || _calib_jet4_et >= ET4)
    return true;
  return false;
}
bool L1Trig::Response (float ET1, float L1MET) {
  if (_calib_jet1_et >= ET1 && _L1_met >= L1MET)
    return true;
  return false;
}
#endif // _L1Trig
