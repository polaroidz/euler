
function is_palindrome(n)
    s = string(n)
    r = reverse(s)

    return s == r
end

function solve()
    a = 999

    for i in a:-1:100
        for j in i:-1:100
            n = i * j

            if is_palindrome(n)
                println(i, " ", j)
                return n
            end
        end
    end

    return false
end

ans = solve()
@time print(ans)
