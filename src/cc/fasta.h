#include <ifstream>
#include <string>


namespace rosalind {
  class Fasta {
   public:
    Fasta(std::ifstream& input);
    Fasta& operator++();
    bool operator!=(const Fasta&) const;

   private:
    std::string curr_name_;
    std::string curr_data_;
    std::ifstream& input_;
  };
}
