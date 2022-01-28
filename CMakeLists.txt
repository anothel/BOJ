# CMake 프로그램의 최소 버전
cmake_minimum_required(VERSION 3.11)

# 프로젝트 정보
project(
  CodeKata
  VERSION 0.1
  DESCRIPTION "CodeKata"
  LANGUAGES CXX)

# 빌드 형상(Configuration) 및 주절주절 Makefile 생성 여부
set(CMAKE_BUILD_TYPE Debug)
# set(CMAKE_BUILD_TYPE MinSizeRel)
set(CMAKE_VERBOSE_MAKEFILE true)
# set(CMAKE_VERBOSE_MAKEFILE false)

# 실행 파일은 빌드 디렉토리 폴더에 출력.
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

add_subdirectory(app)
