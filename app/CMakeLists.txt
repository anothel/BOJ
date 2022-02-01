add_executable(a "")

target_compile_features(a PRIVATE cxx_std_17)

target_sources(a PRIVATE
                          # main.cc
                          # 2908_Constant.cc
                          # 15649_N_M_1.cc
                          # 15650_N_M_2.cc
                          15651_N_M_3.cc
)