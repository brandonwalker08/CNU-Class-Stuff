/*
 /*
 * functionstocomplete.cpp
 *
 *  Created on: Sep 10, 2017
 *      Author: keith
 */

//============================================================================
//	TODO add necessary includes here
//============================================================================


#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "constants.h"



//============================================================================
//	stuff you will need
//============================================================================
//TODO define a structure to track words and number of times they occur

struct uniqueWord{
	std::string wordValue;
	int numOccurences;
};

//TODO add a global array of entry structs (global to this file)

uniqueWord wordArray[100];  //$don't know size of file yet, dummy number$

//TODO add variable to keep track of next available slot in array

int nextIndex = 0;

//TODO define all functions in header file

//done

//zero out array that tracks words and their occurrences

void clearArray(){

	//$just set next index to 0$
	nextIndex = 0;

}

//how many unique words are in array
int getArraySize(){
	return sizeof(wordArray);
}

//get data at a particular location
std::string getArrayWordAt(int i){
	return wordArray[i].wordValue;
}

int getArrayWord_NumbOccur_At(int i){
	return wordArray[i].numOccurences;
}

/*loop through whole file, one line at a time
 * call processLine on each line
 * returns false: myfstream is not open
 *         true: otherwise*/
bool processFile(std::fstream &myfstream){

}

/*Keep track of how many times each token seen*/
void processToken(std::string &token){
	std::cout << token ;
}


/*take 1 line and extract all the tokens from it
feed each token to processToken for recording*/
void processLine(std::string &myString){

	std::stringstream ss(myString);

	std::string tempToken;

	while (getline(ss, tempToken, constants::CHAR_TO_SEARCH_FOR)) {
		processToken(tempToken);
	}
}


/*if you are debugging the file must be in the project parent directory
  in this case Project2 with the .project and .cProject files*/
bool openFile(std::fstream& myfile, const std::string& myFileName,
		std::ios_base::openmode mode = std::ios_base::in){

}

/*iff myfile is open then close it*/
void closeFile(std::fstream& myfile){

}

/* serializes all content in myEntryArray to file outputfilename
 * returns  FAIL_FILE_DID_NOT_OPEN if cannot open outputfilename
 * 			FAIL_NO_ARRAY_DATA if there are 0 entries in myEntryArray
 * 			SUCCESS if all data is written and outputfilename closes OK
 * */
int writeArraytoFile(const std::string &outputfilename){

}

/*
 * Sort myEntryArray based on so enum value.
 * You must provide a solution that handles alphabetic sorting (A-Z)
 * The presence of the enum implies a switch statement based on its value
 * You are provided with a myentry compare function in the cpp file
 */
void sortArray(constants::sortOrder so){

}
