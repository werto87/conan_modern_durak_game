cmake_minimum_required(VERSION 3.15)
project(test_package CXX)

find_package(modern_durak_game REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE modern_durak_game::modern_durak_game)