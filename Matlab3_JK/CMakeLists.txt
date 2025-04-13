cmake_minimum_required(VERSION 3.13)

project(matlab_3)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_options(-Wall -Wextra -Werror -Wpedantic -pedantic-errors)

include_directories(include)

set(SOURCE_FILES
    src/matlab.cpp
)

set(MAIN_SOURCE_FILES
    main.cpp
)

set(TEST_SOURCE_FILES
    test/test_vector.cpp
    test/main_gtest.cpp
)

set(INCLUDE_FILES
    include/matlab.hpp
)

add_library(matlab ${SOURCE_FILES} ${INCLUDE_FILES})

add_executable(main ${MAIN_SOURCE_FILES})

add_executable(tests ${TEST_SOURCE_FILES})

target_link_libraries(tests gtest gtest_main)

target_link_libraries(tests matlab)
