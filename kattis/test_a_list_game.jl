include("/Users/hanyuwu/Study/IT5001/kattis/a_list_game.jl")
using Test

@testset "a_list_game.jl" begin
    @test factors(65536) == 16
    @test factors(127381) == 3
end