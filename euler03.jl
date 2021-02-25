
function is_prime(n)
    if n < 2
        return false
    end

    if n % 2 == 0
        return n == 2
    end

    root = sqrt(n)
    root = ceil(root)

    for i in 3:2:root
        if n % i == 0
            return false
        end
    end

    return true
end

function solve()
    n = 600851475143

    a = sqrt(n)
    a = ceil(a)

    for i in a:-1:2
        if n % i == 0 && is_prime(i)
            return i
        end
    end

    return false
end

ans = solve()
@time print(ans)
