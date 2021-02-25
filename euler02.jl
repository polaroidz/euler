
function fib_sum_even(n, a = 0, b = 1, sum = 0)
    if b >= n
        return sum
    else
        if b % 2 == 0
            sum += b
        end

        temp = b
        b = a + b
        a = temp

        return fib_sum_even(n, a, b, sum)
    end
end


function solve()
    #return fib_sum_even(23)
    return fib_sum_even(4 * 10^6)
end

ans = solve()
@time print(ans)
