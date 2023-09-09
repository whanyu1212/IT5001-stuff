function factors(n)
    count = 0
    factor = 2
    while factor * factor <= n
        if n % factor == 0
            n ÷= factor
            count += 1
        else
            factor += 1
        end
    end
    if n > 1
        count += 1
    end
    return count
end

if abspath(PROGRAM_FILE) == @__FILE__
    println(factors(n))
end

# if abspath(PROGRAM_FILE) == @__FILE__
#     k = factors(65536)
#     println(k)
# end

