cmake_minimum_required(VERSION 3.13)

set(PROJECT_ID matlab_7)

set(SOURCE_FILES
        src/matlab.cpp
        )

set(SOURCES_FILES_TESTS
        test/test_vector.cpp
        test/test_matrix.cpp
        )

include(../SetCommonConfig.cmake)
