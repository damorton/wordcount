#include <boost/python.hpp> // Python modules
#include <fstream> // file I/O
#include <string>
#include <map>
#include <iostream> // cout
#include "boost/algorithm/string.hpp" // to_lower
#include <vector> // vector
#include <algorithm> // pair


//std::map<std::string, int> create_word_count_dictionary(const char *filename)
boost::python::dict create_word_count_dictionary(const char *filename)
{
	//std::map<std::string, int> word_count_dictionary;
	boost::python::dict word_count_dictionary;
	std::ifstream file(filename);
	std::string word;

	if(file.is_open())
	{
		while(file >> word)
		{
			// Store each word in a dictionary
			// Convert to lowercase and check dictionary
			boost::algorithm::to_lower(word);
			//bool doesNotExist = word_count_dictionary.find(word) == word_count_dictionary.end();
			bool keyExists = word_count_dictionary.has_key(word);

			// if the word does not exist store the new word and set the counter to 1
			if(keyExists)
			{
				word_count_dictionary[word] = word_count_dictionary[word] + 1;
				//word_count_dictionary[word] = 1;
			}
			else
			{
				// else increment the counter for that word
				word_count_dictionary[word] = 1;
				//word_count_dictionary[word] = word_count_dictionary[word] + 1;
			}
		}
		file.close();
	}

	return word_count_dictionary;
}

bool compare_value(std::pair<std::string, int> const &a, std::pair<std::string, int> const &b)
{
	return a.second > b.second;
}

std::vector<std::pair<std::string, int> > sort_dictionary_into_vector(std::map<std::string, int> &word_count_dictionary, bool sort_by_key = 1)
{
	// sort the dictionary by dumping the map to a vector and sorting the vector by value
	std::vector<std::pair<std::string, int> > word_count_vector(word_count_dictionary.begin(), word_count_dictionary.end());

	if(sort_by_key)
	{
		// Dictonary already sorted by key
	}
	else
	{
		// Use a value comparator function
		std::sort(word_count_vector.begin(), word_count_vector.end(), compare_value);
	}

	return word_count_vector;
}

void print_top(const char *filename)
{
	/*
	std::map<std::string, int> word_count_dictionary;
	std::vector<std::pair<std::string, int> > word_count_vector;

	word_count_dictionary = create_word_count_dictionary(filename);

	word_count_vector = sort_dictionary_into_vector(word_count_dictionary, 0);

	int count = 0;
	for(std::vector<std::pair<std::string, int> >::const_iterator iterator = word_count_vector.begin(); iterator != word_count_vector.end(); ++iterator)
	{
		count++;
		std::cout << iterator->first << " " << iterator->second << std::endl;
		if(count >= 20)
		{
			break;
		}
	}
	*/
}

BOOST_PYTHON_MODULE(cppExtUtil)
{
	using namespace boost::python;
	def("create_word_count_dictionary", create_word_count_dictionary);
	def("print_top", print_top);
}
