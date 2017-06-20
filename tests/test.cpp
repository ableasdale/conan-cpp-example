#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "easylogging++.h"

INITIALIZE_EASYLOGGINGPP

unsigned int Factorial( unsigned int number ) {
    return number <= 1 ? number : Factorial(number-1)*number;
}

TEST_CASE( "Factorials are computed", "[factorial]" ) {

    LOG(INFO) << "My first info log using default logger";

    REQUIRE( Factorial(1) == 1 );
	REQUIRE( Factorial(2) == 2 );
	REQUIRE( Factorial(3) == 6 );
	REQUIRE( Factorial(10) == 3628800 );
}
