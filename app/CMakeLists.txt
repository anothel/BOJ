add_executable(a "")

target_compile_features(a PRIVATE cxx_std_17)

target_sources(a PRIVATE 
                           main.cc
)