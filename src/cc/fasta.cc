#include <ifstream>

#include "fasta.h"


namespace rosalind {
  Fasta::Fasta(ifstream& input) : input_(input) { }
  Fasta& Fasta::operator++() {
    std::string line;
    while (std::getline(input_, line)) {
      if (IsNewRecordPrefix(line)) {

      }
    }
  }
}
